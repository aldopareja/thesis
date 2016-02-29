'''
Created on Oct 9, 2015

@author: aldo
'''
def execute(network,agents,agentsRoutes):
    period=0
    driversFinished=False
    routeIndexer=[0]*len(agents)
    while not driversFinished:
        #drivers communicate to edges release or seize requests
        period+=1
        driversFinished=True
        seizingCars=[None]*len(agents)
        for i in range(len(agents)):
            temp=agents[i].nextPeriod(period)
            if temp is not None:
                if temp!=-1:
                    network[temp[0]][temp[1]].releaseRequest()
                if not agents[i].finished:
                    routeIndexer[i]+=1
                    edgeOrg=agentsRoutes[i][routeIndexer[i]-1]
                    edgeSink=agentsRoutes[i][routeIndexer[i]]
                    network[edgeOrg][edgeSink].seizeRequest()
                    seizingCars[i]=[edgeOrg,edgeSink]
            if driversFinished:
                if agents[i].finished==False:
                    driversFinished=False
        #edges communicate to drivers after knowing the total cars seizing/crossing the edge
        for i in range(len(seizingCars)):
            if seizingCars[i] is not None:
                cost=network[seizingCars[i][0]][seizingCars[i][1]].evalCost()
                agents[i].seizeEdge(cost,seizingCars[i][1],seizingCars[i])
    #getting the transportation outcome
    transOut=[None]*len(agents)
    for i in range(len(agents)):
        transOut[i]={'route':agents[i].route,'timeFlow':agents[i].timeFlow}
    return transOut