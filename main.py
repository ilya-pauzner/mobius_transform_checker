import numpy as np


def mobius(a, b, c, d, z):
    return (a * z + b) / (c * z + d)


def make_function(z1, z2, z3, w1, w2, w3):
    def inner(a, b, c, d):
        differences = [
            abs(mobius(a, b, c, d, z1) - w1),
            abs(mobius(a, b, c, d, z2) - w2),
            abs(mobius(a, b, c, d, z3) - w3)
        ]
        return sum(differences), np.isclose(differences, 0).sum()

    return inner


func1 = make_function(2j, 0, 1, -1j, 1j, 2)
func2 = make_function(0, 1j, 2, -2, -1j, 2j)
func3 = make_function(1j, -2j, -1, -1j, 1, 0)
func4 = make_function(2j, -1, 1, 0, 2, -1j)
func5 = make_function(-1j, 0, -2, 1, 2j, 1j)
funcs = [None, func1, func2, func3, func4, func5]

while True:
    variant = int(input('Variant: '))
    a = complex(input('a: '))
    b = complex(input('b: '))
    c = complex(input('c: '))
    d = complex(input('d: '))
    try:
        rem, correct_count = funcs[variant](a, b, c, d)
        if rem > 0:
            raise RuntimeError
    except RuntimeError:
        print(f'Wrong answer, sum(abs(f(z_i) - w_i)) = {rem}, correct points = {correct_count}')
    except ZeroDivisionError:
        print('Zero division')
    else:
        print('OK')
    print()
