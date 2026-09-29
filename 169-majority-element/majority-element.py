class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        nums.sort()
        temp=len(nums)//2
        return(nums[temp])