import os
import requests  # We are just importing this to prove the dependency installed correctly

def main():
    version_file_name = os.environ["INPUT_VERSIONFILENAME"]
    print(f'version updated!! in file {version_file_name}')
    version_number_encapsulate_text = os.environ["INPUT_VERSIONNUMBERENCAPSULATETEXT"]
    print(f'version updated!! in file {version_number_encapsulate_text}')

def ReadAndUpdateVersionFile():

    file_name = os.environ["INPUT_VERSIONFILENAME"]
    version_number_encapsulate_text = os.environ["INPUT_VERSIONNUMBERENCAPSULATETEXT"]

    with open(file_name, "r") as read_file:
        version_file_lines = read_file.readlines()
    bump_line = version_file_lines[1]
    print(f'bump={bump_line}')
    split_bump_line = bump_line.split('\"')
    print(f'splitbump={split_bump_line}')
    print(f'bump={bool(int(split_bump_line[1]))}')
    bool_bump = bool(int(split_bump_line[1]))
    
    if bool_bump:
        split_bump_line[1] = '0'
        sep = '\"'
        join_bump_line = sep.join(split_bump_line)
        print(f'joinbump={join_bump_line}')
        version_file_lines[1] = join_bump_line

    version_line = version_file_lines[0]
    split_version_line = version_line.split(version_number_encapsulate_text)
    print(split_version_line)
    version_text = split_version_line[1]
    version_number = version_text.split('.')
    print(f'version_number={version_number}')
    if bool_bump:
        version_number[-2] = str(int(version_number[-2]) + 1)
        version_number[-1] = str(int(0))
    else:
        version_number[-1] = str(int(version_number[-1]) + 1)
    sep = '.'
    join_version_number = sep.join(version_number)
    print(f'join_version_number = {join_version_number}')
    split_version_line[1]=join_version_number
    sep = version_number_encapsulate_text
    join_version_line = sep.join(split_version_line)
    version_file_lines[0] = join_version_line
    print(f'version_file_lines{version_file_lines}')
    # and write everything back
    with open(file_name, 'w') as file:
        file.writelines(version_file_lines)

if __name__ == "__main__":
    main()
    ReadAndUpdateVersionFile(version_file_path)

