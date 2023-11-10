from gates import LogicGates as g


def half_adder(i1, i2):
    sum = g.xorg(i1, i2)
    carry = g.andg(i1, i2)
    return sum, carry
def full_adder(i1, i2, c):
    t1, t2 = half_adder(i1, i2)
    sum, t3 = half_adder(t1, c)
    t4 = g.andg(t3, c)
    carry = g.org(t2, t4)
    return sum,carry
def gated_latch(data, enable, output=False):
    t1=g.andg(data, enable)
    t2=g.andg(g.notg(data), enable)
    t3=g.notg(t2)
    t4 = g.org(t1, output)
    output = g.andg(t3, t4)
    return output

def register(data, enable, output=[False, False, False, False, False, False, False, False]):
    o1=gated_latch(data[0], enable, output[0])
    o2=gated_latch(data[1], enable, output[1])
    o3=gated_latch(data[2], enable, output[2])
    o4=gated_latch(data[3], enable, output[3])
    o5=gated_latch(data[4], enable, output[4])
    o6=gated_latch(data[5], enable, output[5])
    o7=gated_latch(data[6], enable, output[6])
    o8=gated_latch(data[7], enable, output[7])
    return o1,o2,o3,o4,o5,o6,o7,o8
