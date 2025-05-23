from collections.abc import Mapping


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = [] if children is None else children
        if props is not None and not isinstance(props, Mapping):
            raise TypeError(
                f"props must be a dict-like Mapping, got {type(props).__name__}"
            )
        else:
            self.props = {} if props is None else props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html = ""
        if not self.props:
            return html

        for key, value in self.props.items():
            if value is not None:
                html += f' {key}="{str(value)}"'
        return html

    def __repr__(self):
        children_repr = f"[{len(self.children)} children]" if self.children else "[]"
        return f"HTMLNODE(tag={self.tag}, value={self.value}, children={children_repr}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.tag is None:
            return str(self.value)

        props_str = self.props_to_html()

        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode must have a tag")
        if children is None:
            raise ValueError("ParentNode must have children")
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        opening_tag = f"<{self.tag}>"
        closing_tag = f"</{self.tag}>"

        children_html = "".join(child.to_html() for child in self.children)
        return f"{opening_tag}{children_html}{closing_tag}"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
