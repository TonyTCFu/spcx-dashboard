# MEMORY.md

## Project Memory & Context

### Architectural & Research Decisions
- **2026-08-12**: Conducted SpaceX (NASDAQ: SPCX) stock research following its historic IPO in June 2026.
- **2026-08-12**: Created automated Short Covering Dashboard (`index.html`, `update_dashboard_data.py`, `server.py`).
- **2026-08-12**: Cleaned up redundant background tasks and configured daily Cron schedule (`0 5 * * *`) for 1x/day dataset cache updates.

### Active Background Task Architecture
- **Daemon 1 (Web Server)**: `python3 server.py` (Local HTTP port 8080).
- **Daemon 2 (Public Tunnel)**: `./cloudflared tunnel --protocol http2 --url http://localhost:8080` (`https://ser-repeat-mathematics-prime.trycloudflare.com`).
- **Daily Cron (Data Update)**: `0 5 * * *` (Runs `update_dashboard_data.py` once per day, zero unnecessary overhead).

### Key Milestones
- **2026-06-12**: SpaceX completed IPO on NASDAQ (`SPCX`) raising ~$85.7B at a ~$1.77T valuation.
- **2026-08-12**: Tasks streamlined to 2 background daemons + 1 daily Cron schedule.
