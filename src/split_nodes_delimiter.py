from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    # iterate through list of nodes
    for old_node in old_nodes:
        # if it's not a text node, push it to the result
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
        else:
            # if it is then split it by the delimiter
            # so we can convert it to different node types
            split_node_text = old_node.text.split(delimiter)

            if len(split_node_text) % 2 == 0:
                raise ValueError("Must use valid markdown syntax")
            for idx, text in enumerate(split_node_text):
                # odd-indexed parts are whatever the delimiter is and
                # even-indexed parts are Text
                if text == "":
                    continue
                if idx % 2 == 0:
                    result.append(TextNode(text, TextType.TEXT))
                if idx % 2 != 0:
                    result.append(TextNode(text, text_type))

    return result
