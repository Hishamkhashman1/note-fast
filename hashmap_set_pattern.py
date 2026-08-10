nums = [2,7,11,15]
target = 9

def solution_1(nums, target):

    for i in range (len(nums)):
        for j in range (i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i,j
    return None

print (solution_1(nums, target))

def solution_2(nums, target):
    seen = {}

    for i, n in enumerate(nums):
        needed = target - n

        if needed in seen:
            return seen[needed], i

        seen[n] = i

    return None

print (solution_2(nums, target))
