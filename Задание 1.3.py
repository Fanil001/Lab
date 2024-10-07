import math
def vvod_ch(e):
    while True:
        try:
            zh = float(input(e))
            return zh
        except ValueError:
            print("Ошибка: введите числовое значение.")

def plkrug(радиус):
    return math.pi * (радиус ** 2)

r1 = vvod_ch("Введите радиус первого круга: ")
r2 = vvod_ch("Введите радиус второго круга: ")

pl1 = plkrug(r1)
pl2 = plkrug(r2)

if pl1 > pl2:
    max_pl = 1
    raz_pl = pl1 - pl2
else:
    max_pl = 2
    raz_pl = pl2 - pl1

print(f"Круг с номером {max_pl} имеет наибольшую площадь.")
print(f"Разность площадей кругов составляет {raz_pl:.2f}.")