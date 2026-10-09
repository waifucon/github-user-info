import urllib.request
import json
from datetime import datetime, timezone

username = input("Enter a GitHub username: ").strip()
url = f"https://api.github.com/users/{username}"

try:
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())

        # Format registration date
        raw_date = data.get('created_at')
        formatted_date_time = raw_date
        if raw_date:
            dt_utc = datetime.strptime(raw_date, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            dt_local = dt_utc.astimezone()
            formatted_date_time = dt_local.strftime("%B %d, %Y at %H:%M:%S %Z")

        print(f"\nPublic Repos: {data.get('public_repos')}")
        print(f"Registration Date: {formatted_date_time}")
except Exception as e:
    print(f"\nAPI call failed: {e}")
