dividend = input("Enter the dividend") #To get the dividend input
divisor = input("Enter the divisor")# To get divisor input
m=int(dividend)# To convert str value to integer
n=int(divisor)# To convert str value to integer
x=m//n # To perform floor division: to get the quotient
y=m%n # To perform modulus division , to give the remainder
print(f"{m} divided by {n} equals {x} remainder {y}")# display result
