#write a program to find the largest number among three number

num1 = 80
num2 = 8
num3 = 16

if (num1 >=num2) and (num1 >=num3):
  largest = num1
elif(num2 >=num1) and (num2 >=num3):
  largest = num2
else:
  largest = num3
  
print("The largest number is", largest)
