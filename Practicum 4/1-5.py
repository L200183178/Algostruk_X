class MhsTIF:
    def __init__(self, nama, nim, kota, uang):
        self.nama = nama
        self.nim = nim
        self.kota = kota
        self.uang = uang

c0 = MhsTIF("Ika", 10, "Sukoharjo", 240000)
c1 = MhsTIF("Budi", 51, "Sragen", 230000)
c2 = MhsTIF("Ahmad", 2, "Surakarta", 250000)
c3 = MhsTIF("Chandra", 18, "Surakarta", 235000)
c4 = MhsTIF("Eka", 4, "Boyolali", 240000)
c5 = MhsTIF("Fandi", 31, "Salatiga", 250000)
c6 = MhsTIF("Deni", 13, "Klaten", 245000)
c7 = MhsTIF("Galuh", 5, "Wonogiri", 245000)
c8 = MhsTIF("Janto", 23, "Klaten", 245000)
c9 = MhsTIF("Hasan", 64, "Karanganyar", 270000)
c10 = MhsTIF("Khalid", 29, "Purwodadi", 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

#1
a = []
b = 0
for i in Daftar:
    if i.kota == "Klaten":
        a.append(b)
        b += 1
    else:
        b += 1
print(a)

#2
c = c0.uang
d = ""
for i in Daftar:
    if i.uang < c:
        c = i.uang
        d = i.nama
    else:
        continue
print(c,d)

#3
e = []
f = c0.uang
for i in Daftar:
    if i.uang <= f:
        f = i.uang
    else:
        continue
for i in Daftar:
    if i.uang == f:
        e.append(i.nama)
print(e, f)

#4
g = 250000
h = []
for i in Daftar:
    if i.uang < g:
        h.append(i.nama)
    else:
        continue
print(h)

#5
def cariNIM(j, k):
    for i in j:
        if i.nim == k:
            return True
            break
        else:
            continue
    return False
