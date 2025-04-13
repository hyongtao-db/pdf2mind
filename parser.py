import argparse
import os
import sys

import argparse
import os
import sys

import argparse
import os
import sys

# TODO: add pytest for cmd check
def cmd_parser():
    parser = argparse.ArgumentParser(description="Command-line parser: PDF filename + LLM API Key + Model selection")

    parser.add_argument("--pdf", required=True, help="PDF filename")
    parser.add_argument("--model", required=True, help="model name)")
    parser.add_argument("--language", required=True, help="Target language (e.g., 'English', 'Chinese', 'France', etc.)")
    # parser.add_argument("--key", help="LLM API Key (can also be provided via environment variable LLM_API_KEY)")

    # Mutually exclusive group for model selection
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--use-doubao", action="store_true", help="Use Doubao model")
    group.add_argument("--use-qwen", action="store_true", help="Use Qwen model")
    group.add_argument("--use-openai", action="store_true", help="Use OpenAI model")

    args = parser.parse_args()

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
        print("Error: LLM API Key is required. Please provide it via --key argument or set the XXX_API_KEY environment variable.")
        sys.exit(1)

    # Print the parsed results, TODO: use logging rather than print
    print("\n")
    print("📄 PDF filename:", pdf_file)
    # print("🔑 LLM API Key:", llm_key)
    print("🌍 Target language:", language)
    print("🧠 Selected vender:", vender)
    print("🤖 Model name:", model, "\n")
    
    args = parser.parse_args()
    return args
