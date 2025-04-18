from llm.base_llm import BaseLLM

class QwenLLM(BaseLLM):

    def __init__(self, model_name: str, language: str, max_level: int, temperature: float):
        super().__init__(
            model_name=model_name,
            language=language,
            max_level=max_level,
            temperature=temperature,
            api_key_env="DASHSCOPE_API_KEY",
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        )
