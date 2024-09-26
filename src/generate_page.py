import os

from markdown_html import markdown_to_html_node
from htmlnode import ParentNode

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    md_string = open(from_path).read()
    template_string = open(template_path).read()

    html_node = markdown_to_html_node(md_string)
    html_string = html_node.to_html()

    template_string = template_string.replace('{{ Title }}', extract_title(md_string))
    template_string = template_string.replace('{{ Content }}', html_string)

    if os.path.dirname(dest_path) != '':
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    dest_file = open(dest_path, "a")
    dest_file.write(template_string)
    dest_file.close()


def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line.lstrip('#').strip()
    raise ValueError("No # / <h1> header found!")
        
    