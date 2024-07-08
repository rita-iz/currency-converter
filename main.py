# First step. Save the JSON data to a document called exchange_rates.json
{
    "USD": {
        "EUR": 0.85,
        "GBP": 0.75,
        "JPY": 110.0
    },
    "EUR": {
        "USD": 1.18,
        "GBP": 0.88,
        "JPY": 130.0
    },
    "GBP": {
        "USD": 1.33,
        "EUR": 1.14,
        "JPY": 147.0
    },
    "JPY": {
        "USD": 0.0091,
        "EUR": 0.0077,
        "GBP": 0.0068
    }
}

import json

class CurrencyConverter:
    def __init__(self, rates):
        self.rates = rates
    
    def convert(self, amount, from_currency, to_currency):
        try:
            if from_currency == to_currency:
                return amount
            rate = self.rates[from_currency][to_currency]
            return amount * rate
        except KeyError:
            raise ValueError(f"Conversion rate from {from_currency} to {to_currency} not found.")
    
def main():
    # Exchange rates
    rates = {
        "USD": {
            "EUR": 0.85,
            "GBP": 0.75,
            "JPY": 110.0
        },
        "EUR": {
            "USD": 1.18,
            "GBP": 0.88,
            "JPY": 130.0
        },
        "GBP": {
            "USD": 1.33,
            "EUR": 1.14,
            "JPY": 147.0
        },
        "JPY": {
            "USD": 0.0091,
            "EUR": 0.0077,
            "GBP": 0.0068
        }
    }
    
    converter = CurrencyConverter(rates)
    
    try:
        amount = float(input("Enter the amount to convert: "))
        from_currency = input("Enter the currency to convert from (USD, EUR, GBP, JPY): ").upper()
        to_currency = input("Enter the currency to convert to (USD, EUR, GBP, JPY): ").upper()
        
        converted_amount = converter.convert(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


