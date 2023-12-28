import rclpy                     #ROS 2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from person_msgs.srv import Query   #通信の型（16ビットの符号付き整数）

def main():
    rclpy.init()
    node = Node("listener")            #ノード作成（nodeという「オブジェクト」を作成）
    client = node.create_client(Query, 'query')   #パブリッシャのオブジェクト作成
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('待機中')

    req = Query.Request()
    req.name = "山元広太"
    future = client.call_async(req)

    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('呼び出し失敗')
            else:
                node.get_logger().info("age: {}".format(response.age))

            break

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
