from copy import deepcopy
from simulGivenRoutes import execute
from __builtin__ import True




def individualOptimization(network,agents,agentsRoutesComb,agentsRoutesIdxs,optimizingAgentIdx):
    agentsWithRoutes=list()
    agentsRoutes=list()
    for i,j in enumerate(agentsRoutesIdxs):
        if j is not None and i is not optimizingAgentIdx:
            agentsWithRoutes.append(agents[i])
            agentsRoutes.append(agentsRoutesComb[i][j])
    agentsWithRoutes.append(agents[optimizingAgentIdx])
    bestTime=float("inf")
    for i,route in enumerate(agentsRoutesComb[optimizingAgentIdx][:]):
        tempAgents=deepcopy(agentsWithRoutes)
        agentsRoutes.append(route)
        transOut=execute(network, tempAgents, agentsRoutes)
        time=transOut[-1]['timeFlow'][-1]-transOut[-1]['timeFlow'][0]
        if time<bestTime:
            bestTime=time
            bestRouteIdx=i
        agentsRoutes.pop()
    return bestRouteIdx

def ARoptim(network, agents, agentsRoutesComb):
    agentsRoutesIdxs=[None]*len(agents)
    convergence=False
    while not convergence:
        convergence=True
        for i in range(len(agents)):
            tempBestRoute=individualOptimization(network, agents, agentsRoutesComb, agentsRoutesIdxs, i)
            if agentsRoutesIdxs[i] is not tempBestRoute:
                convergence=False
                agentsRoutesIdxs[i]=tempBestRoute
    agentsRoutes=[agentsRoutesComb[i][agentsRoutesIdxs[i]] for i in range(len(agents))]
    return execute(network, agents, agentsRoutes)