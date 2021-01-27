from flask import Flask, render_template, request
import MapManager

app = Flask(__name__)

# 地図情報の初期化
map_info = {
    "lat": 35.20013938746724,
    "lng": 136.89270771599905,
    "zoom": 18,
    "width": 256,
    "height": 256,
    "offset": 64
    }

# マーカー
map_markers = []

# キャプチャ範囲
capture_box = (map_info["offset"],
               map_info["offset"],
               map_info["width"] + map_info["offset"],
               map_info["height"] + map_info["offset"])

@app.route("/")
def index():

    template = render_template("template.html", map_info=map_info, map_markers=map_markers)
    
    return template

@app.route("/", methods=["POST"])
def post():

    method = request.method #POST
    lat = float(request.form.get("lat-input")) #緯度
    lng = float(request.form.get("lng-input")) #経度

    # 地図情報の更新
    map_info["lat"] = lat
    map_info["lng"] = lng

    # マーカーの追加
    popup_text = f"<div><p>緯度: {lat}<br>経度: {lng}</p></div>"
    map_marker = {
        "lat": lat,
        "lng": lng,
        "popupContent": popup_text
    }
    map_markers.append(map_marker)
    
    if request.method == "POST":

        template = render_template("template.html", map_info=map_info, map_markers=map_markers)
        
        return template

if __name__ == "__main__":
    app.run(debug=True)
