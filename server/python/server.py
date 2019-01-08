import time
import os
import grpc
from concurrent import futures
from proto import helloworld_pb2
from proto import helloworld_pb2_grpc

SERVER_IP = '127.0.0.1'
SERVER_PORT = '9999'

class Servicer(helloworld_pb2_grpc.WorldServicer):
  def sayHello(self, request, context):
      print('hello from server', request, context)
      return helloworld_pb2.ResponseType(message='hello world')


def serve():
    print('Starting server...')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_WorldServicer_to_server(
        Servicer(), server
    )
    server.add_insecure_port(SERVER_IP + ':' + SERVER_PORT)
    server.start()
    print('Listen :' + SERVER_PORT)
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        print('Stop server')
        server.stop(0)


if __name__ == '__main__':
    serve()
