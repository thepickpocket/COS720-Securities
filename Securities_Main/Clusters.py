import math

from Points import Point

class Cluster:
    points = None #points that belong to this cluster
    n = 0 #Dimentionality of points in the cluster
    centroid = None

    def __init__(self, points):
        if len(points) == 0: raise Exception("ERROR: Empty cluster")
        self.points = points
        self.n = points[0].n

        #make sure we are working with points in the same dimentionality
        for point in points:
            if point.n != self.n: raise  Exception("ERROR: Points are not of the same dimentions")

        #Set initial centroid
        self.centroid = self.calculateCentroid()
        return

    def calculateCentroid(self):
        numPoints = len(self.points)
        coords = [p.coords for p in self.points]
        unzipped = zip(*coords)
        #calculating the mean of each dimention
        centroid_coords = [math.fsum(dList)/numPoints for dList in unzipped]
        return Point(centroid_coords)

    def update(self, points):
        old_centroid = self.centroid
        self.points = points
        self.centroid = self.calculateCentroid()
        shift = self.getDistance(old_centroid, self.centroid)
        return shift

    def getDistance(self, a, b):
        if a.n != b.n: raise Exception("ERROR: Cannot compare points of different dimentions")
        ret = reduce(lambda x,y: x + pow((a.coords[y]-b.coords[y]), 2), range(a.n), 0.0)
        return math.sqrt(ret)

    def __del__(self):
        return
