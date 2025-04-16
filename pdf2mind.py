
from parser import cmd_parser 
from pdf.pdf_reader import PdfProcess
from mind.generator import gen_all_mindmaps
from utils import model_selector

def main():
    args = cmd_parser()
    
    pdf_name = str(args.pdf)
    
    chunks = PdfProcess.extract_pdf_chunks(pdf_name, int(args.chunk_size), int(args.overlap_size))
    print("The PDF has been split into", len(chunks), "parts")
    
    llm_model = model_selector(args)
    llm_model.loop_pdf_input(chunks)
    markdown_output = llm_model.get_md_result()

    
    gen_all_mindmaps(markdown_output, pdf_name)

if __name__ == "__main__":
    main()
