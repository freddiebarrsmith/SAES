plaintext = bin(1101011100101000)
key = "0100101011110101"

def binaryxor(binaryone, binarytwo):
    a = "11011111101100110110011001011101000"
    b = "11001011101100111000011100001100001"
    y = int(a,2) ^ int(b,2)
    print '{0:b}'.format(y)

def keygenerator():
    keysplitter()
    subkeya = word1
    nibblerotator()
    return subkeya, subkeyb, subkeyc

def keysplitter():
    word0 = key[:8]
    word1 = key[8:]
    print word0
    print word1
    return word0, word1

keysplitter()

def nibblerotator():
    return None
def encrypter():
    addroundkey()
    mainround()
    finalround()
    return ciphertext

def addroundkey():
    return None
def mainround():
    return None
def finalround():
    return NOne