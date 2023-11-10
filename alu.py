from gates import LogicGates as g
import essential_circuits as e

class ALU:
    def add(i1=[], i2=[], c=False):
        o1=e.full_adder(i1[7], i2[7], c)
        o2=e.full_adder(i1[6], i2[6], o1[1])
        o3=e.full_adder(i1[5], i2[5], o2[1])
        o4=e.full_adder(i1[4], i2[4], o3[1])
        o5=e.full_adder(i1[3], i2[3], o4[1])
        o6=e.full_adder(i1[2], i2[2], o5[1])
        o7=e.full_adder(i1[1], i2[1], o6[1])
        o8=e.full_adder(i1[0], i2[0], o7[1])
        return o8[0],o7[0],o6[0],o5[0],o4[0],o3[0],o2[0],o1[0]
    def sub(i1=[], i2=[]):
        o1=e.full_adder(i1[7], g.notg(i2[7]), True)
        o2=e.full_adder(i1[6], g.notg(i2[6]), o1[1])
        o3=e.full_adder(i1[5], g.notg(i2[5]), o2[1])
        o4=e.full_adder(i1[4], g.notg(i2[4]), o3[1])
        o5=e.full_adder(i1[3], g.notg(i2[3]), o4[1])
        o6=e.full_adder(i1[2], g.notg(i2[2]), o5[1])
        o7=e.full_adder(i1[1], g.notg(i2[1]), o6[1])
        o8=e.full_adder(i1[0], g.notg(i2[0]), o7[1])
        return o8[0],o7[0],o6[0],o5[0],o4[0],o3[0],o2[0],o1[0]
