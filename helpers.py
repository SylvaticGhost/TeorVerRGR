import sympy as sp

def derangements(k):
    if k == 0:
        return 1
    if k == 1:
        return 0
    return (k - 1) * (derangements(k - 1) + derangements(k - 2))

def check_distribution(distribution, x1_val, x4_val, M, D):
    # Символи для x1, x4, p3
    x1, x4, p3 = sp.symbols('x1 x4 p3')

    # Копіювання словника і заміна значень x1 та x4
    dist_temp = distribution.copy()
    dist_temp[x1] = x1_val
    dist_temp[x4] = x4_val

    # Обчислення математичного сподівання
    p3_r = sp.solve(sp.Eq(sum(dist_temp.values()), 1))[0]
    M_X = sum([k * v for k, v in dist_temp.items()]) - M
    M_X = M_X.subs(p3, p3_r)
    M_X = sp.simplify(M_X)

    # Обчислення дисперсії
    M_X2 = sum([k**2 * v for k, v in dist_temp.items()]) - M**2
    M_X2 = M_X2.subs(p3, p3_r)
    D_X = sp.simplify(M_X2 - M_X)

    # Перевірка умов
    return M_X == M and D_X == D

def piecewise_diff_special(func, var):
    derivative = []
    for expr, cond in func.args:
        # If the expression is constant, the derivative is 0
        if expr.is_constant():
            derivative.append((0, cond))
        else:
            derivative.append((sp.diff(expr, var), cond))
    return sp.Piecewise(*derivative)
