# Программа, которая считает скорость света в определенной среде
# и выводит результат в метрах в секунду

n = float(input("Введите показатель преломления среды: "))

if n < 1:
    print("Показатель преломления не может быть меньше 1")
else:
    c = 299792458 # скорость света в вакууме
    v = c / n
    print("Скорость света в среде с показателем преломления", n, "равна", v, "м/с")
