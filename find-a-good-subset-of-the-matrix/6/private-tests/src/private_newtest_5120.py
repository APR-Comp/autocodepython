
import solution

def test_5120():
	assert solution.Solution().goodSubsetofBinaryMatrix([[0, 0, 1, 1, 0, 0, 0], [1, 0, 0, 1, 0, 0, 1], [0, 0, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1]]) == [0, 3]
