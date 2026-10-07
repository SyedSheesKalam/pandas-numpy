# list = ['ali', 3, 'bilal']
# list.append("haziq")
# list = list + ['hassan']
# list.reverse()
# list.insert(3,"yahya")
# list.remove(3) #to remove an element from the list, here 3 will remove
# list.pop(2) #to remove by the index from the list, here index 2 (bilal) will be removed bcz 3 was already removed already
# list[0] = "Shees" #to change the value of an element in the list, here index 0 (ali) will be changed to ahmed
# print(list)


# # WAP to ask user to enter his/her 3 favourite movies and store them in a list and print the list.  
# movie1 = input("Enter your favourite movie: ")
# movie2 = input("Enter your second favourite movie: ")   
# movie3 = input("Enter your third favourite movie: ")
# list = [movie1, movie2, movie3]
# print(list)


"""
 WAP to check if a list contains a palindrome or not. 
A palindrome is a word that is the same when read forwards and backwards.(Hint:use copy() method)
"""
list1 = [1, 2, 3, 2, 1]
list2 = ['haziq', 'bilal', 'yahya', 'imad', 'shees']
copy_list1 = list1.copy()
copy_list1.reverse()
if list1 == copy_list1:
    print("The list contains a palindrome.")
else:
    print("The list does not contain a palindrome.")

copy_list2 = list2.copy()
copy_list2.reverse()
if list2 == copy_list2:
    print("The list contains a palindrome.")
else:
    print("The list does not contain a palindrome.")
