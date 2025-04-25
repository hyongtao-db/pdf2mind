import asyncio
import os
from abc import ABC

from openai import OpenAI

from utils.log import logger

# BEGIN_SYSTEM_PROMPT_CN = """
# 你是一个擅长写作的总结专家，请在我给出全部资料后，
# 为我写出一份结构清晰、语言准确、格式为Markdown的总结报告。
# 要求markdown内容都是干货，不需要有思考过程，忽略作者信息和引用文献，
# 我会陆续把文本分段发送给你，在我正式请求摘要前，你不需要回复。
# """
# GET_MD_PROMPT_CN = "请根据上述所有的历史信息，帮我生成Markdown的总结报告，尽量保持上层标题简短"

BEGIN_SYSTEM_PROMPT = """
You are a summarization expert who is good at writing. After I provide all the materials,
write a summary report for me with a clear structure, accurate language, and in Markdown format.
The Markdown content is required to be substantial, without the need for the thinking process. Ignore the author information and cited literature.
I will send the text in segments one after another. You don't need to reply until I formally request the summary.
"""

GET_MD_PROMPT = "Please generate a summary report in Markdown format based on all the above historical information. Try to keep the upper-level headings short."

class BaseLLM(ABC):
    def __init__(self, model_name: str, language: str, max_level: int, temperature: float,
                 api_key_env: str, base_url: str):
        self.client = OpenAI(
            api_key=os.environ.get(api_key_env),
            base_url=base_url
        )
        self.model_name = model_name
        self.chat_history = [{"role": "system", "content": BEGIN_SYSTEM_PROMPT}]
        self.max_level = max_level
        self.language = language
        self.temperature = temperature

    async def process_chunk(self, idx, text):
        user_msg = f"The following is the {idx + 1}-th piece of material. Please make a summary, which is used to prepare for the final Markdown generation:\n{text}"

        self.chat_history.append({"role": "user", "content": user_msg})

        response = await asyncio.to_thread(
            self.client.chat.completions.create,
            model=self.model_name,
            messages=self.chat_history,
            temperature=self.temperature
        )

        assistant_reply = response.choices[0].message.content
        self.chat_history.pop()
        self.chat_history.append({"role": "assistant", "content": assistant_reply})

        logger.info(f"✅ The {idx+1}-th piece of material has been sent and the summary has been recorded.\n")
        await asyncio.sleep(1)

    def get_md_result(self):
        self.chat_history.append({"role": "user", "content": GET_MD_PROMPT + f"The generated Markdown document will be in {self.language} and have a maximum of {self.max_level} hierarchical levels."})

        final_response = self.client.chat.completions.create(
            model=self.model_name,
            messages=self.chat_history,
            temperature=self.temperature
        )

        return final_response.choices[0].message.content
