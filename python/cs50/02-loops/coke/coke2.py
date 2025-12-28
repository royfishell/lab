paid = 0

while paid < 50:
    print("Amount Due:", 50 - paid)
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        paid += coin

print("Change Due:", paid - 50)
