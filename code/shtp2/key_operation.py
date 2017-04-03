#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Author: ClarkYAN -*-

from paillier.paillier import *
from send_key import *

import pickle


def generate_key():
    print "Generating keypair..."
    priv, pub = generate_keypair(128)
    pickle.dump(pub, open("keypair/pub_128.p", "wb"))
    pickle.dump(priv, open("keypair/priv_128.p", "wb"))
    #files = pickle.load(open("keypair/pub_128.p", "rb"))
    #print files


def send_public_key():
    url = 'http://127.0.0.1:6000/upload'
    filename = 'keypair/pub_128.p'
    sender = 'SHTP2'
    receiver = 'Query Provider' #'Data Owner 1'
    send_key(url, filename, sender, receiver)


def main():
    #generate_key()
    send_public_key()

if __name__ == "__main__":
    main()