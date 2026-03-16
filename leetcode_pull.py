import requests
import json
import os

# paste your cookie here
COOKIE = "PASTE_YOUR_LEETCODE_SESSION_COOKIE"

headers = {
    "cookie": f"LEETCODE_SESSION={COOKIE}",
    "referer": "https://leetcode.com",
    "user-agent": "Mozilla/5.0"
}

url = "https://leetcode.com/api/submissions/"

os.makedirs("leetcode_solutions", exist_ok=True)

page = 0
while True:
    r = requests.get(url + f"?offset={page*20}&limit=20", headers=headers)
    data = r.json()

    submissions = data.get("submissions_dump", [])
    if not submissions:
        break

    for sub in submissions:
        if sub["status_display"] == "Accepted":
            title = sub["title_slug"]
            code = sub["code"]

            filename = f"leetcode_solutions/{title}.txt"
            with open(filename, "w", encoding="utf8") as f:
                f.write(code)

            print("Saved:", title)

    page += 1