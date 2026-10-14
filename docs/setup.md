# Setup guide

## 1. Developer token

1. Sign in to [Google Ads](https://ads.google.com).
2. Go to **Tools & Settings → API Center**.
3. Apply for a developer token (Basic access is enough for most MCP use).

## 2. OAuth credentials

1. Open [Google Cloud Console](https://console.cloud.google.com/).
2. Create (or select) a project.
3. Enable the **Google Ads API**.
4. Create OAuth 2.0 Client ID credentials (Desktop or Web app).
5. Download the client ID and client secret.

## 3. Refresh token

Generate a refresh token using Google’s OAuth playground or the Ads API auth examples, then store it in your config file.

## 4. Config file locations

The server loads the first file that exists:

1. `~/.config/google-ads-mcp/config.json`
2. `~/.google-ads-mcp.json`
3. `./google-ads-config.json`

Start from [`config.example.json`](../config.example.json).

| Field | Description |
|-------|-------------|
| `client_id` | OAuth client ID |
| `client_secret` | OAuth client secret |
| `refresh_token` | Long-lived refresh token |
| `developer_token` | Ads API developer token |
| `login_customer_id` | Manager (MCC) account ID if using a manager account |
| `use_proto_plus` | Prefer `true` |

Never commit real credentials. `config.json`, `credentials.json`, and similar files are listed in `.gitignore`.

## 5. Verify

```bash
pip install -e .
google-ads-mcp
```

Wire the server into your MCP client using [examples/mcp-config.example.json](../examples/mcp-config.example.json), then ask the assistant to `list_accounts`.
