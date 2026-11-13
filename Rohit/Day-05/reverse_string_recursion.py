def reverse_string(n: str):
    if n == "":
        return ""

    return reverse_string(n[1:]) + n[0]


print(reverse_string("code"))