import os
import requests  # We are just importing this to prove the dependency installed correctly


def main():
    version_file_name = os.environ["INPUT_VERSIONFILENAME"]
    print(f'version updated!! in file {version_file_name}')
    version_number_encapsulate_text = os.environ["INPUT_VERSIONNUMBERENCAPSULATETEXT"]
    print(f'version updated!! in file {version_number_encapsulate_text}')

if __name__ == "__main__":
    main()
