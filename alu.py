from gates import LogicGates as g
import essential_circuits as e

class ALU:
    def add(i1=[], i2=[]):
        o1=e.full_adder(i1[3], i2[3], False)
        o2=e.full_adder(i1[2], i2[2], o1[1])
        o3=e.full_adder(i1[1], i2[1], o2[1])
        o4=e.full_adder(i1[0], i2[0], o3[1])
        return o4[0],o3[0],o2[0],o1[0]
    def sub(i1=[], i2=[]):
        o1=e.full_adder(i1[3], g.notg(i2[3]), True)
        o2=e.full_adder(i1[2], g.notg(i2[2]), o1[1])
        o3=e.full_adder(i1[1], g.notg(i2[1]), o2[1])
        o4=e.full_adder(i1[0], g.notg(i2[0]), o3[1])
        return o4[0],o3[0],o2[0],o1[0]