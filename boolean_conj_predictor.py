class Var:
    """A simple example class"""

    def __init__(self, isPositive=True, ind=0):
        self.isPositiveForm = isPositive
        self.index = ind;

    def calcVal(self, val):
        return (self.isPositiveForm and val == 1) or (not (self.isPositiveForm) and val == 0)


class Hypothesis:
    def __init__(self, d):
        self.list = []
        for i in range(1, d):
            self.list.append(Var(True, i))
            self.list.append(Var(False, i))

    def calcHypothesis(self):
        for item in self.list:
            if (not (item.calcVal(1))):
                return 0
        return 1

    def removeElemInHypo(self, isPos, index):
        pie = 0
        for elem in self.list:
            if (elem.index == index and isPos == elem.isPositiveForm):
                del self.list[pie]
            pie = pie + 1

    def printHypo(self):
        string_answer = '';
        for elem in self.list:
            if (elem.isPositiveForm):
                string_answer += 'x{0},'.format(elem.index)
            else:
                string_answer += 'not(x{0}),'.format(elem.index)
        return string_answer[0:-1]


def main():
    import numpy as np
    import sys as sys
    training_examples = np.loadtxt(sys.argv[1], dtype=int)
    d = len(training_examples[0])
    num_examples = len(training_examples)
    training_examples.reshape((num_examples, d))
    X, Y = training_examples[:, :d - 1], training_examples[:, d - 1]
    # Consistency  Algorithms

    # Intialize all variables with pos form and neg form
    hypo = Hypothesis(d)
    for item, result in zip(X, Y):
        curr_hypo = hypo
        if curr_hypo.calcHypothesis() == 0 and result == 1:
            indexush = 1
            for itemInX in item:
                if itemInX == 1:
                    curr_hypo.removeElemInHypo(False, indexush)
                elif itemInX == 0:
                    curr_hypo.removeElemInHypo(True, indexush)
                indexush = indexush + 1
        elif result == 0:
            hypothesis = curr_hypo
    with open('output.txt', 'w') as f:
        f.write(hypothesis.printHypo())


main()
