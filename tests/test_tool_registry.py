"""Smoke tests for the MCP tool registry."""

from unittest.mock import MagicMock

from google_ads_mcp.tools import GoogleAdsTools


def _build_tools() -> GoogleAdsTools:
    auth = MagicMock()
    error_handler = MagicMock()
    return GoogleAdsTools(auth, error_handler)


def test_registry_has_core_tools():
    tools = _build_tools()
    names = set(tools._tools_registry.keys())

    expected = {
        "list_accounts",
        "create_campaign",
        "list_campaigns",
        "create_ad_group",
        "create_responsive_search_ad",
        "add_keywords",
        "create_budget",
        "get_campaign_performance",
        "create_portfolio_bidding_strategy",
    }
    missing = expected - names
    assert not missing, f"Missing tools: {missing}"


def test_get_all_tools_returns_mcp_tools():
    tools = _build_tools()
    mcp_tools = tools.get_all_tools()
    assert len(mcp_tools) >= 40
    tool_names = {t.name for t in mcp_tools}
    assert "list_accounts" in tool_names
    assert "create_campaign" in tool_names


def test_registry_handlers_are_callable():
    tools = _build_tools()
    for name, meta in tools._tools_registry.items():
        assert callable(meta["handler"]), f"{name} handler is not callable"
        assert "description" in meta
