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

obj = second_largest([4,4,3])
print("Second Largest:",obj)
