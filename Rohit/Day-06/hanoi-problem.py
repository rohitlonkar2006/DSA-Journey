def hanoi(n, source, spare, target):
    if n == 0:
        return

    hanoi(n-1, source, target, spare)

    print(f"Moved {n} from {source} ---> {target}")

    hanoi(n-1, spare, source, target)


hanoi(30, "A", "B", "C")