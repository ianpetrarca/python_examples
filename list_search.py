#Create a Menu Spacer Function
def openLines(num,msg):
     print(msg)
     print("\n"*num)

# String List
my_list = ["ian","is","making",'lists','and','checking','them','twice']

# Get a Search Term from a user:
openLines(1,"-----")
openLines(1,"List Search Tool: ")
search = input("Enter A Word To Search: ")

# Check if the search term is in your list
if search in my_list:
	print("Search Term Found In List!")
	index = str(my_list.index(search)) # Get index of search term
	print("Item is at index # " + index + " in the list")
else: 
	print("Search Term Not Found In List!")


