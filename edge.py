'''
Created on Oct 8, 2015

@author: aldo
'''
import sympy.parsing.sympy_parser
class edge:

    def __init__(self,costFunction):
        self.costF=sympy.parsing.sympy_parser.parse_expr(costFunction)
        self.currentCars=0
    def releaseRequest(self):
        self.currentCars-=1
    def seizeRequest(self):
        self.currentCars+=1
    def evalCost(self):        
        return  int(self.costF.evalf(subs={'x':self.currentCars}))
    