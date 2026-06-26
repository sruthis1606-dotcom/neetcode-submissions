class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for i in s:
            if i-1 not in s:
                length = 1
                while i+1 in s:

                   i+=1
                   length+=1
                ans = max(ans, length)
        return ans

