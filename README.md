# Currency Converter Free

Currency Converter Free is a Python library designed to fetch and combine exchange rates from two trusted sources: the Central Bank of Russia (CBR) and the European Central Bank (ECB). The library provides an easy-to-use interface for currency conversion and supports caching mechanisms for optimal performance.

## Key Features

- **Multiple Data Sources**: Fetch exchange rates from both the CBR and ECB, ensuring comprehensive coverage of currencies.
- **Caching**: Supports both in-memory and persistent disk caching for efficient performance.
- **Automatic Base Currency Handling**: Handles base currency differences between CBR (RUB) and ECB (EUR) transparently.
- **Easy Conversion**: Convert between any two supported currencies with a single function call.
- **Extensible**: Easily adaptable for additional data sources or custom fetchers.

## Installation

Install the library using pip:

```bash
pip install currency-converter-free
```

## Usage

### Basic Example

```python
from currency_converter_free import CurrencyConverter

# Initialize the converter
converter = CurrencyConverter(persistent=True)

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

#### Persistent Caching

Enable disk-based caching to retain exchange rates between sessions:

```python
converter = CurrencyConverter(persistent=True)
```

#### In-Memory Caching

Use in-memory caching for fast temporary storage:

```python
converter = CurrencyConverter()
```

## Supported Sources

- **Central Bank of Russia (CBR)**: Provides exchange rates with the Russian Ruble (RUB) as the base currency.
- **European Central Bank (ECB)**: Offers exchange rates with the Euro (EUR) as the base currency.

The library intelligently combines rates from both sources, prioritizing CBR for RUB-based conversions and ECB for EUR-based conversions.

## Requirements

- Python 3.7+
- Requests
- CacheTools
- DiskCache

## Contributing

We welcome contributions to improve this library. Please submit issues or pull requests via our [GitHub repository](https://github.com/markolofsen/currency-converter-free).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## About Unrealos.com

Currency Converter Free is developed and maintained by [Unrealos.com](https://unrealos.com), a company specializing in SaaS, PaaS, and web-service solutions. For inquiries, please contact us at [m@unrealos.com](mailto:m@unrealos.com).

