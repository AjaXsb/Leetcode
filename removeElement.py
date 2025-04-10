nums = [3,2,2,3]
val = 3
i = 0
count = 0

while i < len(nums):
    if nums[i] == val:
        del nums[i]
    else:
        count += 1
        i += 1

print(count)
print(nums)