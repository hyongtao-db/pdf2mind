
from llm.base_llm import BaseLLM
from llm.doubao_llm import DoubaoLLM
from llm.qwen_llm import QwenLLM
from llm.openai_llm import OpenaiLLM

def model_selector(args) -> BaseLLM:
    # set default
    max_level = getattr(args, 'max_level', 4)
    temperature = getattr(args, 'temperature', 0.7)

    if getattr(args, 'use_doubao', False):
        return DoubaoLLM(args.model, args.language, max_level, temperature)
    elif getattr(args, 'use_qwen', False):
        return QwenLLM(args.model, args.language, max_level, temperature)
    elif getattr(args, 'use_openai', False):
        return OpenaiLLM(args.model, args.language, max_level, temperature)
    else:
        raise ValueError("Please at least set one of --use-doubao、--use-qwen or --use-openai")

def format_selector(args) -> int:
    if args.only_freemind:
        return 1
    elif args.only_xmind:
        return 2
    elif args.only_svg:
        return 3
    return 0

def wrap_text(text, width=30):
    return '\n'.join([text[i:i+width] for i in range(0, len(text), width)])
