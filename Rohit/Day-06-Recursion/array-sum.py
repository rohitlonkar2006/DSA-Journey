def total_n(data):
    running = 0
    for item in data:
        if isinstance(item,list):
            running += total_n(item)
        else:
            running += item
    return running

print(total_n([1,[2,3],[4,5],6]))