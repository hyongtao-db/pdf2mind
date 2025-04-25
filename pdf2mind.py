import asyncio
from utils.parser import cmd_parser 
from pdf.pdf_reader import PdfProcess
from mind.generator import gen_all_mindmaps
from utils.utils import model_selector, format_selector


async def main():
    args = cmd_parser()

    processor = PdfProcess()
    queue = asyncio.Queue()

    llm_model = model_selector(args)

    producer_task = asyncio.create_task(processor.extract_and_feed_chunks(args, queue))

    async def consumer():
        while True:
            item = await queue.get()
            if item is None:
                break
            idx, chunk = item
            await llm_model.process_chunk(idx, chunk)

    consumer_task = asyncio.create_task(consumer())

    await asyncio.gather(producer_task, consumer_task)

    markdown_output = llm_model.get_md_result()

    pdf_name = str(args.pdf)
    only_what_format = format_selector(args)
    gen_all_mindmaps(markdown_output, pdf_name, only_what_format)


if __name__ == "__main__":
    asyncio.run(main())
