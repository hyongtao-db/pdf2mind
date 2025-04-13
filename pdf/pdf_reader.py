import fitz  # pymupdf

class PdfProcess():

    # TODO, make chunk_size and overlap adjustable
    def extract_pdf_chunks(filepath, chunk_size=30000, overlap=200):
        # open pdf file
        doc = fitz.open(filepath)
        
        # Extract the text of all pages
        full_text = ""
        for page in doc:
            full_text += page.get_text()

        # Split into overlapping segments
        chunks = []
        start = 0
        text_length = len(full_text)

        while start < text_length:
            end = min(start + chunk_size, text_length)
            chunk = full_text[start:end]
            chunks.append(chunk)
            # Update the starting position, taking overlapping into account
            start += chunk_size - overlap

        return chunks

    def feed_into_llm():
        # TODO it should be an async work
        pass 