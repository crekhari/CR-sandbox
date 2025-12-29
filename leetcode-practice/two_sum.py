from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    from collections import defaultdict
    sum_dict = {}
    for x in range(0, len(nums)):
        diff = target - nums[x]
        if diff in sum_dict:
            return [sum_dict[diff], x]
        else:
            sum_dict[nums[x]] = x
        print(sum_dict)

nums = [3,4,5,6]
target = 7

print(twoSum(nums, target))