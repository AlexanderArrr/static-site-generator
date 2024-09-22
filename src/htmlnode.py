

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
        return f"HTMLNode: {self.tag}, {self.value}, {self.children}, {self.props}"

    def to_html(self):
        raise NotImplemented
    
    def props_to_html(self):
        result = ""
        if self.props:
            for key, value in self.props.items():
                result += f' {key}="{value}"'
        return result

class LeafNode(HTMLNode):

    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNodes must have a value!")
        if self.tag == None:
            return self.value
        
        if self.props == None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
