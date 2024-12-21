
# Currency Converter Free

Currency Converter Free is a Python library designed to fetch and combine exchange rates from two trusted sources: the Central Bank of Russia (CBR) and the European Central Bank (ECB). The library provides an easy-to-use interface for currency conversion and employs disk-based caching mechanisms for optimal performance.

## Key Features

- **Multiple Data Sources**: Fetch exchange rates from both the CBR and ECB, ensuring comprehensive coverage of currencies.
- **Disk-Based Caching**: Utilizes persistent disk caching to store exchange rates, reducing unnecessary API calls and enhancing performance.
- **Automatic Base Currency Handling**: Transparently manages base currency differences between CBR (RUB) and ECB (EUR).
- **Easy Conversion**: Convert between any two supported currencies with a single function call.
- **Extensible**: Easily adaptable for additional data sources or custom fetchers.

## Installation

Install the library using pip:

```bash
pip install currency-converter-free
```

## Requirements

- Python 3.7+
- [Requests](https://pypi.org/project/requests/)
- [DiskCache](https://pypi.org/project/diskcache/)

## Installation of Dependencies

If not using `pip` to install `currency-converter-free`, ensure all dependencies are installed:

```bash
pip install requests diskcache
```

## Usage

### Basic Example

```python
from currency_converter_free import CurrencyConverter

# Initialize the converter with default settings (both CBR and ECB sources)
converter = CurrencyConverter()

# Convert 100 USD to EUR
amount_in_eur = converter.convert(100, 'USD', 'EUR')
print(f"100 USD = {amount_in_eur:.2f} EUR")

# Convert 100 RUB to USD
amount_in_usd = converter.convert(100, 'RUB', 'USD')
print(f"100 RUB = {amount_in_usd:.2f} USD")

# List all available currencies
available_currencies = converter.available_currencies()
print("Available currencies:", available_currencies)
```

### Advanced Options

#### Specifying Data Source

The `source` parameter allows you to choose the data source for fetching exchange rates. You can specify `"CBR"`, `"ECB"`, or `"BOTH"` to use both sources simultaneously.

```python
from currency_converter_free import CurrencyConverter

# Initialize the converter to use only CBR rates
converter_cbr = CurrencyConverter(source="CBR")

# Initialize the converter to use only ECB rates
converter_ecb = CurrencyConverter(source="ECB")

# Initialize the converter to use both CBR and ECB rates
converter_both = CurrencyConverter(source="BOTH")
```

**Parameters:**

- `source` (str): The source for exchange rates. Accepted values are:
  - `"CBR"`: Use only the Central Bank of Russia rates.
  - `"ECB"`: Use only the European Central Bank rates.
  - `"BOTH"`: Combine rates from both CBR and ECB for comprehensive coverage.
  
**Default:** `"BOTH"`

#### Customizing Cache Directory

Specify a custom directory for storing cached exchange rates. This is useful for persisting cache across different environments or systems.

```python
from currency_converter_free import CurrencyConverter

# Initialize the converter with a custom cache directory
converter = CurrencyConverter(cache_dir="/path/to/your/cache_directory")
```

**Parameters:**

- `cache_dir` (str): The directory path where cached exchange rates will be stored.

**Default:** `"/tmp/rates_cache"`

## Supported Sources

- **Central Bank of Russia (CBR)**: Provides exchange rates with the Russian Ruble (RUB) as the base currency.
- **European Central Bank (ECB)**: Offers exchange rates with the Euro (EUR) as the base currency.

The library intelligently combines rates from both sources, prioritizing CBR for RUB-based conversions and ECB for EUR-based conversions when using the `"BOTH"` option.

## API Reference

### `CurrencyConverter` Class

#### `__init__(self, source="BOTH", cache_dir="/tmp/rates_cache")`

Initialize the CurrencyConverter with default source and disk-based caching.

- **Parameters:**
  - `source` (str): The default source for rates. Accepted values are `"CBR"`, `"ECB"`, or `"BOTH"`. Defaults to `"BOTH"`.
  - `cache_dir` (str): Directory for persistent cache. Defaults to `"/tmp/rates_cache"`.

#### `convert(self, amount, from_cur, to_cur, source=None)`

Convert an amount between currencies using specified or default source rates.

- **Parameters:**
  - `amount` (float): The amount to convert.
  - `from_cur` (str): The source currency code.
  - `to_cur` (str): The target currency code.
  - `source` (str, optional): The source to use (`"CBR"`, `"ECB"`, or `"BOTH"`). Defaults to the initialized source.

- **Returns:**
  - `float` or `None`: The converted amount or `None` if conversion is not possible.

#### `available_currencies(self, source=None)`

List all available currencies for conversion.

- **Parameters:**
  - `source` (str, optional): The source to use (`"CBR"`, `"ECB"`, or `"BOTH"`). Defaults to the initialized source.

- **Returns:**
  - `List[str]`: A sorted list of available currency codes.

## Contributing

We welcome contributions to improve this library. Please submit issues or pull requests via our [GitHub repository](https://github.com/markolofsen/currency-converter-free).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## About Unrealos.com

Currency Converter Free is developed and maintained by [Unrealos.com](https://unrealos.com), a company specializing in SaaS, PaaS, and web-service solutions. For inquiries, please contact us at [m@unrealos.com](mailto:m@unrealos.com).
