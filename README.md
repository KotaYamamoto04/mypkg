# mypkg
これは、千葉工業大学のロボットシステム学の講義内で扱ったROS2のリポジトリです。

[![test](https://github.com/KotaYamamoto04/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/KotaYamamoto04/mypkg/actions/workflows/test.yml)

## 各種ノードの説明
* talker.py
パブリッシャを持つノード。数字をカウントして、トピック(/countup)を通じて送信する。
* listener.py
サブスクライバを持つノード。トピック(/countup)からメッセージをもらって表示する。
* talk_listen.launch.py
talker.pyとlistener.pyの２つのノードを一度に立ち上げる。

## 実行方法とその結果
* talker.pyとlistener.pyの場合
２つの端末を立ち上げて実行する。

１．１つ目の端末では、
```
ros2 run mypkg talker
```
を実行する。
２．２つ目の端末では、
```
ros2 run mypkg listener
```
と実行する。
３．
４．

## 必要なソフトウェア
* Python

## テスト環境
* Ubuntu 22.04.2 LTS

## 著作権・ライセンス
 * このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます． * このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
      * [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
 * © 2023 Kota Yamamoto
