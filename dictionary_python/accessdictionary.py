d = {'name':'hjwasim','location':'chennai','year':2000}
#d[KEY_NAME]
print(d['name'])
print(d['location'])
#if key is not present, it give error, KeyError
print(d['chennai'])
#access using membership operators(IN , NOT IN)
''' if key in dictionary:
        pass
'''
if 'name' in d:
        print(d['name'])