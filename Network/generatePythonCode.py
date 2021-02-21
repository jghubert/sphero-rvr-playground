# Generate the python code from the protobuf files.

from grpc_tools import protoc

protoc.main((
    '',
    '-IMessages',
    '-IServices',
    '--python_out=gRPCPythonServices',
    '--grpc_python_out=gRPCPythonServices',
    'Services/RVRSpheroServices.proto',
    # 'Messages/SpheroRVRDataTypes.proto',
    'Messages/SensorData.proto'
))


