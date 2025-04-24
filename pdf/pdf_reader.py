import asyncio
import fitz  # pymupdf

class PdfProcess():

    def __extract_pdf_chunks(self, filepath, chunk_size=30000, overlap_size=1000):
        doc = fitz.open(filepath)
        full_text = "".join(page.get_text() for page in doc)

        chunks = []
        start = 0
        text_length = len(full_text)

        while start < text_length:
            end = min(start + chunk_size, text_length)
            chunk = full_text[start:end]
            chunks.append(chunk)
            start += chunk_size - overlap_size

        return chunks

    async def extract_and_feed_chunks(self, args, queue: asyncio.Queue):
        pdf_name = str(args.pdf)
        chunk_size = getattr(args, 'chunk_size', None)
        overlap_size = getattr(args, 'overlap_size', None)
        
        kwargs = {}
        if chunk_size is not None:
            kwargs['chunk_size'] = int(chunk_size)
        if overlap_size is not None:
            kwargs['overlap_size'] = int(overlap_size)

        chunks = self.__extract_pdf_chunks(pdf_name, **kwargs)
        print(f"📄 The PDF has been split into {len(chunks)} parts.")

        for idx, chunk in enumerate(chunks):
            await queue.put((idx, chunk))
            print(f"📤 Put chunk {idx+1} into queue.")

        await queue.put(None)
