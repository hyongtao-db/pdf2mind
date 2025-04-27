
from datetime import datetime
from mind.md_generator import generate_md
from mind.mm_generator import generate_freemind
from mind.svg_generator import generate_svg
from utils.log import logger

def gen_all_mindmaps(markdown_content, file_name, only_what):
    # logger.info("\n📝 Final generated Markdown content:\n")
    # logger.info(markdown_content)
    # Generate mind maps in various formats
    current_timestamp = datetime.now().strftime("%Y%m%d%H%M%S") # YYYYMMDDHHMMSS
    logger.info(f"Current timestamp is {current_timestamp}\n")
    output_name = file_name + "_" + str(current_timestamp)
    md_name = output_name + ".md"
    mm_name = output_name + ".mm"
    svg_name = output_name

    match only_what:
        case 0:
            generate_md(markdown_content, md_name)
            generate_freemind(markdown_content, mm_name)
            generate_svg(markdown_content, svg_name)
        case 1:
            generate_md(markdown_content, md_name)
        case 2:
            generate_freemind(markdown_content, mm_name)
        case 3:
            generate_svg(markdown_content, svg_name)
