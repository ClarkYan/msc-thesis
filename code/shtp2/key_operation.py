#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Author: ClarkYAN -*-

from paillier.paillier import *

import pickle


def generate_key():
    print "Generating keypair..."
    priv, pub = generate_keypair(128)
    pickle.dump(pub, open("pub.p", "wb"))
    pickle.dump(priv, open("priv.p", "wb"))


def send_public_key(sender):
    print "Send public key to", sender, "...."


def main():
    generate_key()
    send_public_key()

if __name__ == "__main__":
    main()