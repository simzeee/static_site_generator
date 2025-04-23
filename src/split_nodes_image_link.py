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
    pass


node = TextNode(
    "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
    TextType.TEXT,
)
new_nodes = split_nodes_image([node])

# [
#     TextNode("This is text with an ", TextType.TEXT),
#     TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
#     TextNode(" and another ", TextType.TEXT),
#     TextNode(
#         "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
#     ),
# ],


# extracting images works this way
# def test_extract_markdown_images(self):
#     matches = extract_markdown_images(
#         "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
#     )
#     self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
