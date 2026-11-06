class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_dups = []

        for n in nums:
            if n in has_dups:
                return True
            has_dups.append(n)
        
        return False
        