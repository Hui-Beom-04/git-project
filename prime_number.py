number = int (input())

prime = True

if number == 1:
    prime = True
else:
    for i in range(2, number):
        if number % i == 0:
            prime = False
        

if prime:
    print("소수입니다.")
else:
    print("소수가 아닙니다.")

