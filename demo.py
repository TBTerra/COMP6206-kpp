import json
from kpp import kPlusPlus, kPoint

with open('fisheriris.json') as file:
	data = json.load(file)

usedata = []
for d in data:
	usedata.append([d[1], d[2], d[3], d[4]])

clustering = kPlusPlus(usedata, 3, 1)
steps = clustering.iterate(1)
#print '{} steps'.format(steps)
centers = clustering.getCenters()
for i, cen in enumerate(centers):
	print 'centre {}: {}\n'.format(i,cen.data)
points = clustering.getPoints()
sucsess = 0
fails = 0
for i, point in enumerate(points):
	if point.group == data[i][0]:
		sucsess += 1
	else:
		fails += 1
print '{} sucsess, {} failures'.format(sucsess, fails)