class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsmap = {}
        for i in range(len(nums)):
            if numsmap.get(nums[i]) is not None:
                return True
            else:
                numsmap[nums[i]] = True
        return False