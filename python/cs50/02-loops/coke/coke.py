paid = 0
coin = 0

while True:
    if paid < 50:
        while True:
            print("Amount Due:", 50 - paid)
            coin = int(input("Insert Coin: "))
            if coin in [5, 10, 25]:
                paid += coin
                break
            else:
                continue 
    else:
        break

print("Change Due:", paid - 50)
