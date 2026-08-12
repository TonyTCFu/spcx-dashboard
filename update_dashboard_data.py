import json
import os
import datetime
import time

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "metrics.json")

def generate_daily_metrics(ticker="SPCX"):
    """
    Simulates fetching fresh daily metrics from live data providers
    and updates data/metrics.json cache with explicit versioning.
    """
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    
    now_dt = datetime.datetime.now()
    now_str = now_dt.strftime("%Y-%m-%d %H:%M:%S")
    today_str = datetime.date.today().isoformat()
    version_tag = f"v_{int(time.time())}"
    
    # Load existing history if available
    history = []
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                existing = json.load(f)
                history = existing.get("historical_data", [])
        except Exception:
            history = []

    current_si = 30.75
    current_util = 97.6
    current_rate = 3.08
    current_price = 138.70

    if history and history[-1].get("date") == today_str:
        history[-1] = {
            "date": today_str,
            "short_interest": current_si,
            "utilization": current_util,
            "borrow_rate": current_rate,
            "price": current_price
        }
    else:
        history.append({
            "date": today_str,
            "short_interest": current_si,
            "utilization": current_util,
            "borrow_rate": current_rate,
            "price": current_price
        })

    payload = {
        "cache_version": version_tag,
        "last_updated": now_str,
        "ticker": ticker,
        "company_name": "SpaceX Exploration Technologies Corp.",
        "current_metrics": {
            "short_interest_pct": current_si,
            "short_interest_change": -5.65,
            "utilization_pct": current_util,
            "utilization_change": -2.2,
            "borrow_rate_pct": current_rate,
            "borrow_rate_change": -6.92,
            "stock_price": current_price,
            "stock_price_change": 5.70
        },
        "status_summary": {
            "primary_status": "有序空头回补 (Orderly Short Covering)",
            "squeeze_risk_level": "低风险 (Low Risk)",
            "description": "Short Interest与Borrow Rate同步显著回落，配合股价缓步上行，表明空头资金正在顺畅主动止盈/止损平仓，市场未出现无券可借导致的强逼空行情。"
        },
        "historical_data": history
    }

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    print(f"[{now_str}] Dashboard metrics updated -> Cache Version: {version_tag}")

if __name__ == "__main__":
    generate_daily_metrics()
