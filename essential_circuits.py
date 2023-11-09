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
