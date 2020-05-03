__author__ = "saimadhu.polamuri"

"""You are given a sequence of points and the order in which you need to cover the points. Give the minimum number 
of steps in which you can achieve it. You start from the first point."""


class Solution:

    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):

        total_steps = 0
        if len(A) == 1:
            return total_steps
        else:
            i = 0
            while i < len(A) -1:

                x_unit_diff = abs(A[i] - A[i + 1])
                y_unit_diff = abs(B[i] - B[i + 1])
                steps = max(x_unit_diff, y_unit_diff)
                total_steps += steps
                i += 1
        return total_steps

test_solution = Solution()

a = [0, 1, 1]
b = [0, 1, 2]

print(test_solution.coverPoints(a,b))