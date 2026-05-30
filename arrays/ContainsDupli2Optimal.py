class Solution:
    def containsNearbyDuplicate(self, nums, k):
        lastIndex = {}

        for i in range(len(nums)):
            if nums[i] in lastIndex and i - lastIndex[nums[i]] <= k:
                return True
            lastIndex[nums[i]] = i

        return False
