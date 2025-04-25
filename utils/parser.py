import argparse
import os
import sys

from utils.log import logger, setup_logger

# TODO: add pytest for cmd check
def cmd_parser():
    parser = argparse.ArgumentParser(description="Command-line parser: PDF filename + Model selection")

    ### required qrguments
    parser.add_argument("--pdf", type=str, required=True, help="PDF filename")
    parser.add_argument("--model", type=str, required=True, help="model name")
    parser.add_argument("--language", type=str, required=True, help="Target language (e.g., 'English', 'Chinese', 'France', etc.)")
    # parser.add_argument("--key", help="LLM API Key (can also be provided via environment variable LLM_API_KEY)")

    # mutually exclusive group for model selection
    llm_group = parser.add_mutually_exclusive_group(required=True)
    llm_group.add_argument("--use-doubao", action="store_true", help="Use Doubao model")
    llm_group.add_argument("--use-qwen", action="store_true", help="Use Qwen model")
    llm_group.add_argument("--use-openai", action="store_true", help="Use OpenAI model")

    ### optional arguments
    parser.add_argument("--chunk-size", type=int, help="chunk size of PDF (optional, default 30000)")
    parser.add_argument("--overlap-size", type=int, help="overlap size of PDF (optional, default 1000)")
    parser.add_argument("--max-level", type=int, default=4, help="maximum level for mind maps (optional, default: 4)")
    parser.add_argument("--temperature", type=float, default=0.7, help="LLM temperature (optional, default: 0.7)")

    # mutually exclusive group for output format selection
    format_group = parser.add_mutually_exclusive_group()
    format_group.add_argument("--only-freemind", action="store_true", help="Only generate FreeMind (.mm) format")
    format_group.add_argument("--only-xmind", action="store_true", help="Only generate XMind (.md) format")
    format_group.add_argument("--only-svg", action="store_true", help="Only generate SVG (.svg) format")

    # log related
    parser.add_argument('--debug', action='store_true', help='Enable debug log output')

    args = parser.parse_args()

    # setup log
    setup_logger(debug_mode=args.debug)

    pdf_file = args.pdf
    model = args.model
    language = args.language

    # Determine selected model
    if args.use_doubao:
        vender = "Doubao"
        llm_key = os.getenv("ARK_API_KEY")
    elif args.use_qwen:
        vender = "Qwen"
        llm_key = os.getenv("DASHSCOPE_API_KEY")
    elif args.use_openai:
        vender = "OpenAI"
        llm_key = os.getenv("OPENAI_API_KEY")
    else:
        # Should not happen due to required=True
        vender = "Unknown"

    if not llm_key:
        logger.info("Error: LLM API Key is required. Please provide it via --key argument or set the XXX_API_KEY environment variable.")
        sys.exit(1)

    logger.info(f"📄 PDF filename: {pdf_file}")
    # logger.info(f"🔑 LLM API Key: {llm_key}")
    logger.info(f"🌍 Target language: {language}")
    logger.info(f"🧠 Selected vender: {vender}")
    logger.info(f"🤖 Model name: {model}\n")
    
    args = parser.parse_args()
    return args
