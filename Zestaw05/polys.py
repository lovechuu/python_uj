from itertools import zip_longest


def add_poly(poly1, poly2):
    res = [sum(coeffs) for coeffs in zip_longest(poly1, poly2, fillvalue = 0)]
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return res


def sub_poly(poly1, poly2):      
    res = [coeff1 - coeff2 for (coeff1, coeff2) in zip_longest(poly1, poly2, fillvalue = 0)]
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return res
    

def mul_poly(poly1, poly2):
    res = [0] * (len(poly1) + len(poly2) - 1)
    for i, coeff1 in enumerate(poly1):
        for j, coeff2 in enumerate(poly2):
            res[i+j] += coeff1 * coeff2
    return res


def is_zero(poly): 
    return True if poly.count(0) == len(poly) else False


def eq_poly(poly1, poly2):    
    while len(poly1) < len(poly2):
        poly1.append(0)
    while len(poly2) < len(poly1):
        poly2.append(0)
    return True if poly1 == poly2 else False


def eval_poly(poly, x0):
    res = 0
    for coeff in reversed(poly):
        res = res * x0 + coeff
    return res


def combine_poly(poly1, poly2):    
    res = []
    for i, coeff in enumerate(poly1):
        tmp = [coeff * x for x in pow_poly(poly2, i)]
        res = add_poly(res, tmp) 
    return res


def pow_poly(poly, n):
    res = [1]
    for i in range(n):
        res = mul_poly(res, poly)
    return res


def diff_poly(poly):
    return [poly[i] * i for i in range(1, len(poly))]
