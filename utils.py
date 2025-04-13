
from llm.base_llm import BaseLLM
from llm.doubao_llm import DoubaoLLM
from llm.qwen_llm import QwenLLM
from llm.openai_llm import OpenaiLLM

def model_selector(args) -> BaseLLM:
    if args.use_doubao:
        return DoubaoLLM(args.model, args.language)
    elif args.use_qwen:
        return QwenLLM(args.model, args.language)
    elif args.use_openai:
        return OpenaiLLM(args.model, args.language)
    else:
        # TODO: should not happen, check error and log out
        pass

def wrap_text(text, width=30):
    return '\n'.join([text[i:i+width] for i in range(0, len(text), width)])
