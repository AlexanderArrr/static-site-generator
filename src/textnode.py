from htmlnode import LeafNode

text_type_text = 'text'
text_type_bold = 'bold'
text_type_italic = 'italic'
text_type_code = 'code'
text_type_link = 'link'
text_type_image = 'image'

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def textnode_to_htmlnode(textnode):
    if textnode.text_type == 'text':
        textnode = LeafNode(None,textnode.text)
        return textnode
    if textnode.text_type == 'bold':
        textnode = LeafNode('b', textnode.text)
        return textnode
    if textnode.text_type == 'italic':
        textnode = LeafNode('i', textnode.text)
        return textnode
    if textnode.text_type == 'code':
        textnode = LeafNode('code', textnode.text)
        return textnode
    if textnode.text_type == 'link':
        textnode = LeafNode('a', textnode.text, {'href':textnode.url})
        return textnode
    if textnode.text_type == 'image':
        textnode = LeafNode('img', "", {'src':textnode.url, 'alt':textnode.text})
        return textnode
    raise ValueError(f"Invalid text type: {textnode.text_type}")
    

