import argparse
import os
import sys

# TODO: add pytest for cmd check
def cmd_parser():
    parser = argparse.ArgumentParser(description="Command-line parser: PDF filename + Model selection")

    ### required qrguments
    parser.add_argument("--pdf", required=True, help="PDF filename")
    parser.add_argument("--model", required=True, help="model name")
    parser.add_argument("--language", required=True, help="Target language (e.g., 'English', 'Chinese', 'France', etc.)")
    # parser.add_argument("--key", help="LLM API Key (can also be provided via environment variable LLM_API_KEY)")

    # mutually exclusive group for model selection
    llm_group = parser.add_mutually_exclusive_group(required=True)
    llm_group.add_argument("--use-doubao", action="store_true", help="Use Doubao model")
    llm_group.add_argument("--use-qwen", action="store_true", help="Use Qwen model")
    llm_group.add_argument("--use-openai", action="store_true", help="Use OpenAI model")

    ### optional arguments
    parser.add_argument("--chunk-size", help="chunk size of PDF (optional, default 30000)")
    parser.add_argument("--overlap-size", help="overlap size of PDF (optional, default 1000)")

    # mutually exclusive group for output format selection
    format_group = parser.add_mutually_exclusive_group()
    format_group.add_argument("--only-freemind", action="store_true", help="Only generate FreeMind (.mm) format")
    format_group.add_argument("--only-xmind", action="store_true", help="Only generate XMind (.xmind) format")
    format_group.add_argument("--only-svg", action="store_true", help="Only generate SVG (.svg) format")

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
