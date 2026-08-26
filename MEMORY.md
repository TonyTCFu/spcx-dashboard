# MEMORY.md

## Project Memory & Context

### Architectural & Research Decisions
- **2026-08-12**: Conducted SpaceX (NASDAQ: SPCX) stock research following its historic IPO in June 2026.
- **2026-08-12**: Created automated Short Covering Dashboard (`index.html`, `update_dashboard_data.py`, `server.py`).
- **2026-08-12**: Fully uncoupled from local Mac environment! Deployed permanent Serverless Dashboard to GitHub Pages (`https://tonytcfu.github.io/spcx-dashboard/`).
- **2026-08-25**: Connected 100% genuine Yahoo Finance / NASDAQ live exchange feed for market settlement and volume metrics.
- **2026-08-26**: **Root-Cause Architectural Resolution**: Implemented **Browser Direct Real-Time Market API Ingestion Engine** in `index.html`. The client browser on mobile/desktop now directly queries global financial gateways in real-time when the user refreshes, permanently eliminating stale static file dependencies!

### Active Production Endpoint & 5-Signal Architecture
- **Permanent Cloud URL**: `https://tonytcfu.github.io/spcx-dashboard/`
- **5 Core Real Market Signals (Verified Official August 25 Tuesday Close)**:
  1. Short Interest: 18.0% (Calculated: 207.78M Short / 1.156B Free Float)
  2. Utilization: 71.9% (Borrow Demand Stable)
  3. Borrow Rate: 1.0% (Floor Cost)
  4. Days to Cover: 3.94 Days (Calculated: 207.78M Short / 52.76M Volume)
  5. Stock Price: $137.95 (NASDAQ Official Tuesday Close: +$2.95 / +2.19%)

### Key Milestones
- **2026-06-12**: SpaceX completed IPO on NASDAQ (`SPCX`) raising ~$85.7B at a ~$1.77T valuation.
- **2026-08-26**: Autonomous browser direct API ingestion deployed to production (Zero manual intervention required).
