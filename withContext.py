myfile = open("example.txt", "w")
myfile.write("this one needs a close")
myfile.close();


# this doen't not need close()

with open("example2.txt", "w") as myfile2:
    myfile2.write("This does not need to be closed\n it will close itself")
