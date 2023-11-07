class LogicGates:
    def andg(self, i1, i2):
        if i1==True and i2==True:
            return True
        return False
    def org(self, i1, i2):
        if i1==True or i2 == True:
            return True
        return False
    def notg(self, i):
        if i == False:
            return True
        return False
    def nandg(self, i1, i2):
        t1 = self.andg(i1, i2)
        t2 = self.notg(t1)
    def xorg(self, i1, i2):
        t1 = self.org(i1, i2)
        t2 = self.nandg(i1, i2)
        return(self.andg(t1, t2))
