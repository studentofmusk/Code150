from typing import List
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr = [0, 0, 0]
        for each in triplets:
            if (
                    each[0] > target[0] or
                    each[1] > target[1] or
                    each[2] > target[2]
            ):
                continue
            curr = [max(curr[0], each[0]), max(curr[1], each[1]), max(curr[2], each[2])]
            if curr == target:
                return True
        return False

print(Solution().mergeTriplets(triplets = [[1,2,3],[7,1,1]], target = [7,2,3]))
print(Solution().mergeTriplets(triplets = [[2,5,6],[1,4,4],[5,7,5]], target = [5,4,6]))

# Merge Triplets to Form Target
# You are given a 2D array of integers triplets, where triplets[i] = [ai, bi, ci] represents the ith triplet. You are also given an array of integers target = [x, y, z] which is the triplet we want to obtain.
#
# To obtain target, you may apply the following operation on triplets zero or more times:
#
# Choose two different triplets triplets[i] and triplets[j] and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
# * E.g. if triplets[i] = [1, 3, 1] and triplets[j] = [2, 1, 2], triplets[j] will be updated to [max(1, 2), max(3, 1), max(1, 2)] = [2, 3, 2].
#
# Return true if it is possible to obtain target as an element of triplets, or false otherwise.
#
# Example 1:
#
# Input: triplets = [[1,2,3],[7,1,1]], target = [7,2,3]
#
# Output: true
# Explanation:
# Choose the first and second triplets, update the second triplet to be [max(1, 7), max(2, 1), max(3, 1)] = [7, 2, 3].
#
# Example 2:
#
# Input: triplets = [[2,5,6],[1,4,4],[5,7,5]], target = [5,4,6]
#
# Output: false
# Constraints:
#
# 1 <= triplets.length <= 1000
# 1 <= ai, bi, ci, x, y, z <= 100
