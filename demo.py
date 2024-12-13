import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是小说助手"},
        {"role": "user", "content": "以“世事如白云苍狗，愿你我都能成为生活的高手”为文章结尾，\
         生成一篇浪子纵横江湖起起落落最终和爱人执子之手与子偕老相忘江湖的小说1000字。古龙风格。"},
    ],
    temperature=2,
    max_tokens=4000,
)

print(response.choices[0].message.content)