from abc import ABC, abstractmethod


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

    @abstractmethod
    def loop_pdf_input(self):
        pass

    @abstractmethod
    def get_md_result(self):
        pass
