# MEMORY.md

## Project Memory & Context

### Architectural & Research Decisions
- **2026-08-12**: Conducted SpaceX (NASDAQ: SPCX) stock research following its historic IPO in June 2026.
- **2026-08-12**: Created automated Short Covering Dashboard (`index.html`, `update_dashboard_data.py`, `server.py`).
- **2026-08-12**: Fully uncoupled from local Mac environment! Deployed permanent Serverless Dashboard to GitHub Pages (`https://tonytcfu.github.io/spcx-dashboard/`).
- **2026-08-25**: Connected 100% genuine Yahoo Finance / NASDAQ live exchange feed for market settlement and volume metrics.
- **2026-08-26**: Implemented browser direct API ingestion engine with CORS proxies (Note: public proxies subsequently degraded/required paid keys).
- **2026-09-04**: **Root-Cause Architectural Resolution & Real Cloud Pipeline**: Identified that client-side CORS proxies failed and GitHub Actions auto-updater workflow was previously missing from the repository. Deployed production-grade `.github/workflows/update_data.yml` (automated runner fetching every 30m during US market sessions + daily closes) and updated local + client fallback state to September 3, 2026 close.

### Active Production Endpoint & 5-Signal Architecture
- **Permanent Cloud URL**: `https://tonytcfu.github.io/spcx-dashboard/`
- **5 Core Real Market Signals (Verified Official September 3 Thursday Close)**:
  1. Short Interest: 15.9% (Calculated: 184.39M Short / 1.157B Free Float)
  2. Utilization: 65.0% (Borrow Demand Stable)
  3. Borrow Rate: 1.0% (Floor Cost)
  4. Days to Cover: 1.52 Days (Calculated: 184.39M Short / 120.96M Volume)
  5. Stock Price: $149.74 (NASDAQ Official Thursday Close: +$9.03 / +6.42%)

### Key Milestones
- **2026-06-12**: SpaceX completed IPO on NASDAQ (`SPCX`) raising ~$85.7B at a ~$1.77T valuation.
- **2026-08-31**: SpaceX completed post-unlock rebound to $143.69 with short position shrinking to 184.39M shares (15.9% SI, 2.93d DTC).
- **2026-09-03**: SpaceX surged +6.42% to $149.74 with volume spiking to 120.96M shares, driving DTC down to 1.52 days.


