#Create A List To Save User Input Into
list = []

#User Input Function
def prompUser(iter,msg):
    # Create A For Loop To Iterate A Specified amount of time
    for i in range(iter):
        a = input(msg) # Prompt User for input with custom message
        list.append(a) # Add User Answers to list
    print(list) #Print Out List at end of loop

#Call Function with custom message
prompUser(5,"Enter A Random Word: ")