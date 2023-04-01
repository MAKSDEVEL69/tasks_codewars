def score(dice):
    amount1 = [0,0,0,0,0,0,0]
    res = 0
    for i in dice:
        amount1[i] += 1
    print(amount1)
    for i in range(7):
        if (amount1[i]) >= 3:
            if i == 1:
                res += 1000
                amount1[i] = amount1[i] - 3
            else:
                res += i * 100
                amount1[i] = amount1[i] - 3

    res += amount1[1] * 100 + amount1[5] * 50
    return res


score([2, 2, 2, 3, 3])