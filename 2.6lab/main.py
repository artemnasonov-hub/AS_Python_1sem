if __name__ == "__main__":
    pass




pi = 3.14
#корень из двух примерно - 1.414
def circle_area(r):
    return pi * r * r

def circle_length(r):
    return 2 * pi * r

def sector_area(r, angle):
    return pi * r * r * angle / 360
def square_perimeter(r):
    a = (2 * r) / 1.414
    return 4 * a

radius = 5
angle = 90

print("Радиус круга:", radius)
print("Площадь круга:", circle_area(radius))
print("Длина окружности:", circle_length(radius))
print("Площадь сектора:", sector_area(radius, angle))
print("Периметр вписанного квадрата:", square_perimeter(radius))

