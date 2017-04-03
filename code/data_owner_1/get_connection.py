#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Author: ClarkYAN -*-

import requests


def set_up_connection(url, sender):
    # files = {'dataset': open(filename, 'rb')}
    user_info = {'name': sender}
    r = requests.post(url, data=user_info, headers={'Connection': 'close'})
    if r.text == "success":
        conn_result = sender, "connect to the cloud"
    else:
        conn_result = sender, "cannot connect to the cloud"
    return conn_result
