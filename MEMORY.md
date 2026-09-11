# MEMORY.md

## Project Memory & Context

### Architectural & Research Decisions
- **2026-08-12**: Conducted SpaceX (NASDAQ: SPCX) stock research following its historic IPO in June 2026.
- **2026-08-12**: Created automated Short Covering Dashboard (`index.html`, `update_dashboard_data.py`, `server.py`).
- **2026-08-12**: Fully uncoupled from local Mac environment! Deployed permanent Serverless Dashboard to GitHub Pages (`https://tonytcfu.github.io/spcx-dashboard/`).
- **2026-08-25**: Connected 100% genuine Yahoo Finance / NASDAQ live exchange feed for market settlement and volume metrics.
- **2026-08-26**: Implemented browser direct API ingestion engine with CORS proxies (Note: public proxies subsequently degraded/required paid keys).
- **2026-09-04/05**: **Price Change Benchmark Decoupling & Alignment**: Discovered that Dashboard previously labeled previous day's close (+6.42% over Sep 2) with the current day's live banner, causing severe confusion with broker real-time apps. Decoupled clock time from data session validation, explicitly displayed the previous close reference price in the change badge.
- **2026-09-11**: **Auto-Update Root-Cause Resolution**: Diagnosed that GitHub Actions workflow was rejected during terminal git push because the user's Personal Access Token (PAT) lacks `workflow` scope. Removed local LaunchAgent per user instruction, and assisted user with direct browser creation of GitHub Actions workflow for 100% cloud-native automated updating.

### Active Production Endpoint & 5-Signal Architecture
- **Permanent Cloud URL**: `https://tonytcfu.github.io/spcx-dashboard/`
- **5 Core Real Market Signals (Official September 10 Thursday Close)**:
  1. Short Interest: 6.2% (Calculated: 184.39M Short / 2.97B Free Float)
  2. Utilization: 65.0% (Borrow Demand Stable)
  3. Borrow Rate: 1.0% (Floor Cost)
  4. Days to Cover: 1.56 Days (Calculated: 184.39M Short / 118.36M Volume)
  5. Stock Price: $148.18 (NASDAQ Thursday Official Close: +$0.63 / +0.43% vs Sep 9 Close $147.55)

### Key Milestones
- **2026-06-12**: SpaceX completed IPO on NASDAQ (`SPCX`) raising ~$85.7B at a ~$1.77T valuation.
- **2026-08-31**: SpaceX completed post-unlock rebound to $143.69 with short position shrinking to 184.39M shares (15.9% SI, 2.93d DTC).
- **2026-09-03**: SpaceX surged +6.42% to $149.74 with volume spiking to 120.96M shares, driving DTC down to 1.52 days.
- **2026-09-08**: SpaceX hit local high of $153.47 post-Labor Day.
- **2026-09-10**: SpaceX stabilized at $148.18 with 118.36M volume and DTC at 1.56 days.




