#m
import datetime as DT
#f

def meres (db):
    e1 = 0
    e2 = 10 ** db
    kezd = DT.datetime.now()
    for i in range(e1, e2):
        s = str(i)
        x == ( s == s )
    zar = DT.datetime.now()
    d = zar - kezd
    return (d.microseconds/1000)

def szamjegy(jsz):
    s = 0
    chs = "0123456789"
    for c in jsz:
        s += chs.count(c)
    return (s > 0)

def kisbetu(jsz):
    s = 0
    chs = "aábcdeéfghiíjklmnoóőöpqrstuúüűvwxyz"
    for c in jsz:
        s += chs.count(c)
    return (s > 0)

def nagybetu(jsz):
    s = 0
    chs = "AÁBCDEÉFGHIÍJKLMNOÓÖŐPQRSTÚUÜŰVWXYZ"
    for c in jsz:
        s += chs.count(c)
    return (s > 0)

#pt

for db in range (3,11):
    jelszo = input ("jelszó:")
    hosz = len(jelszo)

vb_szamjegy = szamjegy(jelszo)
vb_kisbetu = kisbetu(jelszo)
vb_nagybetu = nagybetu(jelszo)

print(f"a megfejtes eseten {hossz}")
print(f"a jelszóban van szamjegy {vb_szamjegy}")
print(f"a jelszoban van kisbetu{vb_kisbetu}")
print(f"a jelszoban van nagy betu{vb_nagybetu}")

d0 = meres(4)
print(f"a referencia ido {d0} ezred masodperc")

k = 0
if vb_szamjegy:
    k += 10
if vb_kisbetu:
    k += 34
if vb_nagybetu:
    k += 34

e = k ** hossz
ido = (e/1000) * d0

print(f"az elvégezendö müveletek száma : {e} muvelet")
print(f"a megfejtes ideje {ido} ezredmasodperc")