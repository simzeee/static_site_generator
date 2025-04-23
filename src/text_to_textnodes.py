from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image_link import split_nodes_image, split_nodes_link
from textnode import TextType, TextNode


def text_to_textnodes(text):
    new_node = TextNode(text, TextType.TEXT)
    delimiters = [("**", TextType.BOLD), ("_", TextType.ITALIC), ("`", TextType.CODE)]
    result = [new_node]

    for delimiter in delimiters:
        refined_result = []
        for node in result:
            if node.text_type == TextType.TEXT:
                refined_result.extend(
                    split_nodes_delimiter([node], delimiter[0], delimiter[1])
                )
            else:
                refined_result.append(node)
        result = refined_result
    result = split_nodes_image(result)
    result = split_nodes_link(result)

    return result
