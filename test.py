import unittest
import os
from version_update import VersionUpdate

class TestMain(unittest.TestCase):

    def set_up_env(self,file_name,encapsulate_text):
        os.environ["INPUT_VERSIONFILENAME"] = str(file_name)
        os.environ["INPUT_VERSIONNUMBERENCAPSULATETEXT"] = str(encapsulate_text)

    def test_version_filename(self):
        self.set_up_env("version.js","*")
        self.assertEqual(os.environ["INPUT_VERSIONFILENAME"],"version.js")
        self.assertEqual(os.environ["INPUT_VERSIONNUMBERENCAPSULATETEXT"],"*")
        v = VersionUpdate()
        self.assertTrue(v.run())

    def test_version_filename_2(self):
        self.set_up_env("version.js","*")
        self.assertEqual(os.environ["INPUT_VERSIONFILENAME"],"version.js")
        self.assertEqual(os.environ["INPUT_VERSIONNUMBERENCAPSULATETEXT"],"*")


if __name__ == "__main__":
    unittest.main()
