from utils.log import logger

def generate_md(markdown_output: str, output_file: str):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(markdown_output)
        logger.info(f"✅ The Xmind mind map has been successfully generated: {output_file}")
    except IOError:
        logger.info(f"❌ Could not save the file: {output_file}")
