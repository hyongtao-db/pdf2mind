import time
import os

from llm.base_llm import BaseLLM, BEGIN_SYSTEM_PROMPT, GET_MD_PROMPT
from openai import OpenAI

class DoubaoLLM(BaseLLM):

    def __init__(self, model_name: str, language: str):
        self.client = OpenAI(
            api_key=os.environ.get("ARK_API_KEY"),
            base_url = "https://ark.cn-beijing.volces.com/api/v3",
        )
        self.model_name = model_name # For example: doubao-1-5-lite-32k-250115
        self.chat_history = [{"role": "system", "content": BEGIN_SYSTEM_PROMPT}]
        self.max_level = 5
        self.language = language

    def loop_pdf_input(self, pdf_result: list):
        # TODO async work with PdfProcess.feed_into_llm()
        for idx, text in enumerate(pdf_result):
            # user_msg = f"以下是第{idx+1}段资料，请做出摘要总结，用于准备最后得Markdown生成：\n{text}"
            user_msg = f"The following is the {idx + 1}-th piece of material. Please make a summary, which is used to prepare for the final Markdown generation:\n{text}"

            self.chat_history.append({"role": "user", "content": user_msg})

            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=self.chat_history,
                temperature=0.5
            )

            assistant_reply = response.choices[0].message.content
            self.chat_history.pop()
            self.chat_history.append({"role": "assistant", "content": assistant_reply})

            # print(f"✅ 第{idx+1}段资料已发送并记录摘要\n")
            print(f"✅ The {idx+1}-th piece of material has been sent and the summary has been recorded.")
            time.sleep(1)

    def get_md_result(self):
        # self.chat_history.append({"角色": "用户", "内容": GET_MD_PROMPT + f"生成的Markdown文档将使用{self.language}语言，并且最多有{self.max_level}个层级。"})
        self.chat_history.append({"role": "user", "content": GET_MD_PROMPT + f"The generated Markdown document will be in {self.language} and have a maximum of {self.max_level} hierarchical levels."})

        final_response = self.client.chat.completions.create(
            model=self.model_name,
            messages=self.chat_history,
            temperature=0.7
        )
        
        return final_response.choices[0].message.content
