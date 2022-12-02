import unittest
import solution
from pprint import pprint
import pathlib

class TestSolution(unittest.TestCase):
    
    def test_parse_input(self):
        expected = [["A", "Y"] , ["B", "X"] , ["C", "Z"]]
        curr_dir = pathlib.Path(__file__).parent.resolve()
        actual = solution.parse_input(f"{curr_dir}/test_input.txt")
        self.assertEqual(actual, expected)

    def test_part1(self):
        problem_input = [["A", "Y"] , ["B", "X"] , ["C", "Z"]]
        actual = solution.solve_part1(problem_input)
        expected = 15
        self.assertEqual(actual, expected)


    def test_part2(self):
        problem_input = [["A", "Y"] , ["B", "X"] , ["C", "Z"]]
        actual = solution.solve_part2(problem_input)
        expected = 12
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()