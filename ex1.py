n = 0
r = 0
resultats = ""
e = input("Introdueix un número:")
while n < 11:
 r = int(e) * n
 n = n + 1
 if (n == 1):
  resultats = str(r)
 else:
  resultats = resultats + ", " + str(r)
print(resultats)