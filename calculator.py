import operation as op

while True:
    inp = int(input('''
    1.Addition
    2.Subtract
    3.Multiply
    4.Division
    5.Exit\n
    Enter Your Choise :-
    '''))

    if inp == 1:
        n11 = int(input("Enter Your Number 1 :-"))
        n12 = int(input("Enter Your Number 2 :-"))
        print (op.addition(n11, n12))


    elif inp == 2:
        n21 = int(input("Enter Your Number 1 :-"))
        n22 = int(input("Enter Your Number 2 :-"))
        print (op.subtrction(n21, n22))

    elif inp == 3:
        n31 = int(input("Enter Your Number 1 :-"))
        n32 = int(input("Enter Your Number 2 :-"))
        print (op.multiplication(n31, n32))

    elif inp == 4:
        n41 = int(input("Enter Your Number 1 :-"))
        n42 = int(input("Enter Your Number 2 :-"))
        print (op.division(n41, n42))

    elif inp == 5:
        quit()

    else:
        print("Incorrect")