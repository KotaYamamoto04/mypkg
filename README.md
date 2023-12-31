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

３．実行結果は以下のようになる。
```
[INFO] [1703987387.783020334] [listener]: Listen: 0
[INFO] [1703987388.262370278] [listener]: Listen: 1
[INFO] [1703987388.762144204] [listener]: Listen: 2
[INFO] [1703987389.261894811] [listener]: Listen: 3
[INFO] [1703987389.761800407] [listener]: Listen: 4
[INFO] [1703987390.262189289] [listener]: Listen: 5
[INFO] [1703987390.762660806] [listener]: Listen: 6
[INFO] [1703987391.262237223] [listener]: Listen: 7
[INFO] [1703987391.761665612] [listener]: Listen: 8
[INFO] [1703987392.261902644] [listener]: Listen: 9
[INFO] [1703987392.762472755] [listener]: Listen: 10
[INFO] [1703987393.262014145] [listener]: Listen: 11
[INFO] [1703987393.762466245] [listener]: Listen: 12
```

* talker_listen.launch.pyの場合

端末は１つで実行可能。
```
ros2 launch mypkg talk_listen.launch.py
```

実行結果は以下のようになる。
```
[INFO] [launch]: All log files can be found below /home/yamamoto/.ros/log/2023-12-31-10-55-24-190587-yamamoto-kota-2799
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [2800]
[INFO] [listener-2]: process started with pid [2802]
[listener-2] [INFO] [1703987724.962738662] [listener]: Listen: 0
[listener-2] [INFO] [1703987725.453082326] [listener]: Listen: 1
[listener-2] [INFO] [1703987725.953043586] [listener]: Listen: 2
[listener-2] [INFO] [1703987726.452587344] [listener]: Listen: 3
[listener-2] [INFO] [1703987726.952958876] [listener]: Listen: 4
[listener-2] [INFO] [1703987727.452789346] [listener]: Listen: 5
[listener-2] [INFO] [1703987727.953141201] [listener]: Listen: 6
[listener-2] [INFO] [1703987728.453306831] [listener]: Listen: 7
[listener-2] [INFO] [1703987728.953185959] [listener]: Listen: 8
[listener-2] [INFO] [1703987729.451793924] [listener]: Listen: 9
[listener-2] [INFO] [1703987729.951286773] [listener]: Listen: 10
[listener-2] [INFO] [1703987730.451949791] [listener]: Listen: 11
[listener-2] [INFO] [1703987730.952575574] [listener]: Listen: 12
```


## 必要なソフトウェア
* Python

## テスト環境
* Ubuntu 22.04.2 LTS

## 著作権・ライセンス
 * このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます． * このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
      * [ryuichiueda/my_slides/robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
 * © 2023 Kota Yamamoto
