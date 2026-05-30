import java.util.*;//To use collections import this package

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int complement = target - num;

            if (map.containsKey(complement)) {
                return new int[]{map.get(complement), i};
            }

            map.put(num, i);
        }

        return new int[]{-1, -1};
    }
}//Complexity: Time->O(n),Space->O(n) as we are using hashmap storing upto n elements
