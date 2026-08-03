class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsmap = {}
        for i in range(len(nums)):
            z = target - nums[i]
            if numsmap.get(z) is not None:
                return sorted([i,numsmap.get(z)])
            else:
                numsmap[nums[i]] = i
        return nums