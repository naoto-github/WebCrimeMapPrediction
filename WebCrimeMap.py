from flask import Flask, render_template, request
import torch
from torchvision import transforms
import MapManager
from CrimeMapNetwork import CrimeMapNetwork

app = Flask(__name__)

# 地図情報の初期化
map_info = {
    "lat": 35.173486,
    "lng": 136.883455,
    "zoom": 17,
    "width": 256,
    "height": 256,
    "offset": 64
    }

# マーカー
map_markers = []

# ネットワーク
network_path = "./model/trained_network_cpu.pth"    
network = CrimeMapNetwork(3)
network.load_state_dict(torch.load(network_path))

# 対象領域を分類
def classify(map_png):

    # 出力サイズ
    output_size = 64

    # クロップ
    crop_size = 64
    
    # アスペクト比
    aspect_ratio = (1.0, 1.0)
    
    # 前処理
    tf = transforms.Compose([
        transforms.Resize(output_size),
        transforms.CenterCrop(crop_size),
        transforms.ToTensor()
    ])

    map_array = tf(map_png)
    map_array = torch.unsqueeze(map_array, 0)
    
    results = network(map_array)
    results = results.detach().numpy().copy()[0]

    classification = []

    for result in results:
        percentage = "{:.2%}".format(result)
        classification.append(percentage)
    
    return classification

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
    
    if request.method == "POST":

        # MapBoxの地図を生成
        fmap = MapManager.makeMap(map_info)

        # 対象領域をキャプチャ
        map_img, map_png = MapManager.capture(fmap, map_info)

        # 分類
        classification = classify(map_img)
        
        # マーカーの追加
        popup_text = f"<div style='width:260px; height:380px'>" \
                     f"<p><img src='data:image/png;base64,{map_png}'</p>" \
                     f"<p>緯度: {lat}<br>経度: {lng}</p>" \
                     f"<p>" \
                     f"車上ねらい: {classification[0]}<br>" \
                     f"自動販売機ねらい: {classification[1]}<br>" \
                     f"自動車盗: {classification[2]}<br>" \
                     f"</p>" \
                     f"</div>"
        
        map_marker = {
            "lat": lat,
            "lng": lng,
            "popupContent": popup_text
        }
        map_markers.append(map_marker)
        
        template = render_template("template.html", map_info=map_info, map_markers=map_markers)
        
        return template

if __name__ == "__main__":
    app.run(debug=True)
