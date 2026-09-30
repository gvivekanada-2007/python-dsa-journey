class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        
        ans=[]
        for i in range(0,len(nums),2):
            s=nums[i+1]
            for j in range(nums[i]):
                ans.append(s)
        return ans

