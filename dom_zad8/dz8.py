from random import randint

chisla = []

for i in range(0, 100000000, 10):
    chisla.append(randint(0, 10) + i)

index = randint(0, 10000000)
ishy_chislo = chisla[index]

chislo1 = 0
chislo2 = len(chisla) - 1

while chislo1 <= chislo2:
    number = (chislo1 + chislo2) // 2
    if ishy_chislo == chisla[number]:
        print("Я нашел загаданное число 'Вася' )")
        break
    elif ishy_chislo < chisla[number]:
        chislo2 = number - 1
    else:
        chislo1 = number + 1