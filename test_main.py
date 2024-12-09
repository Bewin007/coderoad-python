import unittest
from io import StringIO
import sys

class TestPrint(unittest.TestCase):
    def test_print(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        # Call the function to test print
        exec(open('main.py').read())
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()
