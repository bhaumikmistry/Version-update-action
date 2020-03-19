import os

class VersionUpdate():

    def __init__(self):
        # os.environ["INPUT_VERSIONFILENAME"] = str("version.js")
        # os.environ["INPUT_VERSIONNUMBERENCAPSULATETEXT"] = str("*")
        self.version_file_name = os.environ.get("INPUT_VERSIONFILENAME",str(""))
        self.version_number_encapsulate_text = os.environ.get("INPUT_VERSIONNUMBERENCAPSULATETEXT",str(""))

    def check_arguments(self) -> [bool,str]:
        if self.version_file_name == "":
            return [False,"ERROR: No version file name provided!"]
        else:
            if self.version_number_encapsulate_text == "":
                return [False,"ERROR: No Text for version encapsulate text provided!!"]
            else:
                return [True,"Text for version encapsulate text provided > "+self.version_number_encapsulate_text + " Version file name provided > "+self.version_file_name]
        
    def validate_file(self) -> [bool,str]:
        if not os.path.isfile(self.version_file_name):
            return [False,"Error: Version File Does Not exists!!"] 
        with open(self.version_file_name) as f:
            found_version = False
            for line in f.readlines():
                if line.count(self.version_number_encapsulate_text) == 2:
                    if line.lower().find("version") != -1:
                        found_version = True
                    else:
                        line = line[:-1] if line.endswith("\n") else line
                        # print("Line must have \'version=\' text.")
                        # print(f"line: {line}")   
                        # return [found_version,"Line must have \'version\' text"]
                elif line.count(self.version_number_encapsulate_text) > 2 or \
                    line.count(self.version_number_encapsulate_text) != 0:
                    # print(f'Odd encapsulate text found!!')
                    line = line[:-1] if line.endswith("\n") else line
                    # print(f'line: {line}')
                    #return [found_version,"Line must have \'version=\' text"]
                if found_version:
                    return [found_version,"Version Text Found"]
            return [found_version,"Version Text not found"]
    
    def update_version_in_file(self):
        with open(self.version_file_name, "r") as read_file:
            version_file_lines = read_file.readlines()

        for index,line in enumerate(version_file_lines):
            if line.count(self.version_number_encapsulate_text) == 2:
                if line.lower().find("version") != -1:
                    break

        version_line = version_file_lines[index]
        split_version_line = version_line.split(self.version_number_encapsulate_text)
        print(split_version_line)

        #Assuming the version is between encapsulate text
        version_text = split_version_line[1]

        #Assuming the version is split with '.'
        version_sep = '.'

        # check if what we found between encapsulate text is a version number
        if version_text.count(version_sep)==0:
            print("ERROR:Could not read version between the encapsulated text")
            print("line: {version_text}")
            return False

        version_number = version_text.split(version_sep)
        print(f'version_number={version_number}')

        # Check if the version is all numbers
        for item in version_number:
            if item.isdigit():
                continue
            else:
                print('ERROR: version is not numeric')
                print(f"line: {version_number}")
                return False

        # Later if implemented
        bool_bump = False
        if bool_bump and len(version_number)>=2:
            version_number[-2] = str(int(version_number[-2]) + 1)
            version_number[-1] = str(int(0))
        else:
            version_number[-1] = str(int(version_number[-1]) + 1)

        join_version_number = version_sep.join(version_number)
        print(f'join_version_number = {join_version_number}')

        split_version_line[1]=join_version_number
        sep = self.version_number_encapsulate_text

        join_version_line = sep.join(split_version_line)
        version_file_lines[index] = join_version_line

        print(f'Version_file_lines :-')
        print('-'*30)
        for line in version_file_lines:
            print(line,end="")
        print()
        print('-'*30)
        # and write everything back
        with open(self.version_file_name, 'w') as file:
            file.writelines(version_file_lines)
        return True

    def run(self):
        res = self.check_arguments()
        print(res[1])
        res = res[0]
        if res:
            res = self.validate_file()
        if res:
            res = self.update_version_in_file()
        return res

if __name__ == "__main__":
    v = VersionUpdate()
    v.run()