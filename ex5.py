from random import randint

vides = 5
n = randint(1, 2)
while vides > 0:
 e = input("Introdueix un número de l'1 al 100:")
 if n == int(e):
     print("Has guanyat!")
     print("El número és " + str(n) + " i has acabat amb " + str(vides) + " vides!")
     break
 if n > int(e):
     print("El número a endevinar és més gran!")
 else:
  print("El número a endevinar és més petit!")
 vides = vides - 1
 print("Et queden " + str(vides) + " vides!")
 if vides == 0:
  print("Has perdut!")
  print("El número era " + str(n) + "!")