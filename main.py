# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 09:24:37 2015

@author: aldo
"""
import agent
import edge
from simulGivenRoutes import execute 
from getRoutes import getRoutes
from itertools import product
from copy import deepcopy
from ARoptimization import ARoptim
from ExpOptim import updateProb
from ExpOptim import generateDraws
from abstract_rendering.glyphset import idx
#network creation
network=[[None]*4 for i in range(4)]
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

#Experience
#sensitivity to New information
#testing period




#agents routes pool calculation
agentsRoutesComb=getRoutes(network,agents,10)


#Social optimization
bestTime=[float("inf")]
for agentsRoutes in product(*agentsRoutesComb):
    tempAgents=deepcopy(agents)
    #calculation of the transportation outcome for each route combination
    transOut=execute(network, tempAgents, agentsRoutes)
    totalTime=0
    for out in transOut:
        totalTime+=out['timeFlow'][-1]-out['timeFlow'][0]
    if totalTime<bestTime[0]:
        bestTime=[totalTime]
        bestRoute=[agentsRoutes[:]]
    elif totalTime==bestTime[0]:
        bestTime.append(totalTime)
        bestRoute.append(agentsRoutes[:])
print(bestRoute)

#AR optimization
print(ARoptim(network, agents, agentsRoutesComb))


    
    
print('aca')
