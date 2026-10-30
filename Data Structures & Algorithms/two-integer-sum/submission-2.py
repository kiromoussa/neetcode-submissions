class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, number in enumerate(nums): 
            j= target - number
            try: 
                end = nums.index(j, i + 1)
                return [i, end] 
            except:
                pass
