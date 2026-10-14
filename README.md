# Google Ads MCP Server

MCP (Model Context Protocol) server for **Google Ads API v21**. Lets AI assistants create, manage, and optimize Google Ads campaigns through natural language.

## Requirements

- Python 3.10+
- Google Ads account with API access
- Developer token (Basic or Standard)

## Install

```bash
git clone https://github.com/YOUR_USER/google-ads-mcp-complete.git
cd google-ads-mcp-complete
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

## Configuration

Copy the example config and fill in your credentials:

```bash
cp config.example.json ~/.config/google-ads-mcp/config.json
```

```json
{
  "client_id": "YOUR_OAUTH_CLIENT_ID",
  "client_secret": "YOUR_OAUTH_CLIENT_SECRET",
  "refresh_token": "YOUR_REFRESH_TOKEN",
  "developer_token": "YOUR_DEVELOPER_TOKEN",
  "login_customer_id": "YOUR_MANAGER_ACCOUNT_ID",
  "use_proto_plus": true
}
```

The server also checks `~/.google-ads-mcp.json` and `./google-ads-config.json`.

See [docs/setup.md](docs/setup.md) for OAuth and developer token steps.

## Run

```bash
google-ads-mcp
# or
python -m google_ads_mcp
```

### Cursor / Claude MCP config

See [examples/mcp-config.example.json](examples/mcp-config.example.json).

## Tools

40+ tools covering accounts, campaigns, ads, keywords, budgets, extensions, audiences, geography, bidding, and reporting.

Full catalog: [docs/tools.md](docs/tools.md)

## Development

```bash
pip install -e ".[dev]"
pytest
ruff check src tests
```

## License

MIT — see [LICENSE](LICENSE).
