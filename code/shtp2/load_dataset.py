#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Author: ClarkYAN -*-

import xlrd


def open_db(filename):
    try:
        data = xlrd.open_workbook(filename)
        return data
    except Exception, e:
        print str(e)


def read_excel(filename):
    data = open_db(filename)
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
