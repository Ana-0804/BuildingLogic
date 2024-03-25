print("Enter the number of  your choice of operation")
print("1.Addition")
print( "2.Subtraction")
print( "3.Multiplication")
print("4.Division")
choice=int(input())
print("Enter the first number :")
a=float(input())
print("Enter the second number:")
b=float(input())
if (choice==1):
    c = a + b
elif (choice == 2):
    c = a - b
elif (choice == 3):
        c = a * b
else:
    if (b!=0):
        c = a / b
    else:      
        print(" Division by zero gives infinite.")
print("%g %s %g = %.5f" % (a,['+','-','*','/'][choice-1],b,c))  