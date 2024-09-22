from textnode import TextNode

text_type_text = 'text'
text_type_bold = 'bold'
text_type_italic = 'italic'
text_type_code = 'code'
text_type_link = 'link'
text_type_image = 'image'

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = old_nodes.copy()
    li_return = []
    for node in new_nodes:
        if node.text_type != text_type_text:
            li_return = li_return.append(node)
        if not delimiter in node.text:
            li_return = li_return.append(node)
        else:
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
