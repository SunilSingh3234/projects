print("welcome to BYD bank \nPlease Insert your card...")
password=7890
balance=999999
choice=0
pin=int(input("Enter your password"))
if(pin==password):
    while(choice !=4):
        print("\n __Menu__")
        print("1==balance")
        print("2==deposite")
        print("3==withdraw")
        print("4==cancel\n")
        
        choice=int(input("\n Enter u r option:"))
        
        if(choice==1):
            print("Balance=usd",balance)
        
        elif(choice==2):
            deposite=int(input("enter your deposite:usd"))
            balance+=deposite
            print("\ndeposite amount:use",deposite)
            
            print("Total balance=usd",balance)
        elif(choice==3):
            withdraw=int(input("Enter the amount to withdraw:usd"))
            balance-=withdraw
            print("\nwithdraw amount: usd", withdraw)
            print("total balance=usd",balance)
        elif(choice==4):
            print("\n session Ended Bro !!!!")
else:
    print("wrong password try again..!!")