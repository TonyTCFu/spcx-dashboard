# MEMORY.md

## Project Memory & Context

### Architectural & Research Decisions
- **2026-08-12**: Conducted SpaceX (NASDAQ: SPCX) stock research following its historic IPO in June 2026.
- **2026-08-12**: Created automated Short Covering Dashboard (`index.html`, `update_dashboard_data.py`, `server.py`).
- **2026-08-12**: Fully uncoupled from local Mac environment! Deployed permanent Serverless Dashboard to GitHub Pages (`https://tonytcfu.github.io/spcx-dashboard/`).
- **2026-08-25**: Connected 100% genuine Yahoo Finance / NASDAQ live exchange feed for market settlement and volume metrics.
- **2026-08-26**: Implemented browser direct API ingestion engine with CORS proxies (Note: public proxies subsequently degraded/required paid keys).
- **2026-09-04/05**: **Price Change Benchmark Decoupling & Alignment**: Discovered that Dashboard previously labeled previous day's close (+6.42% over Sep 2) with the current day's live banner, causing severe confusion with broker real-time apps (which measure today's intraday price against yesterday's close $149.74, i.e. -$0.98 / -0.65%). Decoupled clock time from data session validation, explicitly displayed the previous close reference price in the change badge, and updated live production data to Sep 4 intraday ($148.76, -0.65%).

### Active Production Endpoint & 5-Signal Architecture
- **Permanent Cloud URL**: `https://tonytcfu.github.io/spcx-dashboard/`
- **5 Core Real Market Signals (Live Intraday September 4 Friday)**:
  1. Short Interest: 15.9% (Calculated: 184.39M Short / 1.157B Free Float)
  2. Utilization: 65.0% (Borrow Demand Stable)
  3. Borrow Rate: 1.0% (Floor Cost)
  4. Days to Cover: 6.17 Days (Calculated: 184.39M Short / 29.91M Volume)
  5. Stock Price: $148.76 (NASDAQ Friday Intraday: -$0.98 / -0.65% vs Sep 3 Close $149.74)

### Key Milestones
- **2026-06-12**: SpaceX completed IPO on NASDAQ (`SPCX`) raising ~$85.7B at a ~$1.77T valuation.
- **2026-08-31**: SpaceX completed post-unlock rebound to $143.69 with short position shrinking to 184.39M shares (15.9% SI, 2.93d DTC).
- **2026-09-03**: SpaceX surged +6.42% to $149.74 with volume spiking to 120.96M shares, driving DTC down to 1.52 days.
- **2026-09-04**: SpaceX trading in regular session around $148.76 (-0.65% vs $149.74 close).



