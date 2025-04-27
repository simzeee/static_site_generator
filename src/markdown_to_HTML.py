from markdown_to_blocks import markdown_to_blocks
from blocktype import block_to_block_type, BlockType
from htmlnode import ParentNode, LeafNode
from textnode import TextNode, TextType
from text_to_text_nodes import text_to_text_nodes
from text_node_to_html_node import text_node_to_html_node

"""converts a full markdown document into a single parent HTMLNode"""


def markdown_to_html_node(markdown):
    result = []
    blocks = markdown_to_blocks(markdown)
    # list of blocks
    blocks = [block for block in blocks if block.strip()]
    for block in blocks:
        # get block type
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            # gather all nodes to push into parent HTML node as children
            processed_text = block.replace("\n", " ")
            processed_text = " ".join(processed_text.split())
            text_nodes = text_to_text_nodes(processed_text)
            nodes_list = []
            # list of text_nodes
            for node in text_nodes:
                nodes_list.append(text_node_to_html_node(node))
            parent_p_tag = ParentNode("p", children=nodes_list)
            result.append(parent_p_tag)
        elif block_type == BlockType.HEADING:
            # extract heading level
            heading_level = 0
            for char in block:
                if char == "#":
                    heading_level += 1
                else:
                    break
            stripped_block = block.strip("#").lstrip()
            text_nodes = text_to_text_nodes(stripped_block)
            nodes_list = []
            for node in text_nodes:
                nodes_list.append(text_node_to_html_node(node))
            parent_h_tag = ParentNode(f"h{heading_level}", children=nodes_list)
            result.append(parent_h_tag)
        elif block_type == BlockType.QUOTE:
            # Extract lines from blockquote, removing the '>' prefix
            lines = []
            for line in block.split("\n"):
                stripped = line.strip()
                if stripped.startswith(">"):
                    # Remove the '>' and any single space after it
                    content = stripped[1:].strip()
                    lines.append(content)

            # Join lines with a space
            quote_text = " ".join(lines)

            # Process into HTML nodes
            text_nodes = text_to_text_nodes(quote_text)
            nodes_list = [text_node_to_html_node(n) for n in text_nodes]
            result.append(ParentNode("blockquote", children=nodes_list))
        elif block_type == BlockType.CODE:
            lines = block.split("\n")

            # Remove lines with triple backticks
            if lines and "```" in lines[0]:
                lines = lines[1:]
            if lines and "```" in lines[-1]:
                lines = lines[:-1]

            # Determine the common indentation to remove
            min_indent = float("inf")
            for line in lines:
                if line.strip():  # Only consider non-empty lines
                    indent = len(line) - len(line.lstrip())
                    min_indent = min(min_indent, indent)

            # If all lines were empty, min_indent will still be inf
            if min_indent == float("inf"):
                min_indent = 0

            # Remove the common indentation from each line
            dedented_lines = []
            for line in lines:
                if line.strip():  # Only dedent non-empty lines
                    dedented_lines.append(line[min_indent:])
                else:
                    dedented_lines.append(line)

            code_content = "\n".join(dedented_lines)
            if code_content and not code_content.endswith("\n"):
                code_content += "\n"
            code_node = LeafNode("code", code_content)
            pre_node = ParentNode("pre", children=[code_node])
            result.append(pre_node)
        elif block_type == BlockType.UNORDERED_LIST:
            list_items = []
            lines = block.split("\n")

            for line in lines:
                if line.strip():  # Skip empty lines
                    # Strip the "- " marker
                    item_text = line.strip().removeprefix("-").lstrip()

                    # Process inline formatting for this item
                    item_nodes = []
                    text_nodes = text_to_text_nodes(item_text)
                    for node in text_nodes:
                        item_nodes.append(text_node_to_html_node(node))

                    # Create li element with processed nodes as children
                    li_node = ParentNode("li", children=item_nodes)
                    list_items.append(li_node)

            # Create ul element with all li elements as children
            ul_node = ParentNode("ul", children=list_items)
            result.append(ul_node)
        elif block_type == BlockType.ORDERED_LIST:
            list_items = []
            lines = block.split("\n")

            for line in lines:
                if line.strip():  # Skip empty lines
                    # Strip digit(s) followed by period and space
                    item_text = line.strip()

                    # Find the position of the first period and space
                    # This helps us strip the "1. ", "2. ", etc.
                    parts = item_text.split(". ", 1)
                    if len(parts) > 1 and parts[0].isdigit():
                        item_text = parts[1]

                    # Process inline formatting for this item
                    item_nodes = []
                    text_nodes = text_to_text_nodes(item_text)
                    for node in text_nodes:
                        item_nodes.append(text_node_to_html_node(node))

                    # Create li element with processed nodes as children
                    li_node = ParentNode("li", children=item_nodes)
                    list_items.append(li_node)

            # Create ol element with all li elements as children
            ol_node = ParentNode("ol", children=list_items)
            result.append(ol_node)

    parent_node = ParentNode("div", result)
    return parent_node


md = """
    > This is a
    > blockquote block

    this is paragraph text

    """

markdown_to_html_node(md)
