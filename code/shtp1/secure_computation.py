#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Author: ClarkYAN -*-

# secure multiplication depends on the formula
# X * Y = ( X + rx ) * (Y + ry ) − ( X * ry + Y * rx + rx * ry )
from paillier.paillier import *

import random
import timeit
import pickle
import xlrd
import xlwt


def open_db(filename):
    try:
        data = xlrd.open_workbook(filename)
        return data
    except Exception, e:
        print str(e)


def secure_multiplication(cx, cy):  # secure multiplication method
    # SHTP1
    rx = random.randint(0, 100)  # generate random numbers
    ry = random.randint(0, 100)
    crx = encrypt(pub, rx)
    cry = encrypt(pub, ry)
    mx = long(cx * crx)
    my = long(cy * cry)
    # SHTP2
    hx = decrypt(priv, pub, mx)
    hy = decrypt(priv, pub, my)
    h = hx * hy
    ch = encrypt(pub, h)
    # SHTP1
    sx = encrypt(pub, decrypt(priv, pub, ch) - decrypt(priv, pub, cx) * ry)
    sy = encrypt(pub, decrypt(priv, pub, sx) - decrypt(priv, pub, cy) * rx)
    sm = encrypt(pub, decrypt(priv, pub, sy) - rx * ry)
    print "SHTP1 computes m=", decrypt(priv, pub, sm)
    return sm


def secure_squared_euclidean_distance(file1, file2):  # secure squared Euclidean distance method
    data1 = open_db(file1)
    data2 = open_db(file2)
    table1 = data1.sheet_by_index(0)
    table2 = data2.sheet_by_index(0)
    # rows
    nrows1 = table1.nrows
    nrows2 = table2.nrows
    # columns
    ncols1 = table1.ncols
    ncols2 = table2.ncols
    # print "load original dataset..."
    temp = 1
    xls = xlwt.Workbook()
    sheet1 = xls.add_sheet(u'M10-N2000-S128-SSED', cell_overwrite_ok=True)
    if ncols1 == ncols2:
        for i in range(nrows1):
            for j in range(ncols1):
                if decrypt(priv, pub, long(table1.cell_value(i, j))) - decrypt(priv, pub,
                                                                               long(table2.cell_value(0, j))) < 0:
                    xy = (decrypt(priv, pub, long(table1.cell_value(i, j))) - decrypt(priv, pub, long(
                        table2.cell_value(0, j)))) * -1
                    # print "SHTP1 computes xy=", xy
                    sm = encrypt(pub, xy)
                    ssm = secure_multiplication(sm, sm)
                else:
                    sm = encrypt(pub, decrypt(priv, pub, long(table1.cell_value(i, j))) - decrypt(priv, pub, long(
                        table2.cell_value(0, j))))
                    ssm = secure_multiplication(sm, sm)
                ssed = temp * ssm
                temp = ssed
            sed = decrypt(priv, pub, ssed)
            print "SSED[Ek(x-y), Ek(x-y)]=", ssed, "SED=", sed
            sheet1.write(i, 0, str(ssed))
            temp = 1
        xls.save('experiment/ssed/128/M10-N2000-S128-SSED.xls')
    else:
        print "It is not suitable for the protocol!!!"


pub = pickle.load(open("keypair/pub_128.p", "rb"))
priv = pickle.load(open("keypair/priv_128.p", "rb"))
print "public key =", pub
start = timeit.default_timer()
secure_squared_euclidean_distance('experiment/data_owner_1/128/M10-N2000-S128_encrypted.xls',
                                  'experiment/query_provider/128/M10-Query-S128_encrypted.xls')
elapsed = (timeit.default_timer() - start)
print "processing time is", elapsed, "seconds"
