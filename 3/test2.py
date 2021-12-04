import unittest
import sys

target = __import__("diag.py")

class TestSolution(unittest.TestCase):

    def test_solution_1(self):
        filename = "test-input.txt"
        with open(filename) as f:
            lines = f.read()
            indata = lines.splitlines()
        outdata = 230
        result = target.solution(indata)
        self.assertEqual(result, outdata, 'Result is {} and should be {}'.format(result,outdata))

    def test_solution_2(self):
        filename = "input.txt"
        with open(filename) as f:
            lines = f.read()
            indata = lines.splitlines()
        outdata = 1
        result = target.solution(indata)
        self.assertEqual(result, outdata, "Result is {} and should be '{}'".format(result,outdata))

if __name__ == "__main__":
    unittest.main()
