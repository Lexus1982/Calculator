from mathOperators import operators


def calculate(val):
    if val.isdigit():
        return float(val)
    for op in operators.keys():
        left, operator, right = val.partition(op)
        if operator in operators:
            return operators[operator](calculate(left.strip()), calculate(right.strip()))
