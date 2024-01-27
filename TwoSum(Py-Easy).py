class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        f = 0;
        x = len(nums)-1
        for i in range (x):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]== target):
                    return [i,j]
        
