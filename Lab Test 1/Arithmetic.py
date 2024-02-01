#Declared a variable (b) to let the while loop executed indefinitely. 
b = 1

# a = The first term of the arithmetic sequence
a = int(input("Enter the first term (a) of the arithmetic sequence: "))

#The below while loop is the technique of detecting whether the user input is positive integer or not.
while b == 1:
    if a < 0:
        #It will get another positive integer from the user if it detected the user input is negative integer. 
        a = int(input("Please insert positive number! \n a = "))
    else:
        #If the user input is positive integer, the while loop will break
        break

#d = The common difference of the arithmetic sequence
d = int(input("Enter the common difference (d) of the arithmetic sequence: "))

#Same while loop as the above had been used, the only difference is the detection of different variable. 
while b == 1:
    if d < 0:
        d = int(input("Please insert positive number! \n d = "))
    else:
        break

#n = The number of terms to sum
n = int(input("Enter the number of terms (n) to sum: "))

#Same while loop as the above had been used, the only difference is the detection of different variable. 
while b == 1:
    if n < 0:
        n = int(input("Please insert positive number! \n n = "))
    else:
        break

#The declaration of the starting value of the sum variable (Total)
total = 0

#The loop below will execute the arithmetic sequence which is equivalent to the mathematics formula below:
# total = a + (a+nd) + (a+nd)......
for i in range(n):
    total = total + a
    a = a + d

#At last, print out the final result of the arithmetic sequence
print("The sum of the first {} terms of the arithmetic sequence is = {}".format(n,total))