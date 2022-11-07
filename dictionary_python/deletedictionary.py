d = {'name':'hjwasim','location':'chennai','year':2000}
#to delete an element,
#use 'del' keyword
# del d[KEY_NAME]
del d['name']
print(d) #{'location': 'chennai', 'year': 2000}

#we delete multiples key-value pairs as well using ',' seperated
del d['location'], d['year']
print(d) #EMPTY DICT