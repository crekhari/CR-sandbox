nums=[0,3,2,5,4,6,1,1]
set_nums = set(nums)
ret_max = 0
for num in nums:
    ret = 0
    if num-1 not in set_nums:
        while (num in set_nums):
            num+=1
            ret+=1
        ret_max = max(ret,ret_max)