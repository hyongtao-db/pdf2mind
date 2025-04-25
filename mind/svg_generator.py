from graphviz import Digraph
from utils.utils import wrap_text
from utils.log import logger

def parse_markdown(md_text):
    lines = md_text.strip().splitlines()
    stack = []
    nodes = {}
    node_id = 0
    last_node_id = None

    for line in lines:
        if line.strip() == "":
            continue  # skip empty line
        if line.strip().startswith("#"):
            level = line.count("#")
            title = line.strip("#").strip()
            curr_id = f"node{node_id}"
            nodes[curr_id] = {"title": title, "level": level}
            while stack and stack[-1][1] >= level:
                stack.pop()
            if stack:
                parent_id = stack[-1][0]
                nodes[curr_id]["parent"] = parent_id
            else:
                nodes[curr_id]["parent"] = None
            stack.append((curr_id, level))
            last_node_id = curr_id
            node_id += 1
        else:
            content = line.strip()
            curr_id = f"node{node_id}"
            nodes[curr_id] = {
                "title": wrap_text(content),
                "level": (nodes[last_node_id]["level"] + 1) if last_node_id else 1,
                "parent": last_node_id
            }
            node_id += 1

    return nodes

def tree_to_svg(nodes, output_file="mindmap"):
    dot = Digraph(format="svg")
    dot.attr(rankdir="LR")  # Left to Right

    level_colors = {
        1: "lightblue",
        2: "lightgreen",
        3: "yellow",
        4: "orange",
        5: "pink",
        6: "gray"
    }

    for node_id, node in nodes.items():
        color = level_colors.get(node["level"], "white")
        dot.node(node_id, node["title"], shape="box", style="rounded,filled", fillcolor=color)
        if node["parent"]:
            dot.edge(node["parent"], node_id)
    dot.render(output_file, view=False)

def generate_svg(md_text, output_file="mindmap"):    
    tree = parse_markdown(md_text)
    # TODO try catch here
    tree_to_svg(tree, output_file)
    logger.info(f"✅ The SVG mind map has been successfully generated: {output_file}.svg")
