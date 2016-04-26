import sys
import operator
import math
from decimal import Decimal, getcontext, ROUND_DOWN

class PowerTower(object):
    __slots__ = ('tower')
    
    def __init__(self, tower):
        self.tower = tuple(map(int, tower.split("^")))

    def __lt__(self, other):
        return PowerTower.approximate(self.tower, other.tower)

    @staticmethod
    def approximate(lhs, rhs):
        def evalp(sl, sr):
            return (0, 0)

        v, w = evalp(1, 1)
        return v / math.log(rhs[0]) < w / math.log(lhs[0])



def domath(cnt):
    lines = [sys.stdin.next().strip() for _ in xrange(cnt)]
    values = {line : (fake_exponent(map(int, line.split("^"))), cnt) for cnt, line in enumerate(lines)}
    print values
    return "\n".join(sorted(lines, key=values.__getitem__))

def fake_exponent(l):
    exp = reduce(operator.mul, (l[v] for v in xrange(1, len(l))), 1)
    base = l[0]
    ans = exponents[base - 1] * Decimal(exp)
    print l, ans.quantize(Decimal('.001'), rounding=)
    return ans

if __name__ == '__main__':
    # getcontext().prec = 220
    global exponents
    exponents = [Decimal(v + 1).ln() for v in xrange(100)]
    print "\n".join("Case %d:\n%s" %(case + 1, domath(int(cnt))) for case, cnt in enumerate(sys.stdin))