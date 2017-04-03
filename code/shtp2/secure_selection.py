#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Author: ClarkYAN -*-

# secure selection protocol k = 1, 2, 3, 4, 5

from paillier.paillier import *

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


def load_data(filename, k):
    data = open_db(filename)
    table = data.sheet_by_index(0)
    nrows = table.nrows
    # ncols = table.ncols
    dist = {}
    for i in range(nrows):
        dist[i + 1] = int(decrypt(priv, pub, long(table.cell_value(i, 0))))
    print "SSED= ", dist
    if k == 1:
        result = secure_selection_1(dist)
    elif k == 2:
        result = secure_selection_2(dist)
    elif k == 3:
        result = secure_selection_3(dist)
    elif k == 4:
        result = secure_selection_4(dist)
    elif k == 5:
        result = secure_selection_5(dist)
    else:
        print "Wrong Input!!"
    print "SSO1NN= ", result


def secure_selection_1(x):
    ss = sorted(x.items(), key=lambda d: d[1])
    print "After sorting dist= ", ss
    # encrypted_result = encrypt(pub, ss[0])
    # print "Before encrypting= ", ss[0]
    return ss[0]


def secure_selection_2(x):
    ss = sorted(x.items(), key=lambda d: d[1])
    print "After sorting dist= ", ss
    return ss[0], ss[1]


def secure_selection_3(x):
    ss = sorted(x.items(), key=lambda d: d[1])
    print "After sorting dist= ", ss
    return ss[0], ss[1], ss[2]


def secure_selection_4(x):
    ss = sorted(x.items(), key=lambda d: d[1])
    print "After sorting dist= ", ss
    return ss[0], ss[1], ss[2], ss[3]


def secure_selection_5(x):
    ss = sorted(x.items(), key=lambda d: d[1])
    print "After sorting dist= ", ss
    return ss[0], ss[1], ss[2], ss[3], ss[4]

pub = pickle.load(open("keypair/pub_128.p", "rb"))
priv = pickle.load(open("keypair/priv_128.p", "rb"))
print "public key =", pub
input = raw_input("Select your proposed k: ")
k = int(input)
start = timeit.default_timer()
load_data('experiment/128/M10-N1000-S128-SSED.xls', k)
elapsed = (timeit.default_timer() - start)
print "processing time is", elapsed, "seconds"
