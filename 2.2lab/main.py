if __name__ == "__main__":
    pass





def RectPS(x1, y1, x2, y2):
    w = abs(x2 - x1)
    h = abs(y2 - y1)
    P = 2 * (w + h)
    S = w * h
    return P, S


x1 = int(input("Введите x1: "))
y1 = int(input("Введите y1: "))
x2 = int(input("Введите x2: "))
y2 = int(input("Введите y2: "))

perimeter, square = RectPS(x1, y1, x2, y2)

print("Периметр прямоугольника:", perimeter)
print("Площадь прямоугольника:", square)
