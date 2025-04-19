from utils.parser import cmd_parser 
from pdf.pdf_reader import PdfProcess
from mind.generator import gen_all_mindmaps
from utils.utils import model_selector, format_selector

def main():
    args = cmd_parser()
    
    processor = PdfProcess()
    chunks = processor.extract_pdf_chunks(args)
    print("The PDF has been split into", len(chunks), "parts")
    
    llm_model = model_selector(args)
    llm_model.loop_pdf_input(chunks)
    markdown_output = llm_model.get_md_result()

    pdf_name = str(args.pdf)
    only_what_format = format_selector(args)
    gen_all_mindmaps(markdown_output, pdf_name, only_what_format)

if __name__ == "__main__":
    main()
