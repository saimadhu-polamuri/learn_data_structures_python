__author__ = "saimadhu.polamuri"

"""Given an integer array, find if an integer p exists in the array such that the number of 
    integers greater than p in the array equals to p If such an integer is found return 1 else return -1."""


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        # sort the array
        A.sort()
        array_len = len(A)
        nobel_flag = -1
        for i in range(0, array_len - 1):

            if A[i] == A[i + 1]:
                continue
            if A[i] == array_len - i - 1:
                nobel_flag = 1
        if A[array_len - 1] == 0:
            nobel_flag = 1

        return nobel_flag



