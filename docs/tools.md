# Tool catalog

Tools are registered in `google_ads_mcp.tools` and grouped by domain modules under `src/google_ads_mcp/tools/`.

## Account management

| Tool | Description |
|------|-------------|
| `list_accounts` | List accessible Google Ads accounts |
| `get_account_info` | Account details and scores |
| `get_account_hierarchy` | Account hierarchy tree |

## Campaigns (`tools/campaigns.py`)

| Tool | Description |
|------|-------------|
| `create_campaign` | Create campaign with budget and targeting |
| `update_campaign` | Update settings / bidding |
| `pause_campaign` / `resume_campaign` | Lifecycle |
| `list_campaigns` | Filter and list campaigns |
| `get_campaign` | Campaign details |
| `delete_campaign` | Remove campaign |
| `copy_campaign` | Duplicate campaign |
| `create_ad_schedule` | Dayparting schedules |
| `get_campaign_overview` | Structure + performance overview |

## Ad groups (`tools/ad_groups.py`)

| Tool | Description |
|------|-------------|
| `create_ad_group` | Create ad group |
| `update_ad_group` | Update settings / bids |
| `list_ad_groups` | List with filters |

## Ads (`tools/ads.py`)

| Tool | Description |
|------|-------------|
| `create_responsive_search_ad` | RSA |
| `create_expanded_text_ad` | Expanded text ad |
| `list_ads` / `update_ad` / `pause_ad` / `enable_ad` / `delete_ad` | Ad lifecycle |
| `compare_ad_performance` | Side-by-side comparison |
| `get_ad_group_performance_ranking` | Rank ads by efficiency |
| `identify_optimization_opportunities` | Optimization suggestions |
| `calculate_roas_by_ad` | ROAS by ad |
| `analyze_ad_strength_trends` | Strength trends |

## Keywords (`tools/keywords.py`)

| Tool | Description |
|------|-------------|
| `add_keywords` / `add_negative_keywords` | Add keywords |
| `list_keywords` | List with quality scores |
| `update_keyword_bid` / `delete_keyword` / `pause_keyword` / `enable_keyword` | Lifecycle |
| `get_keyword_performance` | Performance + quality |
| `auto_suggest_negative_keywords` | Suggest negatives from search terms |
| `get_search_terms_insights` | Search term insights |

## Budgets (`tools/budgets.py`)

| Tool | Description |
|------|-------------|
| `create_budget` / `update_budget` / `list_budgets` | Budget CRUD |

## Assets (`tools/assets.py`)

| Tool | Description |
|------|-------------|
| `upload_image_asset` / `upload_text_asset` | Upload assets |
| `list_assets` | List assets |

## Extensions (`tools/extensions.py`)

| Tool | Description |
|------|-------------|
| `create_sitelink_extensions` | Sitelinks |
| `create_callout_extensions` | Callouts |
| `create_structured_snippet_extensions` | Structured snippets |
| `create_call_extensions` | Call extensions |
| `list_extensions` / `delete_extension` | Manage extensions |

## Audiences (`tools/audiences.py`)

| Tool | Description |
|------|-------------|
| `create_custom_audience` | Custom audience |
| `add_audience_targeting` | Attach audience targeting |
| `list_audiences` | List audiences |
| `get_audience_performance` | Audience metrics |

## Geography (`tools/geography.py`)

| Tool | Description |
|------|-------------|
| `get_location_performance` | Location metrics |
| `optimize_geographic_targeting` | Geo optimization suggestions |

## Bidding (`tools/bidding.py`)

| Tool | Description |
|------|-------------|
| `create_portfolio_bidding_strategy` | Portfolio strategies |
| `list_bidding_strategies` | List strategies |
| `set_bid_adjustments` | Device / location / demo bids |
| `get_bid_adjustment_performance` | Adjustment ROI |
| `get_device_performance` | Device breakdown |

## Reporting (`tools/reporting.py`)

| Tool | Description |
|------|-------------|
| `get_campaign_performance` | Campaign report |
| `get_ad_group_performance` | Ad group report |
| `get_search_terms_report` | Search terms |
| `get_recommendations` / `apply_recommendation` | Recommendations |
| `get_change_history` | Change history |
