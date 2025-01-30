'''# 1.uzd
summa = 0

for i in range (1, 10):
    if (i/3)==(i//3) or i/5==i//5:
        summa = summa + i
        #print(i)

print(summa)
summa2 = 0

for i in range (1, 1000):
    if (i % 3 ==0) or (i % 5 ==0):
        summa2 = summa2 + i
        #print(i)

print(summa2)

# 2.uzd'''

'''fibonaci = 1
fibonaci2 = 1
summa = 0
while fibonaci2 < 40:
    fibonaci += fibonaci2
    print(fibonaci2)
    if (fibonaci % 2 ==0):
        summa = summa + fibonaci'''


sk1 = 1
sk2 = 2
uzkrajosais = 0

while  sk2<40:
    print(sk2)
    summa = sk1 + sk2
    sk1 = sk2
    sk2 = summa
    if sk2 % 2 == 0:
        uzkrajosais += sk2

print("-----------------")
print(uzkrajosais)

