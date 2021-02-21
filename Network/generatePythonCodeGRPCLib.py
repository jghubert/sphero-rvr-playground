# Generate the python code from the protobuf files.

from grpc_tools import protoc

protoc.main((
    '',
    '-IMessages',
    '-IServices',
    '--python_out=gRPCPythonServices',
    '--grpclib_python_out=gRPCPythonServices',
    'Services/RVRSpheroServices.proto',
    'Messages/SensorData.proto'
))


