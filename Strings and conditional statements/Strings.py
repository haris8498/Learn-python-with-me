#Strings
str1="My name is Mahnoor"
str2="I am a student at \n University of Gujrat" # For next line
print(str1)
print(str2)




#Different operations in string 

# Concatenation
str3=str1+str2
print(str3)

#Length of string 
print(len(str3))

#Indexing 
print(str1[0])






# str1[0]="N"  //This is not allowed in python 









# Slicing 

# str[starting_idx:ending_idx] // Ending idx is not included

str="Mahnoor"
print(str[1:5])

print(str[1:len(str)])

print(str[1:]) #It will automatically print till last index

#Negitive indexes
#  A[-5] P[-4] P[-3] L[-2] E[-1]
str4="Apple"
print(str4[-5:-3])




print("Strings functions")
# String functions
name="mahnoor"
print(name)
print(name.endswith("or"))
print(name.capitalize()) #Capitalize first letter
print(name.replace("mahnoor","Ayesha"))
print(name.find("n"))
print(name.count("o"))





