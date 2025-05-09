from llm.base_llm import BaseLLM

class OpenaiLLM(BaseLLM):

    def __init__(self, model_name: str, language: str, max_level: int, temperature: float):
        super().__init__(
            model_name=model_name,
            language=language,
            max_level=max_level,
            temperature=temperature,
            api_key_env="OPENAI_API_KEY",
            base_url="https://api.openai.com/v1"
        )
