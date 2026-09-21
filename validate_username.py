#user name should be no more than 12 chracters length, no spaces, no dashes, only alphabets
username = input("Enter a username: ")

if len(username) > 12:
    print("Invalid username due to more characters")
elif " " in username:
    print("Invalid username due to spaces")
elif "-" in username:
    print("Invalid username due to dashes")
elif not username.isalpha():
    print("Invalid username due to non alphabet characters")
else:
    print("username is valid")
