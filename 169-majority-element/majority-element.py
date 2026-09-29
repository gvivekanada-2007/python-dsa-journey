class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dici ={}
        for i in nums:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]=dici[i]+1
        long = len(nums)//2
        for i in dici:
            if dici[i]>long:
                return i