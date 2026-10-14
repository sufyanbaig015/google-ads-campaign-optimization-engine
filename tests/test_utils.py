"""Smoke tests for utility helpers."""

from datetime import date

from google_ads_mcp.utils import (
    batch_list,
    currency_to_micros,
    format_currency,
    format_customer_id,
    format_percentage,
    format_resource_name,
    micros_to_currency,
    parse_date,
    parse_keyword_match_type,
    parse_resource_name,
    sanitize_customer_id,
    truncate_text,
    validate_url,
)


def test_micros_roundtrip():
    assert micros_to_currency(1_500_000) == 1.5
    assert currency_to_micros(1.5) == 1_500_000
    assert currency_to_micros("$2,000.00") == 2_000_000_000


def test_format_currency():
    assert format_currency(12.5, "USD") == "$12.50"
    assert format_currency(1000, "JPY") == "¥1,000"


def test_format_percentage():
    assert format_percentage(0.156) == "15.60%"


def test_parse_date():
    assert parse_date("2024-01-15") == date(2024, 1, 15)
    assert parse_date("20240115") == date(2024, 1, 15)


def test_customer_id_helpers():
    assert sanitize_customer_id("123-456-7890") == "1234567890"
    assert format_customer_id("1234567890") == "123-456-7890"


def test_resource_name_helpers():
    name = format_resource_name("campaigns", "123-456-7890", "99")
    assert name == "customers/1234567890/campaigns/99"
    parsed = parse_resource_name(name)
    assert parsed["customer_id"] == "1234567890"
    assert parsed["resource_type"] == "campaigns"
    assert parsed["resource_id"] == "99"


def test_text_and_url_helpers():
    assert truncate_text("hello world", 8) == "hello..."
    assert validate_url("https://example.com/path")
    assert not validate_url("not-a-url")
    assert parse_keyword_match_type("exact") == "EXACT"
    assert parse_keyword_match_type("unknown") == "BROAD"


def test_batch_list():
    assert batch_list(list(range(5)), 2) == [[0, 1], [2, 3], [4]]
