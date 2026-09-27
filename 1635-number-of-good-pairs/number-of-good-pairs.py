class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        
        k=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    k=k+1
        return k