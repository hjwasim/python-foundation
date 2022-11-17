from sys import argv

args = argv[1:] #removing first element,
sum = 0
for a in args:
    sum+=int(a)

print(sum)
#150