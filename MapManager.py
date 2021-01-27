import json
import os
import folium
import base64
from PIL import Image
import io

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

tiles = secret["mapbox_url"] + "?access_token=" + secret["mapbox_api_key"]
attr = secret["mapbox_attr"]

# MapBoxの地図を生成
def makeMap(map_info):
    
    fmap = folium.Map(
        tiles = tiles,
        location = (map_info["lat"], map_info["lng"]),
        zoom_start = map_info["zoom"],
        width = map_info["width"] + 2 * map_info["offset"],
        height = map_info["height"] + 2 * map_info["offset"],
        attr = attr, 
        control_scale = False,
        zoom_control = False,
        no_touch = True
    )

    return fmap

# 対象領域をキャプチャ
def capture(fmap, map_info):

    # キャプチャ範囲
    crop_box = (map_info["offset"],
                map_info["offset"],
                map_info["width"] + map_info["offset"],
                map_info["height"] + map_info["offset"])    
    
    # PNG画像のバイナリデータ
    img_data = fmap._to_png()
    map_img = Image.open(io.BytesIO(img_data))
    map_img = map_img.crop(crop_box).convert("RGB")
    map_img.save("map.png")

    # PNG画像のテキストデータ（base64）
    imgByteArr = io.BytesIO()
    map_img.save(imgByteArr, format="PNG")
    map_png = base64.b64encode(imgByteArr.getvalue()).decode()    
    
    return map_img, map_png
