from src.extract_markdown_images import extract_markdown_images, extract_markdown_links
from src.textnode import TextNode, TextType

"""
Extract all images from the original text
For each image:
Split the current working text at the image
Create a node for the text before the image
Create a node for the image itself
Update the current working text to be what comes after the image
After processing all images, if there's any text left, create a node for it
"""


def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        current_text = node.text
        # returns an array of tuples with ('alt text', 'url')
        extracted_image = extract_markdown_images(current_text)
        # print(f"Extracted images: {extracted_image}")
        if not extracted_image:
            # append note to result if there are no images
            result.append(node)
        else:
            for image in extracted_image:
                alt_text, image_url = image
                parts = current_text.split(f"![{alt_text}]({image_url})", 1)
                # print(f"Split parts: {parts}")
                # if there's text before the image
                if parts[0]:
                    text_node = TextNode(parts[0], TextType.TEXT)
                    # print(f"Adding text node: {text_node}")
                    result.append(TextNode(parts[0], TextType.TEXT))
                # add image to result
                image_node = TextNode(alt_text, TextType.IMAGE, image_url)
                # print(f"Adding image node: {image_node}")
                result.append(image_node)
                current_text = parts[1]
            if current_text:
                text_node = TextNode(current_text, TextType.TEXT)
                # print(f"Adding final text node: {text_node}")
                result.append(TextNode(current_text, TextType.TEXT))
    # print(f"Final result: {result}")
    return result


def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        current_text = node.text
        extracted_links = extract_markdown_links(current_text)
        if not extracted_links:
            result.append(node)
        else:
            for link in extracted_links:
                link_text, url = link
                parts = current_text.split(f"[{link_text}]({url})", 1)

                if parts[0]:
                    result.append(TextNode(parts[0], TextType.TEXT))
                link_node = TextNode(link_text, TextType.LINK, url)
                result.append(link_node)
                current_text = parts[1]
            if current_text:
                result.append(TextNode(current_text, TextType.TEXT))
    return result


node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)
new_nodes = split_nodes_link([node])
# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]
