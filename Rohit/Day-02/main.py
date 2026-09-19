import sys

print(f"Integer Takes {sys.getsizeof(0)} bytes")

print(f"Empty String Takes {sys.getsizeof("")} bytes")

print(f"Floating Takes {sys.getsizeof(5.0)} bytes")

print(f"Boolean Takes {sys.getsizeof(True)} bytes")
print(f"Boolean Takes {sys.getsizeof(False)} bytes")

print(f"None Takes {sys.getsizeof(None)} bytes")

strings = ["","a","Hello","Hi,I am rohit!"]
for s in strings:
    display = s if len(s)<=40 else s[:37] + "..."
    print(f"'{display}'")
    print(f"Length {len(s)} characters, Size: {sys.getsizeof(s)} bytes")

for count in [0, 1, 2, 3, 5, 10, 20, 50, 100]:
    my_list = list(range(count))
    print(f"list with {count:<3} items: {sys.getsizeof(my_list):<5} bytes")

my_dict = {"a":1,
           "b":"rohit",
           "c":"deep",
           "d":1.2,
           "e":True,
           }
print(sys.getsizeof(my_dict))

set_ex = {1,1,1,22,3,4,65,75,1}
print(sys.getsizeof(set_ex))