def subsets(nums, i, path, result):
    if i == len(nums):
        result.append(path[:])
        return
    
    path.append(nums[i]) #Including The Element
    subsets(nums, i+1, path, result)
    
    path.pop() #Excluding The Element
    subsets(nums, i+1, path, result)
    
result = []
path = []
i = 0
nums = [1, 2, 3]
subsets(nums, i, path, result)

print(result)