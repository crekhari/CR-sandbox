nums = [1,2,3,4]
res = []

prefix = 1
res = [1] * len(nums)
for x in range(len(nums)):
    res[x] *= prefix
    prefix *= nums[x]
suffix = 1
for x in range(len(nums) - 1, -1, -1):
    res[x] *= suffix
    suffix *= nums[x]
print(res)