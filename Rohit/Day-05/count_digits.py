def count_digits(n):
    count = 0
    if n<10:
        return 1
    
    count += count_digits(n//10) + 1
    return count
    
print(count_digits(40947777))