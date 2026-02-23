num1 = float(input("qual sua nota: "))
num2 = float(input("qual sua nota: "))
num3 = float(input("qual sua nota: "))

media = num1 + num2 + num3 

print("Sua media e: ", media / 3)

if media >= 70:
    print("voce foi aprovado: ")
else:
    print("voce foi reprovado")