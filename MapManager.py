import json
import os

SECRET_FILE = "secret.json"

if os.path.exists(SECRET_FILE):
    f = open(SECRET_FILE)
    secret = json.load(f)
else:
    # Mapboxのタイル情報を指定してください
    secret = {
        "mapbox_url", "xxxxx",
        "mapbox_api_key", "xxxxx",
        "mapbox_attr", "xxxxx"
    }

tiles = secret["mapbox_url"] + "?access_token=" + secret["mapbox_attr"]


