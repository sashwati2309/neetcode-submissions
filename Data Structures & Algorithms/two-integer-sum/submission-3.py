class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsmap = {}
        for i in range(len(nums)):
            z = target - nums[i]
            if numsmap.get(z) is not None and numsmap.get(z) != i:
                return [numsmap.get(z),i]
            else:
                numsmap[nums[i]] = i
        return []