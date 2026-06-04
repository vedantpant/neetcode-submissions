class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        sum_map = {0: 1}
        count = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in sum_map:
                count += sum_map[prefix_sum - k]

            sum_map[prefix_sum] = sum_map.get(prefix_sum, 0) + 1

        return count
        