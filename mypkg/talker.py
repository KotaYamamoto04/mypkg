import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from person_msgs.srv import Query   #通信の型（16ビットの符号付き整数）

def cb(request, response):
    if request.name == "山元広太":
        response.age = 19
    else:
        response.age = 255

    return response

rclpy.init()
node = Node("talker")            #ノード作成（nodeという「オブジェクト」を作成）
srv = node.create_service(Query, "query", cb)   #パブリッシャのオブジェクト作成
rclpy.spin(node)            #実行（無限ループ）
