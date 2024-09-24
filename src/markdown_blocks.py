
def markdown_to_blocks(markdown):
    lines_list = markdown.split('\n\n')
    filtered_lines = []
    for line in lines_list:
        if line == "":
            continue
        line = line.strip()
        filtered_lines.append(line)
    return filtered_lines
