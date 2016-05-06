# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:24:37 2015

@author: aldo
"""
#%%
import agent
import edge
from simulGivenRoutes import execute 
from getRoutes import getRoutes
from itertools import product
from copy import deepcopy
from ARoptimization import ARoptim
from ExpOptim import updatePosterior
from ExpOptim import generateDraws
#network creation
network=[ [None] * 4 for i in range(4)]
network[0][1]=edge.edge('x')
network[1][2]=edge.edge('x')
network[1][3]=edge.edge('x')
network[3][2]=edge.edge('x')
#agent creation
agents=list()
agents.append(agent.agent(0,2,1))
agents.append(agent.agent(1,2,2))
agents.append(agent.agent(1,2,3))
agents.append(agent.agent(1,2,1))
#%%
#Experience
#sensitivity to New information
delta=0.1
#getting routes and costs
routesAndCosts=getRoutes(network, agents, 10, cost=True)
#calculate the first probability distribution
posterior=updatePosterior(routesAndCosts['costs'])
prior=posterior
#get a route draw for each agent
while True:
    for i in range(3000):
        Draws=generateDraws(probDist,routesAndCosts['routes'])
        #run basic algorithm with the draw
        tempNet=deepcopy(network)
        tempAgents=deepcopy(agents)
        transOut=execute(tempNet, tempAgents, Draws['routesDraw'])
        #update costs and probability distribution
        for idx, costs in enumerate(routesAndCosts['costs']):
            newCost=transOut[idx]['timeFlow'][-1]-transOut[idx]['timeFlow'][0]
            newCostIdx=Draws['routesDrawIdx'][idx]
            costs[newCostIdx]=1*delta*(newCost)+(1-delta)*costs[newCostIdx]
        probDist=updateProb(routesAndCosts)
    print('aca')
#agents routes pool calculation
agentsRoutesComb = getRoutes(network,agents,10)


# Social optimization
bestTime = [float("inf")]
for agentsRoutes in product(*agentsRoutesComb):
    tempAgents = deepcopy(agents)
    # calculation of the transportation outcome for each route combination
    transOut = execute(network, tempAgents, agentsRoutes)
    totalTime = 0
    for out in transOut:
        totalTime += out['timeFlow'][-1]-out['timeFlow'][0]
    if totalTime < bestTime[0]:
        bestTime = [totalTime]
        bestRoute = [agentsRoutes[:]]
    elif totalTime == bestTime[0]:
        bestTime.append(totalTime)
        bestRoute.append(agentsRoutes[:])
print(bestRoute)

# AR optimization
print(ARoptim(network, agents, agentsRoutesComb))   
print('aca')
