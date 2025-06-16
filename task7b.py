def addition(a,b):
    return a+b
def substraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def modulus(a,b):
    return a%b
x=int(input("enter first number:"))
y=int(input("enter second number:"))
while True:
    operator=input("enter an operator:")
    if operator=="+":
        print(x,"+",y,"=",addition(x,y))
    elif operator=="-":
        print(substraction(x,y))
    elif operator=="*":
        print(multiplication(x,y))
    elif operator=="/":
        print(division(x,y))
    elif operator=="%":
        print(modulus(x,y))
    else :
        print("syntax error")
        break

"""output: (base) PS C:\Users\shaim\Desktop\pythonlab> python task7b.py
enter first number:10
enter second number:5
enter an operator:+
10 + 5 = 15
enter an operator:-
5
enter an operator:*
50
enter an operator:/
2.0
enter an operator:%
0
enter an operator:=
syntax error
(base) PS C:\Users\shaim\Desktop\pythonlab>"""