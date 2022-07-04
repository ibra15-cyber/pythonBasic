correct_password = "python123"
password = input("Enter password: ")
name = input("Enter your Name: ")
surname = input("Enter your Surname: ")

while correct_password != password:
    password = input("Wrong password enter again: ")

message1 = name, surname, "logged in"
message2 = "%s %s you are logged in" %(name, surname)
print(message1) #tuple
print(message2) #string
