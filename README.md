# MSc-Thesis
## Efficient K-Nearest Neighbor Classification Algorithm on Encrypted Data
SKNNS (Secure K-Nearest Neighbor Scheme) model is a secure scheme for implementing a whole structure of the privacy preserving k-NN algorithm

## Keywords
Security, K-NN Query, Encrypted Data, Privacy Preserving Data Mining, Cryptosystem

## INTRODUCTION
Cloud computing is an emerging computing paradigm that attracts many companies and organizations to make a decision about utilizing the benefits of a cloud to achieve a better data cost management solution. As a cloud concern, a customer (a data owner) outsources his or her own databases to the cloud and provides the access authority of managing and mining the related databases on cloud is a very complexity process in Information Security research area. Our secure model SKNNS is focus on providing an approach to implement a privacy preserving data mining protocol while mining the encrypted data directly

## SECURE K-NEAREST NEIGHBOR SCHEME MODEL
* Protocol 1 K-NN Classification Algorithm: KNN(X, Y)
* Protocol 2 Paillier Cryptosystem Algorithm: PCA(X, Y, Q)
* Protocol 3 Secure Multiplication: SM{Ek(X), Ek(Y)} → Ek(X * Y)
* Protocol 4 Secure Squared Euclidean Distance: SSED{Ek(X),Ek(Y)}→Ek{(X−Y)2}
* Protocol 5 Secure Selection of K-Nearest Neighbors: SSOKNN{Ek(X),Ek(Y),Ek(Q)} → Tmin{1,2,3...k}
* Protocol 6 More Secure Selection of K-Nearest Neighbors: MSSOKNN{Ek(X),Ek(Y),Ek(Q)} → Tmin{1,2,3...k}

## Future work
Now you have finished all the required steps. You can do the further analysis as you wish.
If you've encounted any problems, please do not hesitate to send an email to [Clark YAN (me)](https://github.com/ClarkYan) at clarkyan1993@gmail.com or opening an issue on github.
