# To input users first name and print its length
name=input("Enter your name: ")
print(len(name))



# To find the occourance of '$' in a string 
str="Hello $ how $ are $ you"
print(str.find("$"))


# Check if the number entered by the user is even or odd
number = int(input("Enter any number: "))
if(number%2!=0):
    print("Number is odd")
else:
    print("Number is even")




#To find greatest of the three numbers entered by the user

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))

if(a>b and a>c):
    print("1st number is greater")
elif(b>a and b>c):
    print("2nd number is greater")
else:
    print("3rd number is greater")


#To check if the number is a multiple of 7 or not 

num=int(input("Enter any number: "))
if(num%7==0):
    print("Divisible by 7")
else:
    print("Not divisible by 7")