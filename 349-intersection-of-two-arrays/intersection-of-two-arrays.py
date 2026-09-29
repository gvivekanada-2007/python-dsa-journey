class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = set(nums1)
        answer = set()
        for x in nums2:
            if x in seen:
                answer.add(x)
        return list(answer) 