def add(x, y, f):
    return f(x) + f(y)

print(add(-9, -1, abs))