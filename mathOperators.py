def pw(exp, mod):
    return exp ** mod


def div(exp1, exp2):
    return exp1 / exp2


def mul(exp1, exp2):
    return exp1 * exp2


def add(exp1, exp2):
    return exp1 + exp2


def sub(exp1, exp2):
    return exp1 - exp2


def sqrt(val1, val2=2):
    # return val1 + val2
    pass


operators = {
    '+': add,
    '-': sub,
    '/': div,
    '*': mul,
    '^': pw
}
