class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store_num = {}

        for i in range(len(nums)):
            rem = target - nums[i]

            if rem in store_num:
                return [store_num[rem], i]

            store_num[nums[i]] = i
        
         