nums =[1,1,1,2,2,3]
k = 2
d = {}
for num in nums:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1
arr = []
for key, value in d.items():
    arr.append([value, key])
arr.sort()
res = []
while len(res) < k:
    res.append(arr.pop()[1])
print(res)