# MEMORY.md

## Project Memory & Context

### Architectural & Research Decisions
- **2026-08-12**: Conducted SpaceX (NASDAQ: SPCX) stock research following its historic IPO in June 2026.
- **2026-08-12**: Created automated Short Covering Dashboard (`index.html`, `update_dashboard_data.py`, `server.py`).
- **2026-08-12**: Fully uncoupled from local Mac environment! Deployed permanent Serverless Dashboard to GitHub Pages (`https://tonytcfu.github.io/spcx-dashboard/`).
- **2026-08-25**: Connected 100% genuine Yahoo Finance / NASDAQ live exchange feed for market settlement and volume metrics.
- **2026-08-26**: Implemented browser direct API ingestion engine with CORS proxies (Note: public proxies subsequently degraded/required paid keys).
- **2026-09-04/05**: **Price Change Benchmark Decoupling & Alignment**: Discovered that Dashboard previously labeled previous day's close (+6.42% over Sep 2) with the current day's live banner, causing severe confusion with broker real-time apps. Decoupled clock time from data session validation, explicitly displayed the previous close reference price in the change badge.
- **2026-09-11**: **Auto-Update Root-Cause Resolution & Full Cloud Verification**: Diagnosed that GitHub Actions workflow was rejected during terminal git push because the user's PAT lacked `workflow` scope. Removed local LaunchAgent per user instruction. User created `.github/workflows/update_data.yml` via Chrome. Fixed `cache: 'pip'` failure by committing root `requirements.txt`. Successfully triggered Cloud Action (`run/34555677228`), which executed in 9s and auto-committed `4235c12` back to master via `github-actions[bot]`. 100% serverless, cloud-native automated updating permanently active.
- **2026-09-19**: **Dashboard Frozen at Sep 10 Root-Cause Resolution (NaN Ingestion & APFS Dataless Recovery)**:
  1. *Root Cause*: On Sep 18 (Quadruple Witching, 335M vol), Yahoo Finance temporarily returned `null`/`NaN` for close price during settlement transition. Python's default `json.dump` serialized literal `NaN`, violating RFC 8259 JSON spec. The browser's `JSON.parse` threw a `SyntaxError` and fell back to the hardcoded default dataset (Sep 10).
  2. *Ingestion Hardening*: Modified `update_dashboard_data.py` to add fallback chains (Open -> `regularMarketPrice` -> previous close), recursive float sanitization, and enforced `allow_nan=False` in `json.dump`.
  3. *Client Hardening*: Modified `index.html` (both on init and on manual refresh) to regex-sanitize unquoted `NaN` tokens before parsing, and refreshed default fallback to Sep 18.
  4. *Local Workspace APFS Recovery*: Replaced iCloud-evicted dataless `.git` objects and worktree files with clean local copies, fixing local git/command timeouts.

### Active Production Endpoint & 5-Signal Architecture
- **Permanent Cloud URL**: `https://tonytcfu.github.io/spcx-dashboard/`
- **5 Core Real Market Signals (Official September 18 Friday Close)**:
  1. Short Interest: 4.7% (Calculated: 173.62M Short / 3.70B Free Float)
  2. Utilization: 65.0% (Borrow Demand Stable)
  3. Borrow Rate: 1.0% (Floor Cost)
  4. Days to Cover: 0.52 Days (Calculated: 173.62M Short / 335.39M Quadruple-Witching Volume)
  5. Stock Price: $152.71 (NASDAQ Friday Official Close: -$2.10 / -1.36% vs Sep 17 Close $154.81)

### Key Milestones
- **2026-06-12**: SpaceX completed IPO on NASDAQ (`SPCX`) raising ~$85.7B at a ~$1.77T valuation.
- **2026-08-31**: SpaceX completed post-unlock rebound to $143.69 with short position shrinking to 184.39M shares (15.9% SI, 2.93d DTC).
- **2026-09-03**: SpaceX surged +6.42% to $149.74 with volume spiking to 120.96M shares, driving DTC down to 1.52 days.
- **2026-09-08**: SpaceX hit local high of $153.47 post-Labor Day.
- **2026-09-10**: SpaceX stabilized at $148.18 with 118.36M volume and DTC at 1.56 days.




