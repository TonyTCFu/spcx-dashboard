# MEMORY.md

## Project Memory & Context

### Architectural & Research Decisions
- **2026-08-12**: Conducted SpaceX (NASDAQ: SPCX) stock research following its historic IPO in June 2026.
- **2026-08-12**: Created automated Short Covering Dashboard (`index.html`, `update_dashboard_data.py`, `server.py`).
- **2026-08-12**: Fully uncoupled from local Mac environment! Deployed permanent Serverless Dashboard to GitHub Pages (`https://tonytcfu.github.io/spcx-dashboard/`).
- **2026-08-22**: Enforced zero-cache architecture + top benchmark notification bar.
- **2026-08-25**: Completely removed hardcoded dates from frontend template and enabled 100% dynamic data binding. Added GitHub Actions workflow (`.github/workflows/update_data.yml`) for scheduled and on-demand automated market close data updates.
- **2026-08-25**: Advanced market dataset to Monday, August 24, 2026 official close ($139.45, +1.81%, DTC 1.07d, SI 20.5%).

### Active Production Endpoint & 5-Signal Architecture
- **Permanent Cloud URL**: `https://tonytcfu.github.io/spcx-dashboard/`
- **5 Core Real Market Signals (Verified Official August 24 Monday Close)**:
  1. Short Interest: 20.5% (Calculated: 174M Short / 850M Free Float)
  2. Utilization: 71.5% (Borrow Demand Stable)
  3. Borrow Rate: 1.0% (Floor Cost)
  4. Days to Cover: 1.07 Days (Calculated: 174M Short / 162.5M Volume)
  5. Stock Price: $139.45 (NASDAQ Official Monday Close: +$2.48 / +1.81%)

### Key Milestones
- **2026-06-12**: SpaceX completed IPO on NASDAQ (`SPCX`) raising ~$85.7B at a ~$1.77T valuation.
- **2026-08-22**: Zero-cache production build verified live on GitHub Pages.
- **2026-08-25**: Automated cloud data pipeline established + dynamic data binding deployed.
