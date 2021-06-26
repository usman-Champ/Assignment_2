user_Name = str(input("What is the username: "))
password = str(input("What is the password: "))
password_already_known = "abc$123"
if password == password_already_known :
    print("Welcome!")
else:
    print("I dont know you")
