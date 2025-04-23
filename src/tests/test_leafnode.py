import unittest
from src.htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        # Test when tag is None
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

    def test_leaf_to_html_with_props(self):
        # Test with properties
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_leaf_to_html_multiple_props(self):
        # Test with multiple properties
        node = LeafNode(
            "img", "An image", {"src": "image.jpg", "alt": "An image", "width": 100}
        )
        self.assertEqual(
            node.to_html(),
            '<img src="image.jpg" alt="An image" width="100">An image</img>',
        )

    def test_leaf_node_value_none(self):
        # Test that ValueError is raised when value is None
        with self.assertRaises(ValueError):
            LeafNode("p", None)
