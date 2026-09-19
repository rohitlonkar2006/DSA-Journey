import sys

# print(f"Integer Takes {sys.getsizeof(0)} bytes")

# print(f"Empty String Takes {sys.getsizeof("")} bytes")

# print(f"Floating Takes {sys.getsizeof(5.0)} bytes")

# print(f"Boolean Takes {sys.getsizeof(True)} bytes")
# print(f"Boolean Takes {sys.getsizeof(False)} bytes")

# print(f"None Takes {sys.getsizeof(None)} bytes")

strings = ["","a","Hello","Hi,I am rohit!"]
for s in strings:
    display = s if len(s)<=40 else s[:37] + "..."
    print(f"'{display}'")
    print(f"Length {len(s)} characters, Size: {sys.getsizeof(s)} bytes")