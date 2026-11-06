class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dupes = {}

        for i in range(len(nums)):
            remainder = target - nums[i]

            if remainder in dupes:
                return [dupes[remainder], i]
            dupes[nums[i]] = i
        return []

        