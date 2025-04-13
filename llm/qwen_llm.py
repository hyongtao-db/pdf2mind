import time
import os

from llm.base_llm import BaseLLM, BEGIN_SYSTEM_PROMPT, GET_MD_PROMPT
from openai import OpenAI

class QwenLLM(BaseLLM):

    def __init__(self, model_name: str, language: str):
        self.client = OpenAI(
            api_key = os.getenv("DASHSCOPE_API_KEY"),
            base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1",
        )
        self.model_name = model_name,
        self.chat_history = [{"role": "system", "content": BEGIN_SYSTEM_PROMPT}]
        self.max_level = 5
        self.language = language

    def loop_pdf_input(self, pdf_result: list):
        # TODO async work with PdfProcess.feed_into_llm()
        for idx, text in enumerate(pdf_result):
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

            print(f"✅ The {idx+1}-th piece of material has been sent and the summary has been recorded.\n")
            time.sleep(1)

    def get_md_result(self):
        self.chat_history.append({"role": "user", "content": GET_MD_PROMPT + f"The generated Markdown document will be in {self.language} and have a maximum of {self.max_level} hierarchical levels."})

        final_response = self.client.chat.completions.create(
            model=self.model_name,
            messages=self.chat_history,
            temperature=0.7
        )
        
        return final_response.choices[0].message.content