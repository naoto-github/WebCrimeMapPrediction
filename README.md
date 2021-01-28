# 犯罪予測マップ（WebCrimeMapPrediction）

愛知県警察が公開している[犯罪オープンデータ](https://www.pref.aichi.jp/police/anzen/toukei/opendata/seian-s/crimeopendata.html)と[オープンストリートマップ（MapBox）](https://www.openstreetmap.org/)を利用した犯罪予測のウェブアプリです．アーバンデータチャレンジ2020の応募作品として制作しました．

- 作品タイトル：犯罪オープンデータとオープンストリートマップを利用した犯罪予測マップ
- 製作者：向 直人（[椙山女学園大学](https://www.sugiyama-u.ac.jp/) / Code for Nagoya / UDC愛知ブロック）
- 作品のテーマ：防犯・防災
- 作品のタイプ：アプリケーション
- 応募部門：ビジネス・プロフェッショナル

## 作品概要

本作品は全国で発生する犯罪を予防することを目的としています．犯罪者を減らすのではなく，犯罪が起こりにくい街を設計するためのウェブアプリ「犯罪予測マップ」を提供します．「犯罪予測マップ」は地域の「道路形状」や「建物配置」などの特徴から，起こりやすい犯罪種別を予測することが可能となっており，犯罪種別ごとのきめ細かな防犯対策の実現を支援します．

[令和2年警察白書 統計資料](https://www.npa.go.jp/hakusyo/r02/data.html)によると，愛知県は刑法犯の認知件数が49,956件と全国でワースト4位となっています（交通事故死者数が全国的に多いことでも有名です）．この数値を減らすことで，治安の向上だけでなく，地域の魅力を高めることに繋がり，地域経済の発展にも寄与すると考えています．

|県|認知件数|検挙件数|検挙人員|
|:----|:----|:----|:----|
|東京|104664|34309|24902|
|大阪|84672|22074|15561|
|埼玉|55497|18750|11297|
|愛知|49956|17395|13235|
|千葉|41793|12883|7726|

犯罪の予測には **畳み込みニューラルネットワーク（Convolutional Neural Network: CNN）** を採用しています．CNNは画像認識が得意な深層学習の一つです．CNNの学習には愛知県警察が公開している[犯罪オープンデータ](https://www.pref.aichi.jp/police/anzen/toukei/opendata/seian-s/crimeopendata.html)を利用しました．この犯罪オープンデータには，



## デモ

### 作品の実用度

### 作品の完成度

### 作品の挑戦度

### ビジネス・プロフェッショナル部門でのPR

## 実行方法

[Python v3.x](https://www.python.jp/)で開発しました．アプリの実行には下記のライブラリが必要となりますので，pipコマンドなどを利用して導入してください．

- [Folium](https://python-visualization.github.io/folium/) MapBoxで生成した地図画像をダウンロード
- [PyTorch](https://pytorch.org/) 深層学習のフレームワーク
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) ウェブアプリケーションのフレームワーク

レポジトリをダウンロード（またはクローン）したら，下記のコマンドを実行してください．

```
$ python WebCrimeMap.py
```

ウェブアプリが起動したら，ブラウザで http://127.0.0.1:5000/ にアクセスしてください．

### 重要
MapBox APIにアクセスするための **API_KEY** は公開することが出来ないため，GitHubレポジトリには含まれていません．UDCの審査に際しては，個別に情報を含めたファイル（secret.json）を提供しますので，開発者の向までお知らせください．アクセスが基準を超えると料金が発生してしまうため，ご利用の際はご注意頂けたらと思います．

## データセット

愛知県の[犯罪オープンデータ](https://www.pref.aichi.jp/police/anzen/toukei/opendata/seian-s/crimeopendata.html)を基に独自に生成したCNN用のデータセットです．データセットには，HTMLファイル，地図画像（PNG画像），犯罪データ（JSONファイル）が含まれています．

### [aichi-crime-map-700.zip](https://drive.google.com/file/d/1p7yFhjo7hpNHDjhtf-tFxX_jV9s76XZc/view?usp=sharing)

テスト用のデータセットです．サンプル数はN=700です．

- 部品ねらい 100
- ひったくり 100
- オートバイ盗 100
- 車上ねらい 100
- 自動販売機ねらい 100
- 自動車盗 100
- 自転車盗 100

### [aichi-crime-map-6235.zip](https://drive.google.com/file/d/1p2Tk37pzn6-whtuKfJeNPx8Let3EhgJZ/view?usp=sharing)

犯罪予測マップの学習に用いたデータセットです．サンプル数はN=6235です．

- 部品ねらい 1000
- ひったくり 235
- オートバイ盗 1000
- 車上ねらい 1000
- 自動販売機ねらい 1000
- 自動車盗 1000
- 自転車盗 1000
