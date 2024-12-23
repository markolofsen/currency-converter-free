
# Currency Converter Free

**Currency Converter Free** is a Python library designed for seamless and efficient currency conversion, leveraging exchange rates from two trusted sources: the Central Bank of Russia (CBR) and the European Central Bank (ECB). With its robust caching and flexibility, this library is ideal for financial applications requiring reliable currency data.

## Key Features

- **Multiple Data Sources**: Fetch exchange rates from CBR, ECB, or combine both for comprehensive currency coverage.
- **Disk-Based Caching**: Persistent caching reduces API calls and boosts performance.
- **Automatic Base Currency Management**: Transparently handles base currency differences (RUB for CBR and EUR for ECB).
- **Flexible Conversion**: Convert between any two supported currencies with ease.
- **Customizable**: Easily configurable to adjust caching behavior, data sources, or apply currency-specific correction factors.
- **Optimized for Performance**: Uses efficient caching and data handling techniques.

---

## Installation

Install the library via `pip`:

```bash
pip install currency-converter-free
```

### Requirements

- Python 3.7+
- [Requests](https://pypi.org/project/requests/)
- [DiskCache](https://pypi.org/project/diskcache/)

If the library is installed manually, ensure dependencies are met:

```bash
pip install requests diskcache
```

---

## Usage

### Basic Example

```python
from currency_converter_free import CurrencyConverter

# Initialize the converter
converter = CurrencyConverter()

# Convert 100 USD to EUR
usd_to_eur = converter.convert(100, 'USD', 'EUR')
print(f"100 USD = {usd_to_eur:.2f} EUR")

# Convert 100 RUB to USD
rub_to_usd = converter.convert(100, 'RUB', 'USD')
print(f"100 RUB = {rub_to_usd:.2f} USD")

# List available currencies
currencies = converter.available_currencies()
print("Supported currencies:", currencies)
```

### Advanced Example

#### Specify Data Source

Choose between CBR, ECB, or both sources for exchange rates:

```python
from currency_converter_free import CurrencyConverter

# Use CBR rates only
converter_cbr = CurrencyConverter(source="CBR")

# Use ECB rates only
converter_ecb = CurrencyConverter(source="ECB")

# Use both CBR and ECB rates
converter_combined = CurrencyConverter(source="BOTH")
```

#### Customize Cache Directory

To persist cache in a specific location:

```python
from currency_converter_free import CurrencyConverter

# Specify a custom cache directory
converter = CurrencyConverter(cache_dir="/custom/cache/directory")
```

---

## Supported Sources

- **CBR (Central Bank of Russia)**: Provides rates with RUB as the base currency.
- **ECB (European Central Bank)**: Offers rates with EUR as the base currency.

When using the `"BOTH"` source, the library intelligently combines rates from CBR and ECB, prioritizing accuracy for RUB-based and EUR-based conversions.

---

## API Reference

### `CurrencyConverter`

#### Initialization

```python
CurrencyConverter(source="BOTH", cache_dir="/tmp/rates_cache")
```

- **Parameters:**
  - `source` (str): Selects the data source (`"CBR"`, `"ECB"`, or `"BOTH"`). Default is `"BOTH"`.
  - `cache_dir` (str): Directory for persistent caching. Default is `"/tmp/rates_cache"`.

#### Methods

- **`convert(amount, from_cur, to_cur, source=None)`**
  - Converts an amount from one currency to another.
  - **Parameters:**
    - `amount` (float): The amount to convert.
    - `from_cur` (str): Source currency code.
    - `to_cur` (str): Target currency code.
    - `source` (str, optional): Specify source (`"CBR"`, `"ECB"`, or `"BOTH"`). Defaults to initialized source.
  - **Returns:** `float` (converted amount) or `None` if conversion is unavailable.

- **`available_currencies(source=None)`**
  - Lists all supported currencies.
  - **Parameters:**
    - `source` (str, optional): Specify source (`"CBR"`, `"ECB"`, or `"BOTH"`). Defaults to initialized source.
  - **Returns:** `List[str]` (sorted list of supported currencies).

---

## Development & Contributions

We welcome contributions to enhance this library! You can:

1. Report issues or suggest features via [GitHub Issues](https://github.com/markolofsen/currency-converter-free).
2. Submit pull requests for bug fixes or new features.

### Development Workflow

1. Clone the repository:
   ```bash
   git clone https://github.com/markolofsen/currency-converter-free.git
   cd currency-converter-free
   ```

2. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run tests to verify changes:
   ```bash
   pytest
   ```

---

## License

This project is licensed under the MIT License. For more details, refer to the [LICENSE](LICENSE) file.

---

## About Unrealos.com

Currency Converter Free is developed and maintained by [Unrealos.com](https://unrealos.com), a pioneer in SaaS, PaaS, and web-service solutions. For inquiries, contact us at [m@unrealos.com](mailto:m@unrealos.com).