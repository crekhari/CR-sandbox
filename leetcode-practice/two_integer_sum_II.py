numbers=[1,2,3,4]
target=3
def twoSumSorted(numbers, target):
    left_pointer = 0
    right_pointer = len(numbers) - 1

    while left_pointer < right_pointer:
        summy = numbers[left_pointer] + numbers[right_pointer]
        if summy > target:
            right_pointer-=1
        elif summy < target:
            left_pointer+=1
        else:
            return [left_pointer+1, right_pointer+1]
print(twoSumSorted(numbers,target))