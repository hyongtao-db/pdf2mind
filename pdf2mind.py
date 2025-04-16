
from parser import cmd_parser 
from pdf.pdf_reader import PdfProcess
from mind.generator import gen_all_mindmaps
from utils import model_selector, format_selector

def main():
    args = cmd_parser()
    
    pdf_name = str(args.pdf)
    chunk_size = getattr(args, 'chunk_size', None)
    overlap_size = getattr(args, 'overlap_size', None)
    
    if chunk_size is not None and overlap_size is not None:
        chunks = PdfProcess.extract_pdf_chunks(pdf_name, int(chunk_size), int(overlap_size))
    elif chunk_size is not None:
        chunks = PdfProcess.extract_pdf_chunks(pdf_name, chunk_size=int(chunk_size))
    elif overlap_size is not None:
        chunks = PdfProcess.extract_pdf_chunks(pdf_name, overlap_size=int(overlap_size))
    else:
        chunks = PdfProcess.extract_pdf_chunks(pdf_name)
    print("The PDF has been split into", len(chunks), "parts")
    
    llm_model = model_selector(args)
    llm_model.loop_pdf_input(chunks)
    markdown_output = llm_model.get_md_result()

    only_what = format_selector(args)
    gen_all_mindmaps(markdown_output, pdf_name, only_what)

if __name__ == "__main__":
    main()
