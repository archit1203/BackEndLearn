uname=input("Enter username: ")
passw=input("Enter password: ")

print("Account created successfully!")
print("Login now")

uname2=input("Enter username: ")
passw2=input("Enter password: ")

if uname==uname2 and passw==passw2:
    print("Logged in!")
else:
    print("Wrong password")