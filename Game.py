print(".....Welcome to my GameZone.....")
Balance=int(input("Enter your balance:"))
con=1

while con==1:
    choice=int(input("Select your choice 1 for bowling:300\n 2 for chess:250\n 3 for ludo:400\n 4 for riding:500\n "))

    if choice==1:
        price=300
    elif choice==2:
        price=250
    elif choice==3:
        price=400
    elif choice==4:
        price=500
    if Balance>=price:
        print("Now you can play this game...")
        Balance -=price
        print("Your current Balance is:",Balance)
    else:
        print("Please top-up your balance...")
        print("If you want to top-up your balance than press 1 other for exit")
        top=int(input( ))
        if top==1:
            amount=int(input("Enter your remaing amount: "))
            Balance+=amount
            print("Your Balance is:",Balance)
    con=int(input("Do you want to continue your game? If yes then press 1 or other for exit"))

    