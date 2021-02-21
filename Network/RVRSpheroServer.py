from concurrent import futures
from grpclib.server import Server
from grpclib.utils import graceful_exit
from gRPCPythonServices import RVRSpheroServices_grpc
from gRPCPythonServices import RVRSpheroServices_pb2


class RVRSpheroServer(RVRSpheroServices_grpc.RVRSpheroServiceBase):

    def __init__(self):
        super.__init__()

        self._sensor_commands = {
            0: self.update_accelerometer,
            1: self.update_ambient_light,
            2: self.update_color_sensor,
            3: self.core_time,
            4: self.update_gyroscope,
            5: self.update_imu,
            6: self.update_locator,
            7: self.update_quaternion,
            8: self.update_speed,
            9: self.update_velocity
        }

    async def UpdateSensorData(self, stream):
        request = stream.recv_message()
        assert request is not None
        message = RVRSpheroServices_pb2.SensorData__pb2.SensorData()
        for i in range(request.sensorFlagLength):
            if request.sensorFlags[i]:
                update_cmd = self._sensor_commands.get(i, lambda: None)
                if update_cmd:
                    message = await update_cmd(message)
        await stream.send_message(message)

    async def update_accelerometer(self, message) -> RVRSpheroServices_pb2.SensorData__pb2.SensorData:
        pass

    async def update_ambient_light(self, message) -> RVRSpheroServices_pb2.SensorData__pb2.SensorData:
        pass

    async def update_color_sensor(self, message) -> RVRSpheroServices_pb2.SensorData__pb2.SensorData:
        pass

    async def core_time(self, message) -> RVRSpheroServices_pb2.SensorData__pb2.SensorData:
        pass

    async def update_gyroscope(self, message) -> RVRSpheroServices_pb2.SensorData__pb2.SensorData:
        pass

    async def update_imu(self, message) -> RVRSpheroServices_pb2.SensorData__pb2.SensorData:
        pass

    async def update_locator(self, message) -> RVRSpheroServices_pb2.SensorData__pb2.SensorData:
        pass

    async def update_quaternion(self, message) -> RVRSpheroServices_pb2.SensorData__pb2.SensorData:
        pass

    async def update_speed(self, message) -> RVRSpheroServices_pb2.SensorData__pb2.SensorData:
        pass

    async def update_velocity(self, message) -> RVRSpheroServices_pb2.SensorData__pb2.SensorData:
        pass


async def serve():
    server = Server([RVRSpheroServer()])
    with graceful_exit([server]):
        await server.start('127.0.0.1', 8008)
        print("AI Server started.")
        await server.wait_closed()

if __name__ == '__main__':
    await serve()
