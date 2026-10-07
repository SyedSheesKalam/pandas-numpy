# # def calculate_sum(a, b):
# #     sum = a + b
# #     print("The sum of a and b is:", sum)
# #     return sum

# # calculate_sum(5, 10)
# # calculate_sum(20, 30)

# # Calculate average of 3 numbers
# def cal_avg(n1, n2, n3):
#     avg = (n1 + n2 + n3) / 3
#     return avg

# print(cal_avg(10, 20, 30))    
    
# # WAF to print the length of a list .( list is passed as an argument to the function)
# cities = ["Karachi", "Lahore", "Islamabad", "Quetta", "Peshawar"]
# heroes = ["Superman", "Batman", "Spiderman", "Ironman", "Hulk"]
# def print_len(lst):
#     print(len(lst))

# print_len(cities)
# print_len(heroes)

# WAF to print the elements of a list .( list is passed as an argument to the function)
def cal_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        print(fact, end=" ")

print(cal_factorial(6))

        