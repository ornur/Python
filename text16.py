def remove_empty_lines_from_file(file_name):
    with open(file_name, 'r') as f:
        every_line = f.readlines()
    return [line for line in every_line if line.strip() != '']
