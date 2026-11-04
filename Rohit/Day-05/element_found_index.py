# Consider One Index And Find The Give Element In That List Weather It Exists or not if exists then return its index if not return -1

def element_found(data):
    found = -1
    target = 6
    for i in data:
        if i == target:
            found = data.index(i)
            return found

e = element_found([1,2,3,3,2,6])
print("Element Found At",e,"Position")