class Solution:
    def containsNearbyDuplicate(self, nums, k):
        window = set()

        for i in range(len(nums)):
            if nums[i] in window:
                return True

            window.add(nums[i])

            if i >= k:
                window.remove(nums[i - k])

        return False
#Time Complexity:O(n), Space Complexity:O(k)
