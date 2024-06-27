import re
import sys
import os
from collections import defaultdict
import subprocess

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
        
        match = re.match(r'(#+) <a id=\'(\d+)\'></a>(.*)', line)
        if match:
            header_level = len(match.group(1))
            id = match.group(2)
            header = match.group(3).strip()
            id_counter[header] = int(id)  # Use the existing ID
        elif line.startswith('#'):
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
        
    return "\n".join(toc) + "\n\n"  # Add an empty line after the TOC

def check_execution_policy():
    result = subprocess.run(['powershell', '-Command', 'Get-ExecutionPolicy'], capture_output=True, text=True)
    policy = result.stdout.strip()
    return policy

def set_execution_policy():
    print("The current execution policy is restrictive. This script requires a less restrictive policy to add paths.\n")
    choice = input("Would you like to change the execution policy to 'RemoteSigned'? [Y/N]: ").strip().lower()
    if choice == 'y':
        subprocess.run(['powershell', '-Command', 'Set-ExecutionPolicy RemoteSigned -Scope CurrentUser'])
        print("\nExecution policy set to 'RemoteSigned'. Please restart the script.")
        sys.exit(0)
    else:
        print("\nCannot proceed without changing the execution policy. Exiting.")
        sys.exit(1)

def add_to_path(script_dir):
    path = os.environ.get('PATH', '')
    path_elements = path.split(os.pathsep)
    if script_dir in path_elements:
        print(f"The script directory '{script_dir}' is already stored in the PATH variable.")
        return True
    
    print(f"\nThe script directory '{script_dir}' is not in the PATH.")
    choice = input("Would you like to add it to the PATH? [Y/N]: ").strip().lower()
    if choice == 'y':
        admin_check = input("Do you have administrator privileges? [Y/N]: ").strip().lower()
        if admin_check != 'y':
            print("\nPlease restart the script with administrator privileges enabled.")
            sys.exit(1)
        new_path = f"{path};{script_dir}"
        if len(new_path) > 1024:
            print("\n\033[1;31mWARNING: Adding this path will exceed the maximum PATH length and may cause truncation.\033[0m")
        result = subprocess.run(['powershell', '-Command', f'[System.Environment]::SetEnvironmentVariable("PATH", "{new_path}", "Machine")'])
        if result.returncode == 0:
            print(f"\n\033[1;32mPath added successfully: {script_dir}\033[0m\n")
            print("\033[1;33mWarning: If you change the location of the original script file, you will need to update the PATH manually.\033[0m\n")
            print("To remove the script directory from the PATH, use the following command in PowerShell:\n")
            print("  * [System.Environment]::SetEnvironmentVariable(\"PATH\", $env:PATH -replace \";{script_dir}\", \"\", \"Machine\")\n")
            print("To manually add a new path, use:\n")
            print("  * [System.Environment]::SetEnvironmentVariable(\"PATH\", \"$env:PATH;<new_path>\", \"Machine\")\n")
            return True
        else:
            print("\033[1;31mFailed to add the path. Ensure you have the necessary permissions.\033[0m")
            return False
    else:
        print("\nThe script directory was not added to the PATH.")
        print("Note: If the file wasn't added to the PATH, you need to be in the same directory as the script to execute it.")
        return False

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if not add_to_path(script_dir):
        sys.exit(1)

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
    
    print(f"Success! Automatic TOC generated using {filename}")
