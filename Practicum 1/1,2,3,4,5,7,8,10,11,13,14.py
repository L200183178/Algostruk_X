

#1
def segitiga(x):
    y = 1
    z = 0
    while z < x :
        print("*" * y)
        y += 1
        z += 1

#2
def skuer(x,y) :
    z = 0
    while z < x :
        if z == 0 or z == x-1:
            print("@"*y)
        elif z != 0 and z != x :
            print("@"+" "*3+"@")
        z += 1
#3
def vokal(x) :
    z = 0
    w = ("A","I","U","E","O","a","i","u","e","o")
    for i in x:
        if i in w:
            z += 1
    y = (len(x), z)
    print(y)

def konsonan(x) :
    z = 0
    w = ("A","I","U","E","O","a","i","u","e","o")
    for i in x:
        if i in w:
            z += 1
    y = (len(x), z)
    print(y)

#4
def rerata(b) :
    y = 1
    z = 0
    x = 0
    while y <= len(b) :
        x += b[z]
        y += 1
        z += 1
    return x/len(b)

#5
from math import sqrt as sq
def apakahPrima(n):
    n = int(n)
    assert n >= 0
    primaKecil = [2,3,5,7,11]
    bukanPrKecil = [0,1,4,6,8,9,10]
    if n in primaKecil :
        return True
    elif n in bukanPrKecil :
        return False
    else:
        for i in range(2, int(sq(n))+1) :
            if n % i != 0 :
                return True
            else :
                return False

#7
def faktorPrima(x) :
    y = 0
    w = 0
    v = 0
    u = 0
    t = 0
    z = []
    while x % 2 == 0 :
        x = x / 2
        z.append(2)
    while x % 3 == 0 :
        x = x / 3
        z.append(3)
    while x % 5 == 0 :
        x = x / 5
        z.append(5)
    while x % 7 == 0 :
        x = x / 7
        z.append(7)
    z.append(int(x))
    if 1 in z :
        z.remove(1)  
    print(tuple(z))

#8
def apakahTerkandung(a,b) :
    if a in b :
        return True
    else:
        return False

#10
from math import sqrt as akar
def selesaikanABC(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    D = b ** 2 - 4 * a * c
    if D > 0 :
        x1 = (-b + akar(D)) / (2 * a)
        x2 = (-b - akar(D)) / (2*a)
        hasil = (x1,x2)
        return hasil
    else:
        print("Determinannya negatif. Persamaan tidak mempunyai akar real")

#11
def apakahKabisat(x):
    if x % 100 == 0 :
        if x % 400 == 0 :
            return True
        else:
            return False
    elif x % 400 == 0 or x % 4 == 0 :
        return True
    else:
        return False

#13
import inflect
def katakan(x):
    z = {"zero" : "nol", "one" : "satu", "two" : "dua", "three" : "tiga", "four" : "empat", "five" : "lima", "six" : "enam", "seven" : "tujuh", "eight" : "delapan", "nine" : "sembilan","ten" : "sepuluh",
         "eleven" : "sebelas", "twelve" : "dua belas", "thirteen" : "tiga belas", "fourteen" : "empat belas", "fifteen" : "lima belas", "sixteen" : "enam belas", "seventeen" : "tujuh belas",
         "eighteen" : "delapan belas", "nineteen" : "sembilan belas", "twenty" : "dua puluh", "thirty" : "tiga puluh", "forty" : "empat puluh", "fifty" : "lima puluh", "sixty" : "enam puluh",
         "seventy" : "tujuh puluh", "eighty" : "delapan puluh", "ninety" : "sembilan puluh", "hundred" : "ratus", "thousand" : "ribu", "million" : "juta", "billion" : "miliar", "trillion" : "triliun"}
    if len(str(x)) > 15 :
        print("tidak boleh melebihi 15 digit")
    else:
        y = inflect.engine().number_to_words(x)
        w = list(y)
        for i in w:
            if i == "-":
                w.insert(w.index("-"), " ")
                w.remove("-")
            if i == ",":
                w.remove(",")
        v = ""
        for i in w:
            v += i
        u = v.splitlines()
        t = ""
        for i in u:
            t += i
        s = t.split(" and")
        r = ""
        for i in s:
            r += i
        q = r.split(" ")
        p = []
        p.append(q[0:2])
        k = []
        k.append(q[2:4])
        i = []
        i.append(q[4:6])
        h = []
        h.append(q[6:8])
        g = []
        g.append(q[8:10])
        f = []
        f.append(q[10:12])
        e = []
        e.append(q[12:14])
        d = []
        d.append(q[14:16])
        c = []
        c.append(q[16:18])
        b = []
        b.append(q[18:20])
        a = []
        a.append(q[20:22])
        aa = []
        aa.append(q[22:24])
        ab = []
        ab.append(q[24:26])
        ac = []
        ac.append(p)
        ac.append(k)
        ac.append(i)
        ac.append(h)
        ac.append(g)
        ac.append(f)
        ac.append(e)
        ac.append(d)
        ac.append(c)
        ac.append(b)
        ac.append(a)
        ac.append(aa)
        ac.append(ab)
    n = [['one', 'hundred']]
    m = [['one', 'thousand']]
    for i in ac:
        if i == n:
            print("seratus", end = " ")
        elif i == m:
            print("seribu", end = " ")
        else:
            for ae in i:
                for af in ae:
                    print(z[af], end = " ")

#14
def formatRupiah(x):
    x = str(x)
    y = list(x)
    if len(x) > 9:
        print("tidak boleh lebih dari atau sama dengan 1 miliar")
    if len(x) < 4:
        print("Rp.", x)
    if 3 < len(x) < 7 :
        y.insert(-3,".")
        print("Rp.", end = " ")
        for i in y :
            print(i, end = "")
    if 6 < len(x) < 10 :
        y.insert(-3,".")
        y.insert(-7,".")
        print("Rp.", end = " ")
        for i in y :
            print(i, end = "")
