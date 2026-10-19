class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = []

        for n in nums:
            if n in dupes:
                return True
            dupes.append(n)

        return False
