#1 create empty dictionary
d = {}
d1 = dict()
print(type(d))
print(type(d1))

#2 if we have data,
d = {'key1':'value1',100:'value2','key3':'value3'}
print(d)

#using dict()
# MUST CONTAINS 2 ELEMENTS IN INTERAL TYPE.
#[KEY,VALUE],(KEY,VALUE),
# LIST OF TUPLES
d = dict([('list','of tuples'),('location','chennai'),('year',2000)])
print(d)
# LIST OF LISTS
d = dict([['list','of list'],['location','chennai'],['year',2000]])
print(d)
# TUPLE OF LISTS
d = dict((['tuple','of lists'],['location','chennai'],['year',2000]))
print(d)
# TUPLE OF TUPLES
d = dict((('tuple','of tuples'),('location','chennai'),('year',2000)))
print(d)
# SET OF TUPLES
d = dict({('set','of tuples'),('location','chennai'),('year',2000)})
print(d)

#3 by input
d = eval(input('ENTER DICTIONARY'))
print(d)

