#Network Interface

## gRPC Configuration
### Installation
```
python -m pip install grpcio
python -m pip install grpcio-tools
```

### Generate the Python files
To compile the proto files, use the command below from the Network directory:
```
python -m grpc_tools.protoc -IServices -IMessages  --python_out=. --grpc_python_out=. Services/RVRSpheroServices.proto
```

