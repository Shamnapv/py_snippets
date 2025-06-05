def Arithmetic_ops():
    a,b=2,3
    print("Arithmetic operations:")
    print("a + b =",a+b)
    print("a - b =",a-b)
    print("a * b =",a*b)
    print("a / b =",a/b)
    print("a // b =",a//b)
    print("a % b =",a%b)
    print("a ** b =",a**b)
def Assignment_ops():
    c=10
    print("Assignment operations:")
    print("initial c =",c)
    c+=2;print("c += 2 ->",c)
    c-=2;print("c -= 2 ->",c)
    c*=2;print("c *= 2 ->",c)
    c/=2;print("c /= 2 ->",c)
    c//=2;print("c //= 2 ->",c)
    c%=2;print("c %= 2 ->",c)
    c**=2;print("c **= 2 ->",c)
def Comparison_ops():
    a,b=5,10
    print("Comparison operations:")
    print("a == b",a==b)
    print("a != b",a!=b)
    print("a > b",a>b)
    print("a < b",a<b)
    print("a >= b",a>=b)
    print("a <= b",a<=b)
def Logical_ops():
    a,b=10,3
    print("Logical operations:")
    print("a > 5 and b < 5",a>5 and b<5)
    print("a > 5 or b < 5",a>5 or b<5)
    print("not(a > 5) :",not(a>5))
def Bitwise_ops():
    a,b=4,5
    print("Bitwise operations:")
    print("a & b =",a&b)
    print("a | b =",a|b)
    print("a ^ b =",a^b)
    print("~a =",~a)
    print("a << 1 =",a<<1)
    print("a >> 1 =",a>>1)
def Special_ops():
    x=[1,2,3]
    y=[1,2,3]
    print("Special operations:")
    print("x is y:",x is y)
    print("x is not y:",x is not y)
    print("2 in x:",2 in x)
    print("5 not in x:",5 not in x)

def menu():
    while True:
        print("\nChoose an operator type:")
        print("1. Arithmetic Operators")
        print("2. Assignment Operators")
        print("3. Comparison Operators")
        print("4. Logical Operators")
        print("5. Bitwise Operators")
        print("6. Special Operators")
        print("7. Exit")

        choice=input("enter your choice (1-7)")
        if choice == '1':
            Arithmetic_ops()
        elif choice == '2':
            Assignment_ops()
        elif choice == '3':
            Comparison_ops()
        elif choice == '4':
            Logical_ops()
        elif choice == '5':
            Bitwise_ops()
        elif choice == '6':
            Special_ops()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again!")

menu()