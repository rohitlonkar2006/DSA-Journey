def second_largest(nums):
    first = 0
    second = 0
    
    for x in nums:
        if x > first:
            second = first
            first = x
        elif x > second and x != first:
            second = x
            
    return second

obj = nums([1,2,3,4,5,3])
print("Second Largest:",obj)