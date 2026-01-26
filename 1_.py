# function = a block of reusable code
#             place()after the function name to invoke it

# print("Happy birhtday to you!")
# print("You are old")
# print("Happy birthday to you!")


# print("Happy birhtday to you!")
# print("You are old")
# print("Happy birthday to you!")


# print("Happy birhtday to you!")
# print("You are old")
# print("Happy birthday to you!")


# def happy_birthday(name, uge):
#     print(f"Happy  Birhtday to {name}!")
# print(f"You are {uge} years old")
# print("Happy birthday to you!")


# happy_birthday("bro, 20")
# happy_birthday("Stave, 35")
# happy_birthday("Joe, 25")

# def display_invoice(username, amount , due_date):
#     print(F"hello {username}")
#     print(F"your bill of ${amount:.2f} is due" {due_date}")
          
# display_invoice("joeSchom", 100.01, "01/02")

# def add(x,y):
#     z= x + y
#     return z 

# def subtract(x, y):
#     z = x - y 
#     return z 

# def multiplay(x , y ):
#     z = x * y 
#     return z 

# def division(x , y):
#     z = x / y
#     return z 

# print(add(1 , 2))
# print(subtract(1, 2))
# print(multiplay(1 ,2))
# print(division(1, 2))

def create_name(first , last):
    first= first.capitalize()
    last=last.capitalize()
    return first +" "+ last 
full_name= create_name("bro", "code")

print(full_name)

