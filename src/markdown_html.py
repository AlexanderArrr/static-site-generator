from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_blocks import (markdown_to_blocks, 
                             block_to_block_type,
                             block_type_code,
                             block_type_heading,
                             block_type_ordered_list,
                             block_type_paragraph,
                             block_type_quote,
                             block_type_unordered_list)
from inline_markdown import text_to_textnodes
from textnode import textnode_to_htmlnode


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode('div', children, None)

    
def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    if block_type == block_type_unordered_list:
        return ulist_to_html_node(block)
    if block_type == block_type_ordered_list:
        return olist_to_html_node(block)
    raise ValueError("Invalid block type")
    


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = textnode_to_htmlnode(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split('\n')
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode('p', children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == '#':
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1:]
    children = text_to_children(text)
    return ParentNode(f'h{level}', children)


def code_to_html_node(block):
    if not block.startswith('```') or not block.endswith('```'):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode('code', children)
    return ParentNode('pre', [code])


def quote_to_html_node(block):
    lines = block.split('\n')
    stripped_lines = []
    for line in lines:
        if not line.startswith('>'):
            raise ValueError('Invalid quote block')
        stripped_lines.append(line.lstrip('>').strip())
    text = ' '.join(stripped_lines)
    children = text_to_children(text)
    return ParentNode('blockquote', children)


def ulist_to_html_node(block):
    items = block.split('\n')
    child_lines = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        child_lines.append(ParentNode('li', children))
    return ParentNode('ul', child_lines)


def olist_to_html_node(block):
    items = block.split('\n')
    child_lines = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        child_lines.append(ParentNode('li', children))
    return ParentNode('ol', child_lines)
