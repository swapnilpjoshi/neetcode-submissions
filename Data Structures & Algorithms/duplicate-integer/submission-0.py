class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums)
        len_set = len(num_set)
        len_arr = len(nums)
        if len_set<len_arr:
            return True
        return False
        