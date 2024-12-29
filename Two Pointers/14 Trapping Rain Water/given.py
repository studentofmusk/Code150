from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l, r = 0, len(height)-1

        res = 0
        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

solution = Solution()
print(solution.trap([3,1,0,1,3]))
print(solution.trap([0,2,0,3,1,0,1,3,2,1]))
