import re

from textnode import TextNode

text_type_text = 'text'
text_type_bold = 'bold'
text_type_italic = 'italic'
text_type_code = 'code'
text_type_link = 'link'
text_type_image = 'image'

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, '**', text_type_bold)
    nodes = split_nodes_delimiter(nodes, '*', text_type_italic)
    nodes = split_nodes_delimiter(nodes, '`', text_type_code)
    nodes = split_nodes_images(nodes)
    nodes = split_nodes_links(nodes)
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    li_return = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            li_return.append(node)
            continue
        li_split_strings = node.text.split(delimiter)
        if len(li_split_strings) % 2 == 0:
            raise Exception("Invalid markdown syntax - can not split the strings!")
        for i in range(0, len(li_split_strings)):
            if li_split_strings[i] == '':
                continue
            if i % 2 == 0:
                new_textnode = TextNode(li_split_strings[i], text_type_text)
                li_return.append(new_textnode)
            else:
                new_textnode = TextNode(li_split_strings[i], text_type)
                li_return.append(new_textnode)
    
    return li_return


def split_nodes_images(old_nodes):
    li_return = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            li_return.append(node)
            continue
        current_text = node.text
        extracted_images = extract_markdown_images(current_text)
        if len(extracted_images) == 0:
            li_return.append(node)
            continue
        for image in extracted_images:
            sections = current_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section incorrect!")
            if sections[0] != "":
                li_return.append(TextNode(sections[0], text_type_text))
            li_return.append(TextNode(image[0], text_type_image, image[1]))
            current_text = sections[1]
        if current_text != "":
            li_return.append(TextNode(current_text, text_type_text))
    return li_return


def split_nodes_links(old_nodes):
    li_return = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            li_return.append(node)
            continue
        current_text = node.text
        extracted_links = extract_markdown_links(current_text)
        if len(extracted_links) == 0:
            li_return.append(node)
            continue
        for link in extracted_links:
            sections = current_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section incorrect!")
            if sections[0] != "":
                li_return.append(TextNode(sections[0], text_type_text))
            li_return.append(TextNode(link[0], text_type_link, link[1]))
            current_text = sections[1]
        if current_text != "":
            li_return.append(TextNode(current_text, text_type_text)) 
    return li_return


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

