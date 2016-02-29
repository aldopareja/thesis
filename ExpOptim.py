'''
Created on Jan 25, 2016

@author: aldo
'''
from numpy.random import choice
def updateProb(routesAndCosts):
    probDist=[None]*len(routesAndCosts['costs'])
    for agentIdx, costs in enumerate(routesAndCosts['costs']):
        probDist[agentIdx]=[None]*len(costs)
        for routeIdx, cost in enumerate(costs):
            probDist[agentIdx][routeIdx]=(1.0/cost)/sum([1.0/tmp for tmp in costs])
    return probDist
def generateDraws(probDist,agentsRoutes):
    routeDraw=[None]*len(probDist)
    routeDrawIdx=[None]*len(probDist)
    for i in range(len(routeDraw)):
        routeDrawIdx[i]=choice(a=range(len(probDist[i])),p=probDist[i])
        routeDraw[i]=agentsRoutes[i][routeDrawIdx[i]]
    return {'routesDrawIdx':routeDrawIdx,'routesDraw':routeDraw}

    