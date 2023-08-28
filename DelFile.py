import sys
import asyncio
sys.path.append("..")
from nfysd import sdn

async def test():
    await sdn("签到错误","获取登录状态失败！","https://www.baidu.com")

asyncio.run(test())