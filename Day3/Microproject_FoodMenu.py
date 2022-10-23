#Design a food menu app where a user can select an item out of multiple 
#choices shown to the user. The item selected by the user is shown to the user as the output.
# List of items on the menu stored in the form of list
items = ['Biriyani','Pulao','Palak Paneer','Dal Makhani','Butter Chicken','Butter Naan','Hot and Sour Soup','Paneer Roll','Jeera Rice'] 
# User gives in input an item amongst the list of items stored on the menu
i = input('Enter the item you want to choose: ')
# if the input item, i is present in the items list, items; then the item will be printed. Else the user will be asked to enter a valid item name
if i in items:
  print(i)   # printing the item
else:
  print("Please enter a valid item name.") # if item does not exist in list of items then user has to enter valid item
