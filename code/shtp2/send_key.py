#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Author: ClarkYAN -*-

import requests
import timeit


def send_key(url, filename, sender, receiver):
    start = timeit.default_timer()
    files = {'dataset': open(filename, 'rb')}
    user_info = {'name': sender}
    r = requests.post(url, data=user_info, files=files, headers={'Connection': 'close'})
    print sender, "sends public key to ", receiver, " ...", r.text
    elapsed = (timeit.default_timer() - start)
    print "sending time is", elapsed, "seconds"