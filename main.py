mas = [43.299, 43.091, 42.562, 43.909, 42.743, 41.839, 41.850, 41.679, 41.518, 43.111, 43.418, 45.830, 46.445, 47.314,
       47.755, 46.218, 47.156, 46.465, 47.554, 50.684, 50.797, 50.437, 50.815, 50.812, 48.626, 48.923, 46.898]
le = len(mas)
min_price = mas[1]
for n in range(1, le):
    if min_price > mas[n]:
        min_price = mas[n]
max_price = mas[1]
for n in range(1, le):
    if max_price < mas[n]:
        max_price = mas[n]
print(min_price, 'min_price')
print(max_price, 'max_price')
buy_price = min_price + 3
sell_prise = max_price - 3

#test
profit = []
for m in range(10, 1000):
    money = 1000
    print(money, 'денег в начале')
    btc = 0
    for n in range(1, le):
        if mas[n] <= buy_price and money >= m:
            money -= m
            btc += m / mas[n]
            print('покупка по курсу', mas[n])
            print('денег', money)
            print('битка', btc)
        if mas[n] >= sell_prise:
            money += btc*mas[n]
            btc = 0
            print('продажа по курсу', mas[n])
            print('денег', money)
            print('битка', btc)
    print(money, 'profit')
    profit.append(money)
max_profit = profit[1]
for n in range(1, len(profit)):
    if max_profit < profit[n]:
        max_profit = profit[n]
        best_sum = + m
print(max_profit, 'max_profit')
print(best_sum, 'best_sum')
