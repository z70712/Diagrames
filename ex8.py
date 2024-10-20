print("Introdueix tres números!")
n1= input("Introdueix el primer número a ordenar:")
n2= input("Introdueix el segon número a ordenar:")
n3= input("Introdueix el tercer número a ordenar:")
if n1 > n2:
    if n1 > n3:
        if n2 > n3:
            print(str(n1) + ", " + str(n2) + ", " + str(n3))
        print(str(n1) + ", " + str(n3) + ", " + str(n2))
    print(str(n3) + ", " + str(n1) + ", " + str(n2))
else:
    if n2 > n3:
        if n1 > n3:
            print(str(n2) + ", " + str(n1) + ", " + str(n3))
        print(str(n2) + ", " + str(n3) + ", " + str(n1))
    print(str(n3) + ", " + str(n2) + ", " + str(n1))