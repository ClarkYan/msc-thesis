#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Author: ClarkYAN -*-

import xlrd


# original squared Euclidean distance method
def squared_euclidean_distance(x, y):
    sed = pow((x - y), 2)
    print "squared_euclidean_distance=", sed
    return sed


def sum_squared_euclidean_distance(x):
    ssed = 0
    ssed = ssed + x
    print "sum is=", ssed
    return ssed


def open_db1(file='test-data/test-db1.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception, e:
        print str(e)


def excel_db1_byindex(file='test-data/test-db1.xls'):
    data = open_db1(file)
    table = data.sheet_by_index(0)
    # rows
    nrows = table.nrows
    # columns
    ncols = table.ncols
    # print "load original dataset..."
    for i in range(nrows):
        items = []
        for j in range(ncols):
            items.append(int(table.cell_value(i, j)))
        return items
        # print (items)


def open_query(file='test-data/test-query.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception, e:
        print str(e)


def excel_query_byindex(file='test-data/test-query.xls'):
    data = open_query(file)
    table = data.sheet_by_index(0)
    nrows = table.nrows  # rows
    ncols = table.ncols  # columns
    # print "load original dataset..."
    for i in range(nrows):
        items = []
        for j in range(ncols):
            items.append(int(table.cell_value(i, j)))
        return items
        # print (items)


def main():
    db1 = excel_db1_byindex()
    query = excel_query_byindex()
    len_db1 = len(db1)
    len_query = len(query)
    print "load original dataset..."
    print "original db1=", db1
    print "the length of db1=", len_db1
    print "the length of query=", len_query


if __name__ == "__main__":
    main()
