n = int(input("введите целое положительное число: "))
while n > 0 and isinstance(n, int) :
    s = str(n)
    ls = list(map(int, s))
    r = max(ls)
    print(r, "самое большая цифра")
    break
print(n, "число введеное Вами")

