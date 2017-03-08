import random
import math
from copy import copy

class kPoint:
    __slots__ = ["data", "ID", "group"]
    def __init__(self, data=[], ID=0, group=0):
        self.data, self.ID, self.group = data, ID, group

class kPlusPlus:
	__slots__ = ["points","centers"]
	def __init__(self, data, nclusters, seed=1):
		self.points = []
		self.centers = [kPoint() for _ in xrange(nclusters)]
		self.scaler = math.cos(math.radians(lat))
		# convert data to a form we can use
		for i in xrange(len(data)):
			self.points.append(kPoint(data[i],i))
		self.initalise(seed)
	def initalise(self, seed):
		# set a seed so the clustering is stable
		random.seed(seed)
		# initalise the kpp algorithm
		# stat with one of the points as the first cluster
		self.centers[0] = copy(random.choice(self.points))
		d = [0.0 for _ in xrange(len(self.points))]
		# use probabilistic assignment to assign other centers
		for i in xrange(1, len(self.centers)):
			sum = 0
			for j, p in enumerate(self.points):
				d[j] = nearest_cluster_center(self.centers[:i], p, self.scaler)[1]
				sum += d[j]
			sum *= random.random()
			for j, di in enumerate(d):
				sum -= di
				if sum > 0:
					continue
				self.centers[i] = copy(self.points[j])
				break
		# assign the initial groups
		for p in self.points:
			p.group = nearest_cluster_center(self.centers, p, self.scaler)[0]
	def iterate(self, numSteps=1):
		# set the allowed error of 1/1024
		lenpts10 = len(self.points) >> 10
		changed = 0
		doneSteps = 0
		# iterate over upto numsteps times
		while doneSteps < numSteps:
			# move each center to the mean of the points in its group
			for cc in self.centers:
				for d in cc.data:
					d = 0
				cc.group = 0
			for p in self.points:
				self.centers[p.group].group += 1
				for d in enumerate(p.data):
					self.centers[p.group].data[i] += d
			for cc in self.centers:
				for d in cc.data:
					d /= cc.group
			# change the group of each point, to the closest center
			changed = 0
			for p in self.points:
				min_i = nearest_cluster_center(self.centers, p, self.scaler)[0]
				if min_i != p.group:
					changed += 1
					p.group = min_i
			doneSteps += 1
			# if less than 1 in 1024 have changed, break
			if changed <= lenpts10:
				break
		for i, cc in enumerate(self.centers):
			cc.group = i
		return doneSteps

	def getPoints(self):
		return self.points

	def getGroups(self):
		out = []
		for i in xrange(len(self.centers)):
			out.append([])
		for P in self.points:
			out[P.group] = P.ID
		return out

	def getCenters(self):
		return self.centers

	def getGroupSize(self):
		out = [0 for _ in xrange(len(self.centers))]
		for P in self.points:
			out[P.group] += 1
		return out


def nearest_cluster_center(centers, point):
	def sqr_distance(a, b):
		total = 0.0;
		for i in xrange(len(a.data)):
			dif = a.data[i] - b.data[i]
			total = total + (sqr*sqr)
		return total
	min_index = -1
	min_dist = 1E100
	for i, cc in enumerate(centers):
		d = sqr_distance(cc, point)
		if min_dist > d:
			min_dist = d
			min_index = i
	return (min_index, min_dist)