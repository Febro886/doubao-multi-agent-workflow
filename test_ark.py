# test_ark.py —— 第一次豆包调用测试
import os
from dotenv import load_dotenv
from openai import OpenAI

# 读取同目录 .env 里的 ARK_API_KEY（Key 只待在本地，不写进代码）
load_dotenv()

# 创建客户端：地址指向火山方舟的 OpenAI 兼容接口
client = OpenAI(
    api_key=os.environ["ARK_API_KEY"],
    base_url="https://ark.cn-beijing.volces.com/api/v3",
)

# 发起一次对话请求：model 填你开通的 Seed-2.1-pro 的模型 ID
resp = client.chat.completions.create(
    model="doubao-seed-2-1-pro-260915",
    messages=[
        {"role": "user", "content": "用一句话介绍你自己，并说明你擅长写代码和多智能体协作。"}
    ],
)

# 打印模型回复
print(resp.choices[0].message.content)
print("OK: 豆包调用成功")