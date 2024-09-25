import re

block_type_code = "code"
block_type_heading = "heading"
block_type_ordered_list = "ordered_list"
block_type_paragraph = "paragraph"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"

def markdown_to_blocks(markdown):
    blocks_list = markdown.split('\n\n')
    filtered_blocks = []
    for block in blocks_list:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    if block.startswith('```') and block.endswith('```'):
        return block_type_code
    if block.startswith(('# ', '## ', '### ', '#### ', '##### ', '###### ')):
        return block_type_heading
    if block.startswith('>'):
        split_block = block.split('\n')
        for line in split_block:
            if not line.startswith('>'):
                return block_type_paragraph
        return block_type_quote
    if block.startswith('* ') or block.startswith('- '):
        split_block = block.split('\n')
        for line in split_block:
            if not line.startswith('* ') and not line.startswith('- '):
                return block_type_paragraph
        return block_type_unordered_list
    if block.startswith('1. '):
        split_block = block.split('\n')
        list_number = 1
        for line in split_block:
            if not line.startswith(f"{list_number}. "):
                return block_type_paragraph
            list_number += 1
        return block_type_ordered_list
    return block_type_paragraph
