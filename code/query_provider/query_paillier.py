#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Author: ClarkYAN -*-

from paillier.paillier import *
from send_to_cloud import *

import pickle
import xlrd
import xlwt


# load the raw data records
def open_excel(file='experiment/raw/M30-Query.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception, e:
        print str(e)


def write_excel(file='experiment/raw/M30-Query.xls'):
    data = open_excel(file)
    table = data.sheet_by_index(0)
    nrows = table.nrows  # rows
    ncols = table.ncols  # columns

    pub = pickle.load(open("keypair/pub_128.p", "rb"))
    print "public key =", pub
    print "load original dataset..."
    for i in range(nrows):
        items = []
        for j in range(ncols):
            items.append(int(table.cell_value(i, j)))
        print (items)
    print "Encrypted by paillier cryptosystem..."
    print "encrypted dataset..."
    # print (encrypt(pub, int(table.cell_value(0, 0))))
    xls = xlwt.Workbook()
    sheet1 = xls.add_sheet(u'M30-Query-S128_encrypted', cell_overwrite_ok=True)
    start = timeit.default_timer()
    for i in range(nrows):
        citems = []
        for j in range(ncols):
            x = encrypt(pub, int(table.cell_value(i, j)))
            citems.append(str(x))
            sheet1.write(i, j, str(x))
        print (citems)
    xls.save('experiment/encrypted/M30-Query-S128_encrypted.xls')
    elapsed = (timeit.default_timer() - start)
    print "encrypting time is", elapsed, "seconds"


def main():
    write_excel()
    # url = 'http://112.74.181.10:5000/upload'
    #url = 'http://127.0.0.1:5000/upload'
    #filename = 'test_data/test_query_encrypted.xls'
    #sender = 'query_provider'
    #send_excel(url, filename, sender)


if __name__ == "__main__":
    main()
