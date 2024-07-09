from django.http import StreamingHttpResponse
import openai
from django.shortcuts import render
import json

# 设置OpenAI的API密钥
openai.api_key = ''


def chat_home(request):
    # Ensure the template path is correct
    ai_error = request.session.pop('ai_error', None)
    return render(request, 'myapp/chat.html', {'ai_error': ai_error})

def chat_with_gpt(request):
    # Retrieve user input from GET request
    user_input = request.GET.get('prompt', '你是谁呀？')

    # Launch the ChatCompletion request with streaming response
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[{'role': 'user', 'content': user_input}],
        temperature=0,
        stream=True
    )

    # Define a generator function to handle streaming data
    def stream():
        for event in response:
            data = event['choices'][0]['delta'].get('content', '')  # 获取具体的内容
            yield f"data: {json.dumps(data)}\n\n"  # 遵循 SSE 格式

    # Generate streaming response
    r = StreamingHttpResponse(streaming_content=stream(), content_type='text/event-stream; charset=utf-8')
    r['Cache-Control'] = 'no-cache'
    return r


