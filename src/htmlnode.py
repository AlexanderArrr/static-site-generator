

class HTMLNode:


    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __eq__(self, other):
        if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
            return True
        return False
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        result = ""
        if self.props:
            for key, value in self.props.items():
                result += f' {key}="{value}"'
        return result

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNodes must have a value!")
        if self.tag == None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'


    def __repr__(self):
        return f"LeafNode: {self.tag}, {self.value}, {self.props}"
    

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag!")
        if self.children is None:
            raise ValueError("ParentNode must have children!")
        child_str = ""
        for child in self.children:
            child_str += child.to_html()        
        return f'<{self.tag}{self.props_to_html()}>{child_str}</{self.tag}>'