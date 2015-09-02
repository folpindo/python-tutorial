#!/bin/env python

import collections

student = [
	{"name":'Tim',"age":7,"grade":7},
	{"name":'John',"age":7,"grade":7},
	{"name":'Aaron',"age":8,"grade":7}
]

print "name: %s" % student[0]["name"]

same = []
ages = []
ctr = 0

l = len(student)

for i in range(0,l):
	same.append(i)

for n in student:
	if n['age'] not in ages:
		ages.append(n['age'])
	else:
		
		same[ctr] =n

	print "name:%s,age:%s,grade:%s" % (n['name'],n['age'],n['grade'])
	ctr = ctr + 1
print same
print ages
j = 0
for e in same:
	print e
	if e is not dict:
		same.remove(e)
	j = j + 1
print same
