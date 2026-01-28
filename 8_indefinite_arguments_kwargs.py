
# Indefinite Arguments (**kwargs) Practice #1
# Create a function called number_attributes that counts the number of parameters that are passed, and returns that number as the result.

def number_attributes(**kwargs):
    count = 0
    for key, value in kwargs.items():
        count += 1
        #first time through: count = 0 + 1 = 1
        #second time through: count = 1 + 1 = 2
        #third time through: count = 2 + 1 = 3
    return count 








# Indefinite Arguments (**kwargs) Practice #2
# Create a function called list_attributes that returns in the form of a list the values of the attributes given in the form of keywords. The function must expect to receive any number of arguments of this type.



def list_attributes(**kwargs):
    values_list = []
    for key, value in kwargs.items():
        values_list.append(value)
        #first time through: values_list = [] + [blue] = [blue]
        #second time through: values_list = [blue] + [tall] = [blue, tall]
        #third time through: values_list = [blue, tall] + [smart] = [blue, tall, smart]
    return values_list
print(list_attributes(eye_color="blue", height="tall", intelligence="smart"))


