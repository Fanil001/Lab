
def vvod_ch(e):
    while True:
        try:
            zh = int(input(e))
            return zh
        except ValueError:
            print("Ошибка: введите целочисленное значение.")

im = input("Введите ваше имя: ")
voz = vvod_ch("Введите ваш возраст: ")
nosh= vvod_ch("Введите номер вашей школы: ")
klas = vvod_ch("Какой класс вы окончили? ")

if klas == 11:
    god  = 2024 - voz + 7 + klas
    print(f"Привет, {im}! Поздравляю с окончанием {klas} класса школы № {nosh} в {god } году.")

elif klas == 9:
    god  = 2024 - voz + 7 + klas
    print(f"Привет, {im}! Поздравляю с окончанием {klas} класса школы № {nosh} в {god } году.")
else:
    god = 2024 - voz + 7 + klas
    print(f"Привет, {im}! Поздравляю с окончанием {klas} класса школы № {nosh} в {god} году.")
