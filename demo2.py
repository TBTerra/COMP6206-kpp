import json
from kpp import kPlusPlus, kPoint

with open('data.json') as file:
	data = json.load(file)

clustering = kPlusPlus(data, 5, 2)
#print '{} steps'.format(steps)
count = clustering.getGroupSize()
print 'cluster sizes: {}'.format(count)
groups = clustering.getGroups();
print 'groups: {}'.format(groups)

clustering.iterate(10)

count = clustering.getGroupSize()
print 'cluster sizes: {}'.format(count)
groups = clustering.getGroups();
print 'groups: {}'.format(groups)