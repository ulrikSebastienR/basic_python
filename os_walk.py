import os
print(os.path)
print(dir(os))
print(os.getcwd())
current = os.getcwd()
#os.chdir(path = "/home/normal/Documents/python_2023_thoughtful")
#print(os.path)
#print(help(os.chdir))
for (root, dirs, files) in os.walk(os.getcwd()):
    print("ROOT IS", root)
    for d in dirs:
        print("DIR IS",  d)
        for file in files:
            print("FILE IS", file)
