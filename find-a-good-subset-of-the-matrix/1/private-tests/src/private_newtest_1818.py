
import solution

def test_1818():
	assert solution.Solution().goodSubsetofBinaryMatrix([[0, 1, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1], [1, 0, 0, 1, 0, 1, 0], [0, 1, 0, 0, 1, 1, 0]]) == [1, 5]
