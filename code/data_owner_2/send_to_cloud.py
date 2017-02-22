#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Author: ClarkYAN -*-

import requests
import timeit


def send_excel(url, filename, sender):
    start = timeit.default_timer()
    files = {'dataset': open(filename, 'rb')}
    user_info = {'name': sender}
    r = requests.post(url, data=user_info, files=files, headers={'Connection': 'close'})
    print sender, "sends encrypted dataset to SHTP1...", r.text
    elapsed = (timeit.default_timer() - start)
    print "sending time is", elapsed, "seconds"
