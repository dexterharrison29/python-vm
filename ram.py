import essential_circuits as e
global ram
rv = [[False, False, False, False, False, False, False, False]]*16777216
def ram(data, enable, add=""):
    i = int(add, 16)
    output=rv[i]
    o1=e.gated_latch(data[0], enable, output[0])
    o2=e.gated_latch(data[1], enable, output[1])
    o3=e.gated_latch(data[2], enable, output[2])
    o4=e.gated_latch(data[3], enable, output[3])
    o5=e.gated_latch(data[4], enable, output[4])
    o6=e.gated_latch(data[5], enable, output[5])
    o7=e.gated_latch(data[6], enable, output[6])
    o8=e.gated_latch(data[7], enable, output[7])
    rv[i]=o1,o2,o3,o4,o5,o6,o7,o8
    return o1,o2,o3,o4,o5,o6,o7,o8
