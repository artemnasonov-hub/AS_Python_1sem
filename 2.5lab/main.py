if __name__ == "__main__":
    pass



calls = 0
def C(m, n):
    global calls
    calls += 1
    if m == 0 or m == n:
        return 1
    return C(m, n - 1) + C(m - 1, n - 1)
n = 100
for m in range(200):
    calls = 0
    print("C(", m, ",", n, ") =", C(m, n))
    print("Вызовов:", calls)
