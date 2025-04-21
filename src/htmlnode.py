class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = [] if children is None else children
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
