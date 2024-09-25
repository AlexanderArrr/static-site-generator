from htmlnode import ParentNode
from textnode import textnode_to_htmlnode
from inline_markdown import text_to_textnodes
from markdown_blocks import (block_to_block_type,
                             markdown_to_blocks,
                             block_type_code,
                             block_type_heading,
                             block_type_ordered_list,
                             block_type_paragraph,
                             block_type_quote,
                             block_type_unordered_list)


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_htmlnode(block)
        children.append(html_node)
    return ParentNode('div', children)


def block_to_htmlnode(block):
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
    raise ValueError(f"Invalid block type: ({block_type})")


def text_to_children(text):
    children = []
    textnodes = text_to_textnodes(text)
    for node in textnodes:
        child = textnode_to_htmlnode(node)
        children.append(child)
    return children


def paragraph_to_html_node(block):
    lines = block.split('\n')
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode('p', children)


def heading_to_html_node(block):
    heading_level = 0
    for char in block:
        if char != '#':
            break
        heading_level += 1
    if heading_level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {heading_level}")
    text = block[heading_level + 1:]
    children = text_to_children(text)
    return ParentNode(f'h{heading_level}', children)


def code_to_html_node(block):
    if not block.startswith('```') and not block.endswith('```'):
        raise ValueError("Invalid code block")
    code_text = block[4:-3]
    children = text_to_children(code_text)
    code_node = ParentNode('code', children)
    return ParentNode('pre', [code_node])
    

def quote_to_html_node(block):
    lines = block.split('\n')
    stripped_lines = []
    for line in lines:
        if not line.startswith('>'):
            raise ValueError("Invalid code block")
        stripped_lines.append(line.lstrip('>').strip())
    quote_block = ' '.join(stripped_lines)
    children = text_to_children(quote_block)
    return ParentNode('blockquote', children)


def ulist_to_html_node(block):
    items = block.split('\n')
    child_nodes = []
    for item in items:
        text = item[2:]
        child = text_to_children(text)
        child_nodes.append(ParentNode('li', child))
    return ParentNode('ul', child_nodes)
    

def olist_to_html_node(block):
    items = block.split('\n')
    child_nodes = []
    for item in items:
        text = item[3:]
        child = text_to_children(text)
        child_nodes.append(ParentNode('li', child))
    return ParentNode('ol', child_nodes)

