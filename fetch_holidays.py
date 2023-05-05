import json
import os
import requests
from datetime import datetime

current_year = datetime.now().year
end_year = current_year + 10
base_url = "https://feiertage-api.de/api/"

# Remove existing JSON files in the holidays directory
holidays_dir = "holidays"
if os.path.exists(holidays_dir):
    for file in os.listdir(holidays_dir):
        if file.endswith(".json"):
            os.remove(os.path.join(holidays_dir, file))

os.makedirs(holidays_dir, exist_ok=True)

for year in range(2010, end_year + 1):
    response = requests.get(f"{base_url}?jahr={year}")
    if response.status_code == 200:
        holidays = response.json()
        with open(f"holidays/holidays_{year}.json", "w") as f:
            json.dump(holidays, f, ensure_ascii=False, indent=4)
    else:
        print(f"Error fetching holidays for the year {year}")

