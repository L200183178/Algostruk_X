#1
class Pesan(object):
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print("Kalimatku mempunyai", len(self.teks), "karakter")
    def perbarui(self, stringBaru):
        self.teks = stringBaru
    def apakahTerkandung(self, cari):
        if cari in self.teks:
            return True
        else:
            return False
    def hitungKonsonan(self):
        y = 0
        x = ("A", "I", "U", "E", "O", "a", "i", "u", "e", "o")
        for i in self.teks:
            if i not in x:
                y += 1
            else:
                continue
        return y
    def hitungVokal(self):
        y = 0
        x = ("A", "I", "U", "E", "O", "a", "i", "u", "e", "o")
        for i in self.teks:
            if i in x:
                y += 1
            else:
                continue
        return y

#2
class Mahasiswa():
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama+ ", NIM " + str(self.NIM) \
            + ". Tinggal di " + self.kotaTinggal \
            + ". Uangsaku Rp " + str(self.uangSaku) \
            + " tiap bulannya."
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        print("Saya baru saja makan", s, "sambil belajar.")
        self.keadaan = "kenyang"
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self, kotaBaru):
        self.kotaTinggal = kotaBaru
    def tambahUangSaku(self, tambahUang):
        self.uangSaku += tambahUang

#3
class Mahasiswa():
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama+ ", NIM " + str(self.NIM) \
            + ". Tinggal di " + self.kotaTinggal \
            + ". Uangsaku Rp " + str(self.uangSaku) \
            + " tiap bulannya."
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        print("Saya baru saja makan", s, "sambil belajar.")
        self.keadaan = "kenyang"
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self, kotaBaru):
        self.kotaTinggal = kotaBaru
    def tambahUangSaku(self, tambahUang):
        self.uangSaku += tambahUang
x = input("Masukkan nama -> ")
z = input("Masukkan NIM -> ")
w = input("Masukkan kotaTinggal -> ")
v = input("Masukkan uangSaku -> ")
y = Mahasiswa(x, z, w, v)
print(y)

#4
class Mahasiswa():
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        self.daftar = []
    def __str__(self):
        s = self.nama+ ", NIM " + str(self.NIM) \
            + ". Tinggal di " + self.kotaTinggal \
            + ". Uangsaku Rp " + str(self.uangSaku) \
            + " tiap bulannya."
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        print("Saya baru saja makan", s, "sambil belajar.")
        self.keadaan = "kenyang"
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self, kotaBaru):
        self.kotaTinggal = kotaBaru
    def tambahUangSaku(self, tambahUang):
        self.uangSaku += tambahUang
    def listKuliah(self):
        return self.daftar
    def ambilKuliah(self, mataKuliah):
        self.daftar.append(mataKuliah)

#5
class Mahasiswa():
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        self.daftar = []
    def __str__(self):
        s = self.nama+ ", NIM " + str(self.NIM) \
            + ". Tinggal di " + self.kotaTinggal \
            + ". Uangsaku Rp " + str(self.uangSaku) \
            + " tiap bulannya."
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        print("Saya baru saja makan", s, "sambil belajar.")
        self.keadaan = "kenyang"
    def ambilKotaTinggal(self):
        return self.kotaTinggal
    def perbaruiKotaTinggal(self, kotaBaru):
        self.kotaTinggal = kotaBaru
    def tambahUangSaku(self, tambahUang):
        self.uangSaku += tambahUang
    def listKuliah(self):
        return self.daftar
    def ambilKuliah(self, mataKuliah):
        self.daftar.append(mataKuliah)
    def hapusKuliah(self, hapus):
        self.daftar.remove(hapus)

#6
class Manusia(object):
    keadaan = "lapar"
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salam, namaku", self.nama)
    def makan(self, s):
        print("Saya baru saja makan", s)
        self.keadaan = "kenyang"
    def olahraga(self, k):
        print("Saya baru saja latihan", k)
        self.keadaan = "lapar"
    def mengalikanDenganDua(self, n):
        return n*2

class SiswaSMA(Manusia):
    def __init__(self, nama, absen, sekolah, us):
        self.nama = nama
        self.noAbsen = absen
        self.sekolah = sekolah
        self.uangSaku = us
    def __str__(self):
        s = self.nama+ ", No Absen " + str(self.noAbsen) \
            + ". sekolah di " + self.sekolah \
            + ". Uang saku Rp " + str(self.uangSaku) \
            + " tiap minggunya."
        return s
    def ambilNama(self):
        return self.nama
    def ambilNoAbsen(self):
        return self.noAbsen
    def ambilUangSaku(self):
        return self.uangSaku
    def ambilSekolah(self):
        return self.sekolah
#7
class Manusia(object):
    keadaan = "lapar"
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salam, namaku", self.nama)
    def makan(self, s):
        print("Saya baru saja makan", s)
        self.keadaan = "kenyang"
    def olahraga(self, k):
        print("Saya baru saja latihan", k)
        self.keadaan = "lapar"
    def mengalikanDenganDua(self, n):
        return n*2

class Mahasiswa(Manusia):
    def __init__(self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama+ ", NIM " + str(self.NIM) \
            + ". Tinggal di " + self.kotaTinggal \
            + ". Uangsaku Rp " + str(self.uangSaku) \
            + " tiap bulannya."
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        print("Saya baru saja makan", s, "sambil belajar.")
        self.keadaan = "kenyang"

class MhsTIF(Mahasiswa):
    def katakanPy(self):
        print("Python is cool")

a = MhsTIF("Zaza, 3178, "Surakarta", 400000)
a.ucapkanSalam() # from class Manusia
a.makan("Nasgor") # from class Mahasiswa
a.olahraga("tidur") # from class Manusia
a.mengalikanDenganDua(18) # from class Manusia
a.ambilNama() # from class Mahasiswa
a.ambilNIM() # from class Mahasiswa
a.ambilUangSaku() # from class Mahasiswa
a.katakanPy() # from class MhsTIF
a.nama # from class Mahasiswa
a.NIM # from class Mahasiswa
a.kotaTinggal # from class Mahasiswa
a.uangSaku # from class Mahasiswa
