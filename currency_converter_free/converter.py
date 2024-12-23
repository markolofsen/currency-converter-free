import logging
import requests
import xml.etree.ElementTree as ET
from diskcache import Cache

class CurrencyConverter:
    CBR_URL = "https://www.cbr.ru/scripts/XML_daily.asp"
    ECB_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"

    def __init__(self, source="BOTH", cache_dir="/tmp/rates_cache"):
        """
        Initialize the CurrencyConverter with default source and disk-based caching.
        :param source: The default source for rates ("CBR", "ECB", or "BOTH").
        :param cache_dir: Directory for persistent cache.
        """
        self.default_source = source.upper()
        self.cache = Cache(cache_dir)
        logging.info(f"Initialized persistent cache at {cache_dir}")

    def _fetch_cbr_rates(self):
        """Fetch rates from the CBR API."""
        logging.info("Fetching rates from CBR API...")
        resp = requests.get(self.CBR_URL, timeout=10)
        resp.raise_for_status()
        xml_content = resp.text

        tree = ET.fromstring(xml_content)
        rates_dict = {"RUB": 1.0}  # Base currency is RUB

        for valute_el in tree.findall("Valute"):
            char_code_el = valute_el.find("CharCode")
            value_el = valute_el.find("Value")
            nominal_el = valute_el.find("Nominal")

            if char_code_el is not None and value_el is not None and nominal_el is not None:
                char_code = char_code_el.text.strip().upper()
                value_str = value_el.text.strip().replace(",", ".")
                nominal_str = nominal_el.text.strip()

                try:
                    nominal = int(nominal_str)
                    rate_float = float(value_str)
                    rate_per_one = rate_float / nominal
                    rates_dict[char_code] = rate_per_one
                except ValueError:
                    pass

        logging.info("Fetched rates from CBR.")
        return rates_dict

    def _fetch_ecb_rates(self):
        """Fetch rates from the ECB API."""
        logging.info("Fetching rates from ECB API...")
        resp = requests.get(self.ECB_URL, timeout=10)
        resp.raise_for_status()
        xml_content = resp.text

        tree = ET.fromstring(xml_content)
        rates_dict = {"EUR": 1.0}  # Base currency is EUR

        for cube_time_el in tree.findall(".//{*}Cube[@time]"):
            for cube_el in cube_time_el.findall("{*}Cube"):
                cur = cube_el.attrib.get("currency")
                rate_str = cube_el.attrib.get("rate")
                if cur and rate_str:
                    try:
                        rates_dict[cur.upper()] = float(rate_str)
                    except ValueError:
                        pass

        logging.info("Fetched rates from ECB.")
        return rates_dict

    def _get_rates(self, source):
        """Get rates from the specified source, with disk-based caching."""
        if source in self.cache:
            logging.info(f"Fetching {source} rates from cache...")
            return self.cache[source]

        if source == "CBR":
            rates = self._fetch_cbr_rates()
        elif source == "ECB":
            rates = self._fetch_ecb_rates()
        else:
            raise ValueError("Invalid source specified. Use 'CBR' or 'ECB'.")

        # Store in cache with a default TTL of 24 hours (86400 seconds)
        self.cache.set(source, rates, expire=86400)
        return rates

    def get_combined_rates(self, source=None):
        """
        Fetch combined rates from the specified or default source.
        :param source: The source to use ("CBR", "ECB", or "BOTH"). Defaults to the initialized source.
        :return: A dictionary of combined rates.
        """
        source = source.upper() if source else self.default_source
        combined_rates = {}

        if source in {"CBR", "BOTH"}:
            cbr_rates = self._get_rates("CBR")
            combined_rates.update(cbr_rates)

        if source in {"ECB", "BOTH"}:
            ecb_rates = self._get_rates("ECB")
            if "EUR" in ecb_rates and "RUB" in combined_rates:
                # Convert ECB rates to RUB base
                eur_to_rub = combined_rates.get("EUR", 1.0)
                for currency, rate in ecb_rates.items():
                    if currency != "EUR":
                        combined_rates[currency] = rate * eur_to_rub
            else:
                combined_rates.update(ecb_rates)

        return combined_rates

    def convert(self, amount, from_cur, to_cur, source=None):
        """
        Convert an amount between currencies using specified or default source rates.
        Handles intermediate conversion through the base currency if necessary.
        :param amount: The amount to convert.
        :param from_cur: The source currency code.
        :param to_cur: The target currency code.
        :param source: The source to use ("CBR", "ECB", or "BOTH"). Defaults to the initialized source.
        :return: The converted amount or None if conversion is not possible.
        """
        rates = self.get_combined_rates(source)
        base_currency = "RUB" if source == "CBR" else "EUR"  # Determine the base currency of the source

        if from_cur == to_cur:
            return amount

        if from_cur not in rates or to_cur not in rates:
            logging.warning(f"Conversion not possible: {from_cur} to {to_cur}. Rates missing.")
            return None

        # Direct conversion if both currencies are related to the base currency
        if from_cur == base_currency:
            return amount / rates[to_cur]
        elif to_cur == base_currency:
            return amount * rates[from_cur]

        # Indirect conversion through the base currency
        try:
            amount_in_base = amount * rates[from_cur]  # Convert to base currency
            converted_amount = amount_in_base / rates[to_cur]  # Convert from base currency to target
            return converted_amount
        except KeyError:
            logging.warning(f"Conversion not possible: {from_cur} to {to_cur}. KeyError in rates.")
            return None


    def available_currencies(self, source=None):
        """
        List all available currencies for conversion.
        :param source: The source to use ("CBR", "ECB", or "BOTH"). Defaults to the initialized source.
        :return: A sorted list of available currency codes.
        """
        rates = self.get_combined_rates(source)
        return sorted(rates.keys())


# Example Usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    converter = CurrencyConverter(source="BOTH")

    logging.info("\nAvailable currencies: %s", converter.available_currencies())

    amount = 10000
    from_currency = "RUB"
    to_currency = "USD"
    converted = converter.convert(amount, from_currency, to_currency)
    logging.info("\n%d %s => %.4f %s", amount, from_currency, converted, to_currency)
