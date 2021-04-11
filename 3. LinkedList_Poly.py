class Poly1:
    def __init__(self, maxOrder):
        self.coef = [0] * (maxOrder + 1)
        self.maxOrder = maxOrder

    def setCoef(self, coef, order):
        self.coef[order] = coef

    def print(self):
        _tmp = self.coef[::-1]
        for i in range(len(_tmp) - 1):
            if _tmp[i] != 0:
                print("{}x^{} + ".format(_tmp[i], len(_tmp) - i - 1), end="")
        print(self.coef[0])

    @classmethod
    def add(cls, p, q):
        if p.maxOrder >= q.maxOrder:
            n = q.maxOrder
            r = Poly1(n)
            for i in range(n + 1):
                r.coef[i] = p.coef[i] + q.coef[i]
            r.coef += p.coef[n+1:]
        else:
            n = p.maxOrder
            r = Poly1(n)
            for i in range(n + 1):
                r.coef[i] = p.coef[i] + q.coef[i]
            r.coef += q.coef[n + 1:]



p = Poly1(4)
p.setCoef(4, 4)
p.setCoef(3, 2)
p.setCoef(3, 0)
p.print()

q = Poly1(3)
q.setCoef(3, 3)
q.setCoef(4, 2)
q.setCoef(2, 1)
q.setCoef(1, 0)
q.print()

r = Poly1.add(p, q)
r.print()