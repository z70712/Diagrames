n = 0
i = 0
r = 0
resultats = ""
while i < 11:
 r = n * i
 n = n + 1
 if (i == 0):
  resultats = str(r)
 else:
  resultats = resultats + ", " + str(r)
 if (n > 10):
  n = 0
  i = i + 1
print(resultats)