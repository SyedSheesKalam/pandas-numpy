# i = 10
# n = int(input("Enter a number: "))
# while i >= 1:
#     print("The count is:", n * i)
#     i -= 1

# list

# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# idx = 0
# while idx < len(list):
#     print(list[idx])
#     idx += 1

# Search
# tup=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# idx = 0
# x = int(input("Enter a number to search: "))
# while idx < len(tup):
#     if tup[idx] == x:
#         print("Found")
       
#     idx += 1

# BREAK
i = 1
# while i <= 5:
#     print(i)
#     if (i == 3):
#         print("The end of loop")
#         break
#     i += 1

# # CONTINUE
# i=1
# while i <= 5:
#     if (i == 3):
#         i += 1
#         continue #skip the current iteration and move to the next one
#     print(i)
#     i += 1
  
# For Loop
# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# find = int(input("Enter a number to search: "))
# for val in num:
#     if val == find:
#         print("Found")
#         break
# else:
#     print("Not Found")


# str = "Hello World"
# for char in str :
#     print(char)
# else:
#     print("The end of loop")

# RANGE
# range(start, stop, step)
# #   optional, Compulsory, optional
# num = int(input("Enter a number: "))
# for i in range(1,11):
#     print(num * i)

#     # PASS
# for i in range(6):
#     pass
# print("The count is:" ) 

# PRACTICE
#  1. Write a program to FIND the sum of first N natural numbers using  while.
# N = int(input("Enter a number: "))
# sum = 0
# i = 1

# while i <= N:
#     sum += i
#     i += 1
# print("total sum = ", sum)

# Write a program to find the factorial of first n number using while .
# n = int(input("Enter a number: "))
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1

# print("Factorial is:", fact)

# Write a program to find the factorial of first n number using for.
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n +1):
    fact *= i

print("Factorial is:", fact)
