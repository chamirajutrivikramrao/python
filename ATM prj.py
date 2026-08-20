print("Welcome to the ATM")
card=int(input("insert the card:"))
balance=10000
if card==1:
    lang=int(input("select the languge1.english: 2.telugu"))
    if lang==1:
        print("enter the pin")
        pin=int(input())
        if pin==1234:
            print("select the choose 1.withdraw 2.balance 3.deposit")
            option=int(input("choose the option:"))
            if option==1:
                amt=int(input("enter the amount:"))
                if balance>=amt:
                    print("balance",balance-amt)
                    print("thanks for visiting")
                else:
                    print("insufficiant balance")
            elif option==2:
                print("balance",balance)
                print("thanks for visiting")
            else:
                deposit=int(input("put th amount:"))
                print("balance",balance+deposit)
                print("thanks for visiting")
        else:
            print("wrong pin entered")
    else:
        print("choose correct option")
else:
    print("insert card correctly")
