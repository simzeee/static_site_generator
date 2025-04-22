import unittest

from src.htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_repr_with_no_children(self):
        node = HTMLNode("div", "the best div", None, {"class": "container"})
        rep = node.__repr__()
        test_string = "HTMLNODE(tag=div, value=the best div, children=[], props={'class': 'container'})"
        self.assertEqual(rep, test_string)

    def test_repr_with_no_props(self):
        child1 = HTMLNode(
            tag="p", value="First paragraph", children=None, props={"class": "text"}
        )
        child2 = HTMLNode(
            tag="p", value="Second paragraph", children=None, props={"class": "text"}
        )
        node = HTMLNode("div", "the best div", [child1, child2], None)
        rep = node.__repr__()
        test_string = (
            "HTMLNODE(tag=div, value=the best div, children=[2 children], props={})"
        )
        self.assertEqual(rep, test_string)

    def test_repr_with_all_properties(self):
        child1 = HTMLNode(
            tag="p", value="First paragraph", children=None, props={"class": "text"}
        )
        child2 = HTMLNode(
            tag="p", value="Second paragraph", children=None, props={"class": "text"}
        )
        node = HTMLNode("div", "the best div", [child1, child2], {"class": "container"})
        rep = node.__repr__()
        test_string = "HTMLNODE(tag=div, value=the best div, children=[2 children], props={'class': 'container'})"
        self.assertEqual(rep, test_string)


if __name__ == "__main__":
    unittest.main()
