class LogicGates:
    def andg(i1, i2):
        if i1==True and i2==True:
            return True
        return False
    def org(i1, i2):
        if i1==True or i2 == True:
            return True
        return False
    def notg(i):
        if i == False:
            return True
        return False
    def nandg(i1, i2):
        t1 = LogicGates.andg(i1, i2)
        return LogicGates.notg(t1)
    def xorg(i1, i2):
        t1 = LogicGates.notg(i1)
        t2 = LogicGates.notg(i2)
        t3 = LogicGates.andg(i1, t2)
        t4 = LogicGates.andg(t1, i2)
        return LogicGates.org(t3, t4)
    def norg(i1, i2):
        t1 = LogicGates.org(i1, i2)
        return LogicGates.notg(t1)
