from sys import argv
#using sys module, argv variable is used to get cmd args.

#py main.py 10 20
#[  main.py,10,20]
#    0       1  2
#space seperated

print(argv) #List of arguments passed by cmd line.
print(argv[0]) #location of python file.
print(argv[1]) #args we pass
#10

#Everythin we passed as cmd args is string type only.
print(type(argv[1]))
#string