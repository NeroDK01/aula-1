a = float(input("qual seu numero: "))
b = float(input("qual seu numero: "))
c = float(input("qual seu numero: "))

delta = (b*b) -  (4 * a * c)

x1 = (-b - (delta / 2 * a)) / 2 * a
x2 = (-b + (delta / 2 * a)) / 2 * a

print("x1 = ", x1, "x2 = ", x2)