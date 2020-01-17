import decimal
import math
from decimal import Decimal as D

def contFrac(x, k):
    """Cont Frac from Real value"""
    cf = []
    q = math.floor(x)
    cf.append(q)
    x = x - q
    i = 0

    while x != 0 and i < k:
        q = math.floor(1 / x)
        if q > k:
            break
        cf.append(q)
        x = 1/x - q
        i += 1

    return cf

def bestra(clist, app):
    """Best Rational Approximation from Cont. Frac"""
    hn0, kn0 = 0, 1
    hn1, kn1 = 1, 0
    """Best Rational Approx Init"""
    ran, rad = 0, 0
    conlist, finallist = [], []
    for n in clist:
        hn2 = (n*hn1)+hn0
        kn2 = (n*kn1)+kn0
        conlist.append({'ratio': f'{hn2}/{kn2}', 'denom': kn2})
        hn0, kn0 = hn1, kn1
        hn1, kn1 = hn2, kn2

    for x in sorted(conlist, key = lambda i: i['denom']):
        finallist.append(x['ratio'])

    return list(dict.fromkeys(finallist))

def seq_gen():
    seqsum = 0
    for i in range(1, 25): #to infinity
        a = D(i)*(D(10)**-(i+1))
        seqsum += (a)
    return seqsum

if __name__ == "__main__":
    prec = 100
    decimal.getcontext().prec = prec
    value = seq_gen()
    vc = contFrac(value, prec)
    print(bestra(vc, value)[-1])