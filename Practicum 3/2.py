def buatNol(a,b = None):
    if b == None:
        c = []
        e = 0
        while len(c) != a:
            d = []
            while len(d) != a:
                d.append(e)
            c.append(d)
        print(c)
    else:
        c = []
        e = 0
        while len(c) != a:
            d = []
            while len(d) != b:
                d.append(e)
            c.append(d)
        print(c)
            
def buatIdentitas(f):
    g = []
    h = 0
    i = 1
    j = 0
    while len(g) != f:
        k = []
        while len(k) != f:
            if len(k) == j:
                k.append(i)
            else:
                k.append(h)
        g.append(k)
        j += 1
    print(g)
