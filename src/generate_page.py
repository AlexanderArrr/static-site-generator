import os

from markdown_html import markdown_to_html_node
from htmlnode import ParentNode
from pathlib import Path

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


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    new_content_path = Path(dir_path_content)
    new_template_path = Path(template_path)
    new_dest_path = Path(dest_dir_path)

    if not os.path.exists(new_dest_path):
        os.mkdir(new_dest_path)

    content_file_list = os.listdir(new_content_path)
    for entry in content_file_list:
        entry_content_path = os.path.join(new_content_path, entry)
        entry_dest_path = os.path.join(new_dest_path, entry)
        if not os.path.isfile(entry_content_path):
            generate_pages_recursive(entry_content_path, template_path, entry_dest_path)
        if not os.path.exists(entry_dest_path):
            md_string = open(entry_content_path).read()
            template_string = open(new_template_path).read()

            html_node = markdown_to_html_node(md_string)
            html_string = html_node.to_html()

            template_string = template_string.replace('{{ Title }}', extract_title(md_string))
            template_string = template_string.replace('{{ Content }}', html_string)

            entry_dest_path = entry_dest_path.replace('.md', '.html')
            dest_file = open(entry_dest_path, "a")
            dest_file.write(template_string)
            dest_file.close()


def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line.lstrip('#').strip()
    raise ValueError("No # / <h1> header found!")
        
    