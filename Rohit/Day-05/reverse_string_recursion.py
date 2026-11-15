def reverse_string(text: str) -> str:
    """Return the reverse of a string using recursion."""
    if text == "":
        return ""

    return reverse_string(text[1:]) + text[0]


if __name__ == "__main__":
    sample = "code"
    print(f"Original: {sample}")
    print(f"Reversed: {reverse_string(sample)}")