# Using https://github.com/FindKim/Jaccard-K-Means/blob/master/k-means.py as an example implementation
# https://github.com/harborisland/plotly/blob/master/twitter%20k-means%20clustering%20analysis/twitter-followers-clustering-plotlygraphs.rmd

import plotly.plotly as plt
import plotly.graph_objs as go
from Points import Point
from Clusters import Cluster
import random
import math


def getDistance(a, b):
    if a.n != b.n: raise Exception("ERROR: Cannot compare points of different dimentions")
    ret = reduce(lambda x, y: x + pow((a.coords[y] - b.coords[y]), 2), range(a.n), 0.0)
    return math.sqrt(ret)

class KMeans:
    K = 2
    CUTOFF = 0.5
    points = list()

    def __init__(self, database, K = 2, Cutoff=0.5):
        self.K = K
        self.CUTOFF = Cutoff

        userIDs = list(database.distinct("UserID"))
        for userID in userIDs:
            userID = int(round(userID))
            results = list(database.find({"UserID": userID}, {"_id":0, "Friends": 1, "Followers": 1}).limit(1))
            for result in results:
                coords = list()
                coords.append(result["Followers"]) # X
                coords.append(result["Friends"]) # Y
                self.points.append(Point(coords))
        return

    def cluster(self):
        #pick out k random points for initial centroids
        initial = random.sample(self.points, self.K)

        #create k clusters using the initial centroids
        clusters = [Cluster([p]) for p in initial]

        #loop through the clusters until it stabalises
        loopCounter = 0
        while True:
            #Create a list of lists to hold the points in each cluster
            lists = [[] for c in clusters]
            clusterCount = len(clusters)

            loopCounter += 1
            for p in self.points:
                smallest_distance = getDistance(p, clusters[0].centroid)
                clusterIndex = 0
                for i in range(clusterCount - 1):
                    distance = getDistance(p, clusters[i+1].centroid)
                    if distance < smallest_distance:
                        smallest_distance = distance
                        clusterIndex = i+1
                lists[clusterIndex].append(p)

            biggest_shift = 0.0
            for i in range(clusterCount):
                shift = clusters[i].update(lists[i])
                biggest_shift = max(biggest_shift, shift)

            if biggest_shift < self.CUTOFF:
                print("Converged after %i iterations" % loopCounter)
                break
        return clusters

    def plotClusters(self, data):
        symbols = ['circle', 'cross', 'triangle-up', 'square']
        tracelist = []
        for i, c in enumerate(data):
            data = []
            for p in c.points:
                data.append(p.coords)
            trace = {}
            trace['x'], trace['y'] = zip(*data)
            trace['marker'] = {}
            trace['marker']['symbol'] = symbols[i]
            trace['name'] = "Cluster " + str(i)
            tracelist.append(trace)

            centroid = {}
            centroid['x'] = [c.centroid.coords[0]]
            centroid['y'] = [c.centroid.coords[1]]
            centroid['marker'] = {}
            centroid['marker']['symbol'] = symbols[i]
            centroid['marker']['color'] = 'rgb(200,10,10)'
            centroid['name'] = "Centroid " + str(i)
            tracelist.append(centroid)

        layout = {
            'mode': 'markers',
            'type': 'scater'
        }

        url = plt.plot(tracelist, layout=layout)

    def __del__(self):
        return