'''
Created on Oct 14, 2015

@author: aldo
'''
import YenKSP.algorithms as Yen
from copy import deepcopy
from YenKSP.graph import DiGraph

def getRoutes(network,agents,k,cost=False):
    emptyNetwork=deepcopy(network)
    G=DiGraph()#graph class to create the object for YENs algorithm
    for rowIdx, row in enumerate(emptyNetwork):
        for colIdx, col in enumerate(row):
            if col is not None:
                col.seizeRequest()#add one car to each edge in the empty network
                G.add_edge(rowIdx, colIdx, col.evalCost())#add an edge to the fixed network
    #Get each agent's routes from Yen's algorithm and the fixed empty network
    agentsRoutes=[None]*len(agents)
    agentsRoutesCost=[None]*len(agents)
    for agentIdx in range(len(agentsRoutes)):
        agentsRoutes[agentIdx]=list()
        agentsRoutesCost[agentIdx]=list()
        for path in Yen.ksp_yen(G, agents[agentIdx].o, agents[agentIdx].d, k):
            agentsRoutes[agentIdx].append(path['path'])
            agentsRoutesCost[agentIdx].append(path['cost'])
    costosZero=[[0 for i in range(len(agentsRoutesCost[j]))] for j in range(len(agentsRoutesCost))]
    if cost:
        return {'routes':agentsRoutes,'costs':costosZero}
    else:            
        return(agentsRoutes)