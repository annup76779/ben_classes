# it says we want to execute some sort of code when some specific resource is in the RAM.


try:
    with open("text.txt", "r") as file:
        nfile = open("text.txt", "w")
        nfile.write("Hello")
except:
    pass


# try:
#     file = open("text.txt", "r")
# except:
#     print("error occured")

# print(file.readlines())