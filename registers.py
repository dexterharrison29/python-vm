import essential_circuits as e
def accumulator(data, enable):
    global accumulator_value
    if accumulator_value is None:
        accumulator_value=e.register(data, enable)
    else:
        accumulator_value=e.register(data, enable, accumulator_value)
def base(data, enable):
    global base_value
    if base_value is None:
        base_value=e.register(data, enable)
    else:
        base_value=e.register(data, enable, base_value)
def count(data, enable):
    global count_value
    if count_value is None:
        count_value=e.register(data, enable)
    else:
        count_value=e.register(data, enable, count_value)
def datar(data, enable):
    global datar_value
    if datar_value is None:
        datar_value=e.register(data, enable)
    else:
        datar_value=e.register(data, enable, datar_value)




def instruction_pointer(data, enable):
    global instruction_pointer_value
    if instruction_pointer_value is None:
        instruction_pointer_value=e.register(data, enable)
    else:
        instruction_pointer_value=e.register(data, enable, instruction_pointer_value)
