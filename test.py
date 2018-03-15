class Var:
    """A simple example class"""
    def  __init__(self, isPositive = True, ind = 0):
        self.isPositiveForm = isPositive;
        self.index = ind;
    def calcVal(self,val):
        return (self.isPositiveForm and val == 1) or (not(self.isPositiveForm) and val == 0)
def calcHypothesis(hypo):
    for item in hypo:
        if(not(item.calcVal(1))):
            return '0'
    return '1'
def removeElemInHypo(hypo,isPos,index):
    pie = 0
    for elem in hypo:
        if(elem.index == index and isPos == elem.isPositiveForm):
            del hypo[pie]
            break
        pie = pie + 1

import numpy as np
training_examples = np.loadtxt("testfile.txt")
d = len(training_examples[0])
num_examples = len(training_examples)
training_examples.reshape((num_examples,d))
X,Y = training_examples[:, :d-1],training_examples[:, d-1]
#Consistency  Algorithms

#Intialize all variables with pos form and neg form
hypothesis = [];
for i in range(1,d):
    hypothesis.append(Var(True,i))
    hypothesis.append(Var(False,i))
removeElemInHypo(hypothesis,False,2)
lol = 5