#!/bin/bash
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

LOG_FILE="$DIR/auto_sync.log"
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting automated SPCX market sync..." >> "$LOG_FILE"

/usr/bin/python3 "$DIR/update_dashboard_data.py" >> "$LOG_FILE" 2>&1

if [[ -n $(git status -s data/metrics.json) ]]; then
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] Market data changed, committing and pushing..." >> "$LOG_FILE"
  git add data/metrics.json
  git commit -m "chore(auto): update SPCX market metrics [skip ci]" >> "$LOG_FILE" 2>&1
  git push origin master >> "$LOG_FILE" 2>&1
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] Push completed successfully." >> "$LOG_FILE"
else
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] No changes detected in market data." >> "$LOG_FILE"
fi
