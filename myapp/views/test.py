import os
import django
from django.conf import settings
from django.test import AsyncClient
import asyncio

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myxuexi.settings')
django.setup()


async def test_chat_stream():
    client = AsyncClient()
    response = await client.post('/index/ask_chatgpt/', {'message': 'Hello, world!'})
    print('Status Code:', response.status_code)

    # 如果状态码表明重定向，手动处理重定向
    if response.status_code in [301, 302, 303, 307, 308]:
        redirect_url = response.headers['Location']
        print('Redirected URL:', redirect_url)
        # 你可能需要根据实际情况决定是否发起新的请求
        # response = await client.get(redirect_url)
        # print('Response Content After Redirect:', response.content)
    else:
        print('Response Content:', response.content)


if __name__ == '__main__':
    asyncio.run(test_chat_stream())
