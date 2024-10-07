def vvod_ch(e):
    while True:
        try:
            ch = float(input(e))
            return ch
        except ValueError:
            print("Ошибка: введите числовое значение.")

ch1 = vvod_ch("Введите первое число: ")
ch2 = vvod_ch("Введите второе число: ")

summ = ch1 + ch2
raz = ch1 - ch2
proiz = ch1 * ch2
arif = summ / 2

mod1 = ch1 if ch1 >= 0 else -ch1
mod2 = ch2 if ch2 >= 0 else -ch2

max = mod1
min = mod2

if mod2 > mod1:
    max = mod2
    min = mod1
else: max = mod1; min =mod2

razmaxmin = max - min

print("сумма:", summ)
print("Разность:", raz)
print("Произведение:", proiz)
print("Среднее арифметическое:", arif)
print("Разность максимального и минимального по модулю:", razmaxmin)