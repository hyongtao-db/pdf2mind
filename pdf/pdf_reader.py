import fitz  # pymupdf

class PdfProcess():

    def __extract_pdf_chunks(self, filepath, chunk_size=30000, overlap_size=1000):
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
            start += chunk_size - overlap_size

        return chunks

    def extract_pdf_chunks(self, args):
        pdf_name = str(args.pdf)
        chunk_size = getattr(args, 'chunk_size', None)
        overlap_size = getattr(args, 'overlap_size', None)
        
        kwargs = {}
        if chunk_size is not None:
            kwargs['chunk_size'] = int(chunk_size)
        if overlap_size is not None:
            kwargs['overlap_size'] = int(overlap_size)

        chunks = self.__extract_pdf_chunks(pdf_name, **kwargs)
        return chunks

    def feed_into_llm():
        # TODO it should be an async work
        pass
