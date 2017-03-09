import json
from kpp import kPlusPlus, kPoint

with open('data.json') as file:
	data = json.load(file)

clustering = kPlusPlus(data, 5, 8)
steps = clustering.iterate(100)
print '{} steps'.format(steps)

count = clustering.getGroupSize()
print 'cluster sizes: {}'.format(count)
groups = clustering.getGroups();
print 'groups: {}'.format(groups)