
import asyncio
from sphero_sdk import SpheroRvrAsync
from sphero_sdk import SerialAsyncDal


class SpheroToolbox:
    def __init__(self):
        self._event_loop = asyncio.get_event_loop()
        self._rvr = SpheroRvrAsync(dal=SerialAsyncDal(self._event_loop))

    async def wake_up_rvr(self):
        await self._rvr.awake()
        rgb_values = [0, 255, 0]
        await self._rvr.set_all_leds(0x3FFFFFFF, [color for i in range(10) for color in rgb_values])
        print("rvr ready!")
        await self._rvr.reset_yaw()




