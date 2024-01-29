class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left,right =0,len(height)-1

        while left < right:
            area = (right-left)* min(height[right],height[left])
            ans = max(ans,area)
            if height[right] <= height[left]:
                right -= 1
            else:
                left += 1

        return ans 
