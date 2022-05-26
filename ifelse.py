n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
n3 = int(input('Enter the third number: '))
max = int

if n1 > n2:
  max = n1
else:
    max = n2
if n3 > max:
    max = n3 

print("the greatest number is", max)