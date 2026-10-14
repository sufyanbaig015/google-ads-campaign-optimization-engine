"""Currency conversion and formatting helpers."""

import re
from decimal import Decimal
from typing import Union


def micros_to_currency(micros: int) -> float:
    """Convert micros to currency amount.

    Args:
        micros: Amount in micros (1,000,000 micros = 1 currency unit)

    Returns:
        Currency amount as float
    """
    return micros / 1_000_000


def currency_to_micros(amount: Union[float, Decimal, str]) -> int:
    """Convert currency amount to micros.

    Args:
        amount: Currency amount

    Returns:
        Amount in micros
    """
    if isinstance(amount, str):
        # Remove currency symbols and commas
        amount = re.sub(r"[^\d.-]", "", amount)
        amount = float(amount)
    return int(amount * 1_000_000)


def format_currency(amount: Union[float, int], currency_code: str = "USD") -> str:
    """Format currency amount with symbol.

    Args:
        amount: Currency amount
        currency_code: ISO 4217 currency code

    Returns:
        Formatted currency string
    """
    currency_symbols = {
        "USD": "$",
        "EUR": "€",
        "GBP": "£",
        "JPY": "¥",
        "AUD": "A$",
        "CAD": "C$",
        "CHF": "CHF",
        "CNY": "¥",
        "INR": "₹",
    }

    symbol = currency_symbols.get(currency_code, currency_code + " ")

    # Format with appropriate decimal places
    if currency_code == "JPY":
        return f"{symbol}{amount:,.0f}"
    else:
        return f"{symbol}{amount:,.2f}"


def format_percentage(value: float, decimals: int = 2) -> str:
    """Format a decimal value as percentage.

    Args:
        value: Decimal value (0.15 = 15%)
        decimals: Number of decimal places

    Returns:
        Formatted percentage string
    """
    return f"{value * 100:.{decimals}f}%"
