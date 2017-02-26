#！ /etc/bin/env python
import collections

class AutomataGenerator(object):
    def __init__(self):
        self.state0 = '000r'
        self.res = collections.OrderedDict()

    def generate(self):
        left = '0'
        right = '1'
        accept = 'a'
        reject = 'r'
        key = [self.state0] # a queue
        while len(key) > 0:
            state0 = key.pop(0)
            # stateA
            if state0[0] == left:
                stateA = right + state0[1:3] + reject
            elif state0[1] == left:
                stateA = left + right + state0[2] + reject
            else:
                stateA = left + left + state0[2] + accept
            # stateB
            if state0[2] == right:
                stateB = state0[0:2] + left + accept
            elif state0[1] == left:
                stateB = state0[0] + right + right + reject
            else:
                stateB = state0[0] + left + right + accept
            # add into res dict
            self.res[state0] = [stateA,stateB]
            # add into key queue
            if not stateA in self.res:key.append(stateA)
            if not stateB in self.res:key.append(stateB)

    def show(self):
        print ("\t|State\t|A\t|B")
        print ("    ->",end='')
        for i in self.res:
            if i[3] == 'a':
                print ('    *',end='')
            print ("\t|%s\t|%s\t|%s" % (i, self.res[i][0], self.res[i][1]))


if __name__ == "__main__":
    a = AutomataGenerator()
    a.generate()
    a.show()
