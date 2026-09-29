class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        
        temp=list(set(nums1))
        
        for i in range(len(temp)):
            for j in range(len(nums2)):
                if temp[i]==nums2[j]:
                    ans.append(nums2[j])
                    break
        return ans