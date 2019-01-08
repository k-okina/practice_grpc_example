import grpc
from proto import helloworld_pb2
from proto import helloworld_pb2_grpc

SERVER_IP = '127.0.0.1'
SERVER_PORT = '9999'


def run():
  print('start run')
  channel = grpc.insecure_channel(SERVER_IP + ':' + SERVER_PORT)
  stub = helloworld_pb2_grpc.WorldStub(channel)
  stub.sayHello(helloworld_pb2.RequestType())
  print('sayHello')


if __name__ == '__main__':
  run()
