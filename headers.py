import re
import sys
from collections import defaultdict

def insert_ids(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    id_counter = defaultdict(int)
    updated_lines = []
    inside_code_block = False
    
    for line in lines:
        if line.startswith("```"):
            inside_code_block = not inside_code_block
        if inside_code_block:
            updated_lines.append(line)
            continue
        
        if line.startswith('#'):
            header_level = len(re.match(r'#+', line).group(0))
            header = re.sub(r'#', '', line).strip()
            id_counter[header] += 1
            id = id_counter[header]
            line = f"{'#' * header_level} <a id='{id}'></a>{header}\n"
        
        updated_lines.append(line)
    
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(updated_lines)

def generate_toc(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    toc = []
    inside_code_block = False
    
    for line in lines:
        if line.startswith("```"):
            inside_code_block = not inside_code_block
        if inside_code_block:
            continue
        
        match = re.match(r'(#+) <a id=\'(\d+)\'></a>(.*)', line)
        if match:
            level = len(match.group(1))
            id = match.group(2)
            header = match.group(3).strip()
            clean_header = re.sub(r'\*\*', '', header)  # Remove asterisks for bold text
            indent = "    " * (level - 1)
            toc.append(f"{indent}- [[#<a id='{id}'></a>{header}|{clean_header}]]")
        
    return "\n".join(toc) + "\n"  # Add an empty line after the TOC

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python headers.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    insert_ids(filename)
    
    toc = generate_toc(filename)
    
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(toc)
        file.writelines(lines)
    
    print("Success!")
