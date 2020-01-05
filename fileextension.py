fileName = input("Enter the fileName: ")
fileExtension = fileName.split(".")
print(repr(fileExtension[-1]))