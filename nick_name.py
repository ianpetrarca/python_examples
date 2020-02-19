# Python Project: Nick NAME GENERATOR 
# CLI Goals: Generate A Nick Name From a User's Data

# Python Topics: 
#   - If Statement
#   - Writing To Files
#   - Lists
#   - Functions

# Sample Data:
# - Broadway
# - 25
# - Purple
# - 5
# - Brooklyn


import random
#Create a Menu Spacer Function
def openLines(num,msg):
     print(msg)
     print("\n"*num)

#Add Opening Prompt
openLines(0,("-"*10))   
openLines(3,"")
openLines(0,"Welcome To The Nick Name Generator")

#Enter Street Name
street = input("Enter Your Street Name: ")
#Enter Age
age = input("Enter Your Age: ")
if int(age) > 65:
    age = "old"
else:
    age = "yung"

#Enter Color
color = input("Enter Your Favorite Color: ")

#Enter Sign
sign = input("Enter Your Birthday Month Number: ")
sign_list = ['Capricorn', 'Aquarius', 'Pisces', 'Aries', 'Zodiac', 'Gemini', 'Cancer',
 'Leo  ', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius']
sign = sign_list[(int(sign)-1)]

#Enter Hometown
hometown = input("Enter Your Hometown: ")

names = []
#Randomize Names
def randomize(age,sign,street,color,town):
    names.append(sign),names.append(street),names.append(color) 
    sampling = random.sample(names,k=2) #return random choice
    return age + " " + sampling[1] + " " + sampling[0][0]

#Print Final Result
openLines(1,"-")   
result = randomize(age,sign,street,color,hometown)+" from "+hometown

#Display and Save Result
print(result)
file = open("name.txt", "w")
file.write(str(result))
file.close()