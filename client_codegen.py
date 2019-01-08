from grpc.tools import protoc

protoc.main(
    (
        '',
        '-I.',
        '--python_out=./client/python',
        '--grpc_python_out=./client/python',
        './proto/helloworld.proto',
    )
)

