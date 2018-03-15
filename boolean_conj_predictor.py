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
            return 0
    return 1
def removeElemInHypo(hypo,isPos,index):
    pie = 0
    for elem in hypo:
        if(elem.index == index and isPos == elem.isPositiveForm):
            del hypo[pie]
        pie = pie + 1
def printHypo(hypo):
    string_answer = '';
    for elem in hypo:
        if(elem.isPositiveForm):
            string_answer += 'x{0},'.format(elem.index)
        else:
            string_answer += 'not(x{0}),'.format(elem.index)
    return string_answer[0:-1]


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
for item,result in zip(X,Y):
    curr_hypo = hypothesis
    if(calcHypothesis(curr_hypo)== 0  and result == 1):
        indexush = 1
        for itemInX in item:
            if(itemInX == 1):
                removeElemInHypo(curr_hypo,False,indexush)
            elif(itemInX == 0):
                removeElemInHypo(curr_hypo,True,indexush)
            indexush = indexush + 1
    elif(result == 0):
        hypothesis = curr_hypo
with open('output.txt', 'w') as f:
    f.write(printHypo(hypothesis))
