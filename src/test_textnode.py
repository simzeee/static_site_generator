import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("equal node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("not equal node", TextType.ITALIC, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_url_is_none(self):
        node = TextNode("equal node", TextType.ITALIC)
        self.assertEqual(node.url, None)

    def test_text_type_is_different(self):
        node = TextNode("equal node", TextType.CODE, "https://www.boot.dev")
        node2 = TextNode("not equal node", TextType.LINK, "https://www.boot.dev")
        self.assertNotEqual(node.text_type, node2.text_type)


if __name__ == "__main__":
    unittest.main()
