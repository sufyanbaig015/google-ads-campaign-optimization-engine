"""Google Ads resource name and text helpers."""

import re
from typing import Union


def sanitize_customer_id(customer_id: str) -> str:
    """Sanitize customer ID by removing hyphens.

    Args:
        customer_id: Customer ID with or without hyphens

    Returns:
        Customer ID without hyphens
    """
    return customer_id.replace("-", "")


def format_customer_id(customer_id: Union[str, int]) -> str:
    """Format customer ID with hyphens for display.

    Args:
        customer_id: Customer ID without hyphens

    Returns:
        Customer ID formatted as XXX-XXX-XXXX
    """
    customer_id = str(customer_id)
    if len(customer_id) == 10 and "-" not in customer_id:
        return f"{customer_id[:3]}-{customer_id[3:6]}-{customer_id[6:]}"
    return customer_id


def truncate_text(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate text to maximum length.

    Args:
        text: Text to truncate
        max_length: Maximum length
        suffix: Suffix to add if truncated

    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def validate_url(url: str) -> bool:
    """Validate if a string is a valid URL.

    Args:
        url: URL string to validate

    Returns:
        True if valid URL, False otherwise
    """
    url_pattern = re.compile(
        r"^https?://"  # http:// or https://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|"  # domain...
        r"localhost|"  # localhost...
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )
    return url_pattern.match(url) is not None


def parse_keyword_match_type(match_type_str: str) -> str:
    """Parse and validate keyword match type.

    Args:
        match_type_str: Match type string

    Returns:
        Normalized match type
    """
    match_type_map = {
        "broad": "BROAD",
        "phrase": "PHRASE",
        "exact": "EXACT",
        "broad match modifier": "BROAD_MATCH_MODIFIER",
        "bmm": "BROAD_MATCH_MODIFIER",
    }

    normalized = match_type_str.lower().strip()
    return match_type_map.get(normalized, "BROAD")


def format_resource_name(resource_type: str, customer_id: str, resource_id: str) -> str:
    """Format a Google Ads resource name.

    Args:
        resource_type: Type of resource (campaigns, adGroups, etc.)
        customer_id: Customer ID
        resource_id: Resource ID

    Returns:
        Formatted resource name
    """
    customer_id = sanitize_customer_id(customer_id)
    return f"customers/{customer_id}/{resource_type}/{resource_id}"


def parse_resource_name(resource_name: str) -> dict:
    """Parse a Google Ads resource name into components.

    Args:
        resource_name: Resource name like "customers/1234567890/campaigns/123"

    Returns:
        Dict with customer_id, resource_type, and resource_id
    """
    parts = resource_name.split("/")
    if len(parts) >= 4 and parts[0] == "customers":
        return {
            "customer_id": parts[1],
            "resource_type": parts[2],
            "resource_id": parts[3],
        }
    return {}


def batch_list(items: list, batch_size: int = 1000) -> list:
    """Split a list into batches.

    Args:
        items: List to batch
        batch_size: Maximum size of each batch

    Returns:
        List of batches
    """
    batches = []
    for i in range(0, len(items), batch_size):
        batches.append(items[i : i + batch_size])
    return batches
