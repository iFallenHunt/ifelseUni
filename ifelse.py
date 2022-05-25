n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
max = int

if n1 > n2:
  if n2 > n3:
    max = n1 
  else:
    max = n3
else:
  if n2 > n3:
    max = n2
  else:
    max = n3
print("o maior numero é", max)