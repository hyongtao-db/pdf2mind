def generate_md(markdown_output: str, output_file: str):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(markdown_output)
        print(f"✅ The Xmind mind map has been successfully generated: {output_file}")
    except IOError:
        print(f"❌ Could not save the file: {output_file}")
