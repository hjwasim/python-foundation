d = {'name':'hjwasim','location':'chennai','year':2000}
print(len(d))

l = list(d.values())
print(l) # ['hjwasim', 'chennai', 2000] ONLY VALUES

l = list(d.keys())
print(l) # ['name', 'location', 'year'] ONLY KEYS

print(list(d.items())) #[('name', 'hjwasim'), ('location', 'chennai'), ('year', 2000)]
# LIST OF TUPLES - [('KEY1','VALUE1')....]

d1 = d.copy()
print(f'd1:{d1}')

print(d.get('name')) #IF KEY IS PRESENT
print(d.get('name1')) #IF KEY IS NOT PRESENT, then `NONE`
#GET(KEY,DEFAULY_VALUE)
print(d.get('name1','NO NAME'))
print(d)


print(d.pop('name')) #IF KEY IS PRESENT
#print(d.pop('name1')) #IF KEY IS NOT PRESENT, then `KeyError will throw`
#pop(KEY,VALUE)
print(d.pop('name1','NO NAME')) # NO NAME
print(d)

#It remove any aribitary item, random item will be deleted.
print(d.popitem())

#setdefault(KEY,VALUE)
print(d.setdefault('name','hjwasim'))
print(d)
print(d.setdefault('name','HJWASIM'))
print(d)

d1.clear() #clear all items
print(d1) #empty dictionay
