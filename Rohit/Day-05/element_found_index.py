# Consider One Index And Find The Give Element In That List Weather It Exists or not if exists then return its index if not return -1

def element_found(data:list):
    found = -1
    element = 3
    for i in data:
        if i == element:
            found = indexof(i)
            return 
        else:
            return -1

e = element_found([1,2,3,3,2,6])
print("Element Found At:",e)