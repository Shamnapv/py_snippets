atm_pin=int(input("Set your 4-digit ATM pin:"))
balance=int(input("Enter your current balance:"))
for i in range(0,3):
    enter_pin=int(input("Enter your 4-digit  ATM pin"))
    if atm_pin == enter_pin:
        print("Access granted")
        break
    else:
        print(f"Incorrect pin . Attempt left : {2 - i}")
else:
    print("Too many attempts exiting...")
    exit()
while True:
    print("===== ATM MENU =======")
    print("1-Check balance")
    print("2-Withdraw money")
    print("3-Deposit money")
    print("4-Change ATM pin")
    print("5-Exit")
    choice=input("Enter your choice:")
    if choice== "1":
        print(f"Your balance is : {balance}")
    elif choice== "2":
        amount=int(input("Enter the amount to  withdraw:"))
        if amount<=0:
            print("Invalid amount try again")
            continue
        if amount > balance:
            print("Insufficient balance!")
            continue
        balance -= amount
        print("Withdrawal successful !")
    elif choice=="3":
        amount=int(input("Enter the amount to  deposit:"))
        if amount <= 0:
            print("Invalid amount try again!")
            continue
        balance+=amount
        print("Deposited successfully!")
    elif choice=="4":
        current_pin=int(input("Enter your current pin:"))
        if current_pin==atm_pin:
            new_pin=input("Enter 4-digit ATM pin:")
            if len(new_pin)==4 and new_pin.isdigit():
                atm_pin=int(new_pin)
            else:
                print("Invalid new pin ,Must be 4-digit")
        else:
            print("Invalid current pin ")

    elif choice=="5":
        print("Thank you for using the ATM Bye")
        break
    else:
        print("Invalid choice.please enter a number between 1 and 5")
"""output:
(base) PS C:\Users\shaim\Desktop\pythonlab> python task5.py
Set your 4-digit ATM pin:1234
Enter your current balance:2000
Enter your 4-digit  ATM pin1234
Access granted
===== ATM MENU =======
1-Check balance
2-Withdraw money
3-Deposit money
4-Change ATM pin
5-Exit
Enter your choice:1
Your balance is : 2000
===== ATM MENU =======
1-Check balance
2-Withdraw money
3-Deposit money
4-Change ATM pin
5-Exit
Enter your choice:2
Enter the amount to  withdraw:200
Withdrawal successful !
===== ATM MENU =======
1-Check balance
2-Withdraw money
3-Deposit money
4-Change ATM pin
5-Exit
Enter your choice:3
Enter the amount to  deposit:400
Deposited successfully!
===== ATM MENU =======
1-Check balance
2-Withdraw money
3-Deposit money
4-Change ATM pin
5-Exit
Enter your choice:4
Enter your current pin:1234
Enter 4-digit ATM pin:23
Invalid new pin ,Must be 4-digit
===== ATM MENU =======
1-Check balance
2-Withdraw money
3-Deposit money
4-Change ATM pin
5-Exit
Enter your choice:4
Enter your current pin:1234
Enter 4-digit ATM pin:2345
===== ATM MENU =======
1-Check balance
2-Withdraw money
3-Deposit money
4-Change ATM pin
5-Exit
Enter your choice:5
Thank you for using the ATM Bye
"""
