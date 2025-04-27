import xml.etree.ElementTree as ET

from utils.log import logger

def parse_markdown(md_text):
    lines = md_text.strip().splitlines()
    tree = []
    stack = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i].strip()
        if line.startswith("#"):
            level = line.count("#")
            title = line.strip("# ").strip()
            node = {"title": title, "level": level, "children": []}

            while stack and stack[-1]["level"] >= level:
                stack.pop()
            if stack:
                stack[-1]["children"].append(node)
            else:
                tree.append(node)
            stack.append(node)
            i += 1

            description_lines = []
            while i < n and not lines[i].strip().startswith("#"):
                if lines[i].strip() != "":
                    description_lines.append(lines[i].strip())
                i += 1
            if description_lines:
                desc_text = " ".join(description_lines)
                desc_node = {
                    "title": desc_text,
                    "level": level + 1,
                    "children": []
                }
                node["children"].append(desc_node)
        else:
            i += 1

    return tree

def build_freemind_node(xml_parent, node_dict):
    xml_node = ET.SubElement(xml_parent, "node", TEXT=node_dict["title"])
    for child in node_dict.get("children", []):
        build_freemind_node(xml_node, child)

def generate_freemind(md_text, output_file="freemind-output.mm"):
    tree_data = parse_markdown(md_text)
    root = ET.Element("map", version="0.9.0")
    for item in tree_data:
        build_freemind_node(root, item)
    tree = ET.ElementTree(root)

    try:
        with open(output_file, 'w', encoding='utf-8'):
            tree.write(output_file, encoding="utf-8", xml_declaration=True)
        logger.info(f"✅ The freemind mind map has been successfully generated: {output_file}")
    except IOError:
        logger.info(f"❌ Could not save the file: {output_file}")
