"""Date parsing and range helpers."""

from datetime import date, datetime, timedelta
from typing import Tuple, Union


def parse_date(date_str: str) -> date:
    """Parse date string in various formats.

    Args:
        date_str: Date string in format YYYY-MM-DD, YYYYMMDD, or MM/DD/YYYY

    Returns:
        date object
    """
    # Remove any whitespace
    date_str = date_str.strip()

    # Try different formats
    formats = [
        "%Y-%m-%d",  # 2024-01-15
        "%Y%m%d",  # 20240115
        "%m/%d/%Y",  # 01/15/2024
        "%d/%m/%Y",  # 15/01/2024
        "%Y/%m/%d",  # 2024/01/15
    ]

    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt).date()
        except ValueError:
            continue

    raise ValueError(f"Unable to parse date: {date_str}")


def format_date_range(start_date: Union[str, date], end_date: Union[str, date]) -> str:
    """Format a date range for display.

    Args:
        start_date: Start date
        end_date: End date

    Returns:
        Formatted date range string
    """
    if isinstance(start_date, str):
        start_date = parse_date(start_date)
    if isinstance(end_date, str):
        end_date = parse_date(end_date)

    return f"{start_date.strftime('%b %d, %Y')} - {end_date.strftime('%b %d, %Y')}"


def get_date_range_dates(date_range: str) -> Tuple[date, date]:
    """Convert a date range string to start and end dates.

    Args:
        date_range: Date range like "LAST_30_DAYS", "THIS_MONTH", etc.

    Returns:
        Tuple of (start_date, end_date)
    """
    today = date.today()

    if date_range == "TODAY":
        return today, today
    elif date_range == "YESTERDAY":
        yesterday = today - timedelta(days=1)
        return yesterday, yesterday
    elif date_range == "LAST_7_DAYS":
        return today - timedelta(days=6), today
    elif date_range == "LAST_14_DAYS":
        return today - timedelta(days=13), today
    elif date_range == "LAST_30_DAYS":
        return today - timedelta(days=29), today
    elif date_range == "LAST_90_DAYS":
        return today - timedelta(days=89), today
    elif date_range == "THIS_MONTH":
        start = today.replace(day=1)
        return start, today
    elif date_range == "LAST_MONTH":
        # First day of last month
        if today.month == 1:
            start = date(today.year - 1, 12, 1)
            end = date(today.year - 1, 12, 31)
        else:
            start = date(today.year, today.month - 1, 1)
            # Last day of last month
            if today.month == 1:
                end = date(today.year - 1, 12, 31)
            else:
                next_month_first = date(today.year, today.month, 1)
                end = next_month_first - timedelta(days=1)
        return start, end
    elif date_range == "THIS_YEAR":
        return date(today.year, 1, 1), today
    elif date_range == "LAST_YEAR":
        return date(today.year - 1, 1, 1), date(today.year - 1, 12, 31)
    elif date_range == "ALL_TIME":
        # Return a very old date to today
        return date(2000, 1, 1), today
    else:
        # Try to parse custom range like "2024-01-01,2024-12-31"
        if "," in date_range:
            start_str, end_str = date_range.split(",", 1)
            return parse_date(start_str.strip()), parse_date(end_str.strip())
        else:
            raise ValueError(f"Unknown date range: {date_range}")
