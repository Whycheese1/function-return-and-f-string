def addition( c, d):
    product = c + d
    return product

#print(addition(2,4) )
###################
def subtraction( e, f):
    product = e - f
    return product

#print(subtraction(2,4) )
#########################
def divide( g, h):
    qoutient = g/h
    return qoutient

#print(multiply(2,4) )
########################
def multiply( a, b):
    product = a * b
    return product

#print(multiply(2,4) )
###################

total_students = multiply(3,22)
team_size = divide(total_students,6)
print(f"You have {total_students}, you can make 6 teams of {int(team_size)} students")