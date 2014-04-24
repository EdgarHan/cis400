#edge class defines an edge used for vanishing point detection

from __future__ import division
import sys
import numpy as np

class Edge:
    def __init__(self, endpoint1, endpoint2):
        #endpoint 1
        self.ep1 = endpoint1
        self.ep2 = endpoint2
        x1,y1 = self.ep1
        x2,y2 = self.ep2
        self.length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5

    def __repr__(self):
        return "(endpoint1: %s endpoint2: %s)" % (self.ep1, self.ep2)
    # compute the midpoint of the edge
    def midpoint(self):
        x1,y1 = self.ep1
        x2,y2 = self.ep2
        return ((x1+x2)/2, (y1+y2)/2)

# compute a vanishing point hypothesis common to two edges
def perp(a):
    b = np.empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b

def vanishingPoint(edge1, edge2):
    a1 = np.array(edge1.ep1)
    a2 = np.array(edge1.ep2)
    b1 = np.array(edge2.ep1)
    b2 = np.array(edge2.ep2)

    a = a2 - a1
    b = b2 - b1
    a_perp = perp(a)
    denom = np.dot(a_perp, b)
    if denom == 0:
        return (sys.maxint, sys.maxint)
    num = np.dot(a_perp, a1 - b1)
    result = (num / denom) * b + b1
    return (int(result[0]), int(result[1]))
