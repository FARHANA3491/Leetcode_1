class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            new_target = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == new_target:
                    return[i,j]
        return []
