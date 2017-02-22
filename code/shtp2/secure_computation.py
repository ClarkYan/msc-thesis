#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Author: ClarkYAN -*-

# secure multiplication depends on the formula
# X * Y = ( X + rx ) * (Y + ry ) − ( X * ry + Y * rx + rx * ry )
from paillier.paillier import *
from load_dataset import *

import random

"""def isEqual(ca, cb):
    a = decrypt(priv, pub, ca)  # decrypted with private key
    b = decrypt(priv, pub, cb)
    if a == b:  # compares the decrypted values
        return 1
    else:
        return 0


def multiplication(x, y):  # original multiplication method
    m = x * y
    cm = encrypt(pub, m)
    print "Ek(x*y)=", cm
    return cm"""


def secure_multiplication(cx, cy):  # secure multiplication method
    # SHTP1
    rx = random.randint(0, 100)  # generate random numbers
    ry = random.randint(0, 100)
    print "SHTP1 generates random number rx=", rx
    print "SHTP1 generates random number ry=", ry
    crx = encrypt(pub, rx)
    cry = encrypt(pub, ry)
    mx = cx * crx
    my = cy * cry
    print "SHTP1 sends mx(Ek(x)*Ek(rx)) to SHTP2, mx=", mx
    print "SHTP1 sends my(Ek(y)*Ek(ry)) to SHTP2, my=", my
    # SHTP2
    hx = decrypt(priv, pub, mx)
    hy = decrypt(priv, pub, my)
    h = hx * hy
    ch = encrypt(pub, h)
    print "SHTP2 sends ch(Ek[(x+rx)(y+ry)]) to SHTP1, ch=", ch
    # SHTP1
    sx = h - x * ry
    csx = encrypt(pub, sx)
    sy = sx - y * rx
    csy = encrypt(pub, sy)
    sm = sy - rx * ry
    csm = encrypt(pub, sm)
    print "After Secure Multiplication Protocol, result=", csm
    return csm


"""
def squared_euclidean_distance(x, y):  # original squared Euclidean distance method
    ed = pow((x - y), 2)
    ced = encrypt(pub, ed)
    print "Ek[pow(x-y), 2]=", ced
    return ced
"""


def secure_squared_euclidean_distance(x, y):  # secure squared Euclidean distance method
    ed = x - y
    sed = secure_multiplication(ed, ed)
    print "SM[Ek(x-y), Ek(x-y)]=", sed
    return sed


def main():
    open_db('data/test_db1_encrypted.xls')
    edb1 = read_excel('data/test_db1_encrypted.xls')
    open_db('data/test_query_encrypted.xls')
    equery = read_excel('data/test_query_encrypted.xls')
    priv, pub = generate_keypair(128)

if __name__ == "__main__":
    main()

"""
# print "Generating keypair..."
priv, pub = generate_keypair(128)
# pickle.dump(pub, open("save.p", "wb"))
print "public key =", pub
# test the function
# public_key = pickle.load(open("save.p", "rb"))
print "Show the result of computing original multiplication..."
mp = multiplication(3, 4)
print "Show the process of computing secure multiplication..."
smp = secure_multiplication(3, 4)
z = isEqual(mp, smp)
print "After decryption, result compares to (x*y), equal is 1, not equal is 0, z=", z
print "Show the result of computing original squared Euclidean distance..."
sd = squared_euclidean_distance(5, 2)
print "Show the process of computing secure squared Euclidean distance..."
ssd = secure_squared_euclidean_distance(5, 2)
zd = isEqual(sd, ssd)
print "After decryption, result compares to (pow(x-y), 2), equal is 1, not equal is 0, zd=", zd
"""
