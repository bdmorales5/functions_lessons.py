# def tea_order(custormer_name , tea_type, **kwargs):
#     print(custormer_name, "ordered a" , tea_type, "tea")
#     for key, value in kwargs.items():
#         print("  - Add",key, ":", value)
   
# tea_order("alice" , "chamomile")
# tea_order("bob","black", milk ="oat")
# tea_order("tony", "black", milk = "oat",sweethner="honey")


# Indefinite Arguments (*args) Practice #1


# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.
def sum_squares(*args):
    sum=0
    for num in args:
        sum +=num **2
    return sum 
#first time through: sum = 0 + 4= 4
#first time through: sum = 4 + 25 = 29
#first time through: sum = 29 + 36 = 65
#first time through: sum = 65 + 49 = 114

print(sum_squares(3,4,5,6,7,7,7,8,9,9,9))


# For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).

# Indefinite Arguments (*args) Practice #2
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).
def absolute_sum(*args):
    sum=0
    for num in args:
        sum += abs(num)
        #first time through: sum = 0 + 10 = 10
        #second time through: sum = 10 + 5 = 15     
        #third time through: sum = 15 + 3 = 18
        #fourth time through: sum = 18 + 7 = 25
    return sum
list_of_numbers = [-10,5,-3,7,-2,6,7,-8,9]
print(absolute_sum(*list_of_numbers))


# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.
def personal_numbers(name, *args):
    sum_numbers = 0
    for num in args:#itarate through each argument 
        sum_numbers += num #add the numbers together
        #first time through: sum_numbers = 0 + 10 = 10
        #second time through: sum_numbers = 10 + 20 = 30
        #third time through: sum_numbers = 30 + 30 = 60
        #fourth time through: sum_numbers = 0 + 5 = 5
    return f"{name}, the sum of your numbers is {sum_numbers}"
print(personal_numbers("Alice", 10, 20, 30))
print(personal_numbers("Bob", 5, 15, 25, 35, 45))
# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"
