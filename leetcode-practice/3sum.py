
def threeSum(self, nums):
    res = []
    nums.sort()
    for idx, num in enumerate(nums):
        if num > 0:
            break
        if idx > 0 and num == nums[idx-1]:
            continue
        l = idx + 1
        r = len(nums) - 1 
        while l < r:
            summ = num + nums[l] + nums[r]
            if summ < 0:
                l+=1
            elif summ > 0:
                r-=1
            else:
                res.append([num, nums[l], nums[r]])
                l+=1
                while l < r and nums[l] == nums[l-1]:
                    l+=1
    return res