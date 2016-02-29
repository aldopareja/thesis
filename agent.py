# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 17:00:09 2015

@author: aldo
"""

class agent:
    def __init__(self,origin,destination,departingTime):
        self.o=origin
        self.d=destination
        self.t=departingTime #initialized in 0. Edges Id must be > 0 and integers
        self.route=list()#contains the route followed
        self.route.append(origin)
        self.timeFlow=list() #contains the periods in which each vertex is visited
        self.timeQueue=0
        self.actualEdge=None
        if origin!=destination:
            self.finished=False
        else:
            self.finished=True
        
    def seizeEdge(self,cost, nextVertex,nextEdge):#updates agent information
        self.timeQueue=cost #the number of periods before releasing this edge
        self.actualEdge=nextEdge#this is the ID of the seized edge, for communicating a release.
        self.route.append(nextVertex)#stores the following vertex in its route
        if self.finished:
            raise ValueError('attempted to seize edge for a finished agent')
            
    def nextPeriod(self,period):
        if period>=self.t:
            if not self.finished:
                if self.timeQueue>0:
                    self.timeQueue-=1
                if self.timeQueue==0:
                    self.timeFlow.append(period)#stores period of visiting actual vertex
                    if self.route[-1]==self.d:
                        self.finished=True
                    if self.actualEdge is not None:
                        return self.actualEdge #this is for releasing the edge in main
                    else:
                        return -1 #value for communicating that is starting its trip
                if self.timeQueue<0:
                    raise ValueError('timeQueue<0')
            
    def getAgent(self):
        return [self.o,self.d,self.t]
        
    def getTransOuti(self):
        return [self.route,self.timeFlow]