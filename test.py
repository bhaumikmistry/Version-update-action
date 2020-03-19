import unittest
import os
from version_update import VersionUpdate
import random

class TestMain(unittest.TestCase):

    def set_up_env(self,file_name,encapsulate_text):
        os.environ["INPUT_VERSIONFILENAME"] = str(file_name)
        os.environ["INPUT_VERSIONNUMBERENCAPSULATETEXT"] = str(encapsulate_text)

    def test_set_up_env(self):
        self.set_up_env("version.js","*")
        self.assertEqual(os.environ["INPUT_VERSIONFILENAME"],"version.js")
        self.assertEqual(os.environ["INPUT_VERSIONNUMBERENCAPSULATETEXT"],"*")

    def test_env_variable_set(self):
        file_name = "version.js"
        encapsulate_text = "*"
        self.set_up_env(file_name,encapsulate_text)
        v = VersionUpdate()
        self.assertEqual(v.version_file_name,file_name)
        self.assertEqual(v.version_number_encapsulate_text,encapsulate_text)   

    def test_check_argument_file_error_test(self):
        file_name = ""
        encapsulate_text = ""
        self.set_up_env(file_name,encapsulate_text)
        v = VersionUpdate()
        self.assertFalse(v.check_arguments()[0])
    
    def test_check_argument_encapsulate_test(self):
        file_name = "version.js"
        encapsulate_text = ""
        self.set_up_env(file_name,encapsulate_text)
        v = VersionUpdate()
        self.assertFalse(v.check_arguments()[0])

    def test_check_argument_encapsulate_test(self):
        file_name = "version.js"
        encapsulate_text = "*"
        self.set_up_env(file_name,encapsulate_text)
        v = VersionUpdate()
        self.assertTrue(v.check_arguments()[0])

    def test_check_argument_encapsulate_test(self):
        file_name = "version.js"
        encapsulate_text = "*"
        self.set_up_env(file_name,encapsulate_text)
        v = VersionUpdate()
        self.assertTrue(v.check_arguments()[0])

    def test_file_verification_part_one(self):
        file_name = "version_test_one.js"
        wrong_name = "version_test_bad.js"
        encapsulate_test = "*"
        self.set_up_env(wrong_name,encapsulate_test)
        v = VersionUpdate()
        self.assertFalse(v.validate_file()[0])
    
    def test_file_verification_part_two(self):
        file_name = "version_test_two.js"
        encapsulate_test = "*"
        self.set_up_env(file_name,encapsulate_test)

        version_file_lines = []
        version_file_lines.append("version = *0.0.1*")
        version_file_lines.append("Why did it take so long for the composer to be unambivalently embraced? Maybe because ambivalence is what he’s embraced most of all. ")
        with open(file_name, 'w') as file:
            file.writelines(version_file_lines)
        v = VersionUpdate()
        res = v.validate_file()
        self.assertTrue(res[0],res[1])
        os.remove(file_name)

    def test_file_verification_part_three(self):
        file_name = "version_test_three.js"
        encapsulate_test = "*"
        self.set_up_env(file_name,encapsulate_test)

        version_file_lines = []
        version_file_lines.append("version = **0.0.1*\n")
        version_file_lines.append("Why did it take so long for the composer to be unambivalently embraced? Maybe because ambivalence is what he’s embraced most of all. ")
        with open(file_name, 'w') as file:
            file.writelines(version_file_lines)
        v = VersionUpdate()
        self.assertTrue(v.check_arguments()[0])
        res = v.validate_file()
        self.assertFalse(res[0],res[1])
        os.remove(file_name)

    def test_file_verification_part_four(self):
        file_name = "version_test_four.js"
        encapsulate_test = "*"
        self.set_up_env(file_name,encapsulate_test)
        version_file_lines = []
        version_file_lines.append("**0.0.1*\n")
        version_file_lines.append("Why did it take so long for the composer to be unambivalently embraced? Maybe because ambivalence is what he’s embraced most of all. ")
        with open(file_name, 'w') as file:
            file.writelines(version_file_lines)
        v = VersionUpdate()
        self.assertTrue(v.check_arguments()[0])
        res = v.validate_file()
        self.assertFalse(res[0],msg=res[1])
        os.remove(file_name)

    def test_version_update_call(self):
        file_name = "version_final_test.js"
        encapsulate_test = "*"
        self.set_up_env(file_name,encapsulate_test)
        version_file_lines = []

        x = random.randint(0,10000000)
        y = random.randint(0,10000000)
        z = random.randint(0,10000000)
        version = f"version = *{x}.{y}.{z}*\n"
        print(f"{x}:{y}:{z}:{version}")
        version_file_lines.append(version)
        version_file_lines.append("Why did it take so long for the composer to be unambivalently embraced? Maybe because ambivalence is what he’s embraced most of all. ")
        with open(file_name, 'w') as file:
            file.writelines(version_file_lines)
        v = VersionUpdate()
        self.assertTrue(v.check_arguments()[0])
        res = v.validate_file()
        self.assertTrue(res[0],msg=res[1])
        os.remove(file_name)



if __name__ == "__main__":
    unittest.main()
