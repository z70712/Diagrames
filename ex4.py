n = 0
i = 0
r = 0
resultats = ""
while i < 11:
 if (n == 0):
  resultats = resultats + "\n" + "Taula del " + str(i) + ":" + "\n"
 r = n * i
 resultats = resultats + str(n) + " * " + str(i) + " = " + str(r) + "\n"
 n = n + 1
 if (n > 10):
  n = 0
  i = i + 1
print(resultats)

