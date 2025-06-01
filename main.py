def add(x,y):
    return x + y   

def subtract(x,y):
    return x - y     
  
def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def modulus(x,y):
    return x % y

def sum_list(numbers):
    """Returns the sum of a list of numbers."""
    total = 0
    for number in numbers:
        total += number
    return total


users=[
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 28},
    {"name": "Eve", "age": 22},
    {"name": "Frank", "age": 40},
    {"name": "Grace", "age": 32},
    {"name": "Hannah", "age": 29},
    {"name": "Ivy", "age": 27},
    {"name": "Jack", "age": 31}
]


def get_user_by_name(name):
    """Returns user information by name."""
    for user in users:
        if user["name"].lower() == name.lower():
            return user
    return None


def get_users_by_age(age):
    """Returns a list of users by age."""
    return [user for user in users if user["age"] == age]

def get_users_above_age(age):
    """Returns a list of users above a certain age."""
    return [user for user in users if user["age"] > age]



