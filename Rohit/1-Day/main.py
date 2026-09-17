import dis
from helper import add
op = add(9,9)
dis.dis(add)
print(op)