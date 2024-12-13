import os, re
from openai import OpenAI

def get_prompt(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
def get_story(prompt):
    client = OpenAI(
        api_key=os.getenv('ZHIPUAI_API_KEY'), 
        base_url="https://open.bigmodel.cn/api/paas/v4/")

    response = client.chat.completions.create(
        model="glm-4-plus",
        messages=[
            {"role": "system", "content": "你是小说助手"},
            {"role": "user", "content": prompt},
        ],
        top_p=0.7,
        temperature=0.9,
        # max_tokens=4096,
    )

    return response.choices[0].message.content

def compact_story(story):
    compacted_story = re.sub(r'\n\n+', '\n', story)
    return compacted_story

def make_sory(prompt_path, output_path):
    prompt = get_prompt(prompt_path)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(compact_story(get_story(prompt)))
    

if __name__ == '__main__':
    make_sory('../prompts/古龙v2.txt', '../stories/江湖_11.txt')