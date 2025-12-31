nums=[4,1,-1,2,-1,2,3]
k=2
# d = {}
# for num in nums:
#     if num in d:
#         d[num] += 1
#     else:
#         d[num] = 1
# arr = []
# for key, value in d.items():
#     arr.append([value, key])
# arr.sort()
# res = []
# while len(res) < k:
#     res.append(arr.pop()[1])
# print(res)


count_dict = {}
if k == len(nums):
    print(nums)
# key: value
for num in nums:
    if num in count_dict:
        count_dict[num] +=1
    else:
        count_dict[num] = 1
inverse_count_dict = {}
for num, count in count_dict.items():
    if count in inverse_count_dict:
        inverse_count_dict[count].append(num)
    else:
        inverse_count_dict[count] = [num]
res = []
print(inverse_count_dict)
for count in range(len(nums), 0, -1):
    if count in inverse_count_dict:
        res.extend(inverse_count_dict[count])
    if len(res) == k:
        break
print(res)
