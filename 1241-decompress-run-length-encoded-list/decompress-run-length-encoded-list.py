class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        
    
        ans=[]
        i=0
        while i<len(nums):
            s=nums[i]
            k=nums[i+1]
            for j in range(nums[i]):
                ans.append(nums[i+1])
            i=i+2
        return ans



