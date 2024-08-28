class Solution(object):
    def containsDuplicate(self, nums):
        return (len(nums) > len(set(nums)))


nums = [1,2,3,1]
solution = Solution()
result = solution.containsDuplicate(nums)