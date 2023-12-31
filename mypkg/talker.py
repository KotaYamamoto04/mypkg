#SPDX-FileCopyrightText: 2023 Kota Yamamoto s22c1133uz@s.chibakoudai.jp
#SPDX-License-Identifier:BSD-3-Clause

import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import Int16   #通信の型（16ビットの符号付き整数）

class Talker():          #ヘッダの下にTalkerというクラスを作成
    def __init__(self, nh):  # オブジェクトを作ると呼ばれる関数
        self.pub = node.create_publisher(Int16, "countup", 10)
        self.n = 0
        nh.create_timer(0.5, self.cb)
         # ↑ selfはオブジェクトのこと
         # ↑ オブジェクトにひとつパブリッシャと変数をもたせる。
    def cb(self):              
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.n += 1

rclpy.init()
node = Node("talker")
talker = Talker(node)
rclpy.spin(node)
