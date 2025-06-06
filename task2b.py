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

""" output:
(base) PS C:\Users\shaim\Desktop\pythonlab> python task2b.py

Choose an operator type:
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Bitwise Operators
6. Special Operators
7. Exit
enter your choice (1-7)1
Arithmetic operations:
a + b = 5
a - b = -1
a * b = 6
a / b = 0.6666666666666666
a // b = 0
a % b = 2
a ** b = 8

Choose an operator type:
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Bitwise Operators
6. Special Operators
7. Exit
enter your choice (1-7)2
Assignment operations:
initial c = 10
c += 2 -> 12
c -= 2 -> 10
c *= 2 -> 20
c /= 2 -> 10.0
c //= 2 -> 5.0
c %= 2 -> 1.0
c **= 2 -> 1.0

Choose an operator type:
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Bitwise Operators
6. Special Operators
7. Exit
enter your choice (1-7)3
Comparison operations:
a == b False
a != b True
a > b False
a < b True
a >= b False
a <= b True

Choose an operator type:
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Bitwise Operators
6. Special Operators
7. Exit
enter your choice (1-7)4
Logical operations:
a > 5 and b < 5 True
a > 5 or b < 5 True
not(a > 5) : False

Choose an operator type:
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Bitwise Operators
6. Special Operators
7. Exit
enter your choice (1-7)5
Bitwise operations:
a & b = 4
a | b = 5
a ^ b = 1
~a = -5
a << 1 = 8
a >> 1 = 2

Choose an operator type:
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Bitwise Operators
6. Special Operators
7. Exit
enter your choice (1-7)6
Special operations:
x is y: False
x is not y: True
2 in x: True
5 not in x: True

Choose an operator type:
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Bitwise Operators
6. Special Operators
7. Exit
enter your choice (1-7)8
Invalid choice. Please try again!

Choose an operator type:
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Bitwise Operators
6. Special Operators
7. Exit
enter your choice (1-7)7
Exiting program. """
