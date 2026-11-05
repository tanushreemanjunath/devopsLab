import unittest

class TestApplication(unittest.TestCase):

    def test_application(self):
        name = "VVCE"
        self.assertEqual(name, "VVCE")

    def test_department(self):
        department = "CSE"
        self.assertEqual(department, "CSE")

if __name__ == "__main__":
    unittest.main()
