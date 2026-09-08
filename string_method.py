
string=input("Enter a random string: ")
method=input("enter a mthod of string in lower case")
if method == "find":
    key=input("Enter the Key to find")
    print(string.find(key))
elif method == "rfind":
     key=input("Enter the Key to find")
     print(string.rfind(key))
elif method == "capatilize":
    print( string.capitalize())
elif method == "upper" :
     print(string.upper())
elif method == "lower":
     print(string.lower)
elif method == "isdigit":
     print(string.isdigit)

  