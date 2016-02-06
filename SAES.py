#http://ict.siit.tu.ac.th/~sgordon/reports/simplified-aes-example.pdf

plaintext = bin(1101011100101000)
key = "0100101011110101"

def binaryxor(binaryone, binarytwo):
    a = "0"
    b = "1"
    y = int(a,2) ^ int(b,2)
    xorbinary = '{0:b}'.format(y)
#http://www.nku.edu/~christensen/2015%20JMM%20SAES.pdf - page 2
#hacky af but this is for fun and i don't understand s-boxes yet
def sbox(binaryone):
    strbinary = str(binaryone)
    if strbinary == "0000":
        binaryoutput = "1001"
    elif strbinary == "0001":
        binaryoutput = "0100"
    elif strbinary == "0010":
        binaryoutput = "1010"
    elif strbinary == "0011":
        binaryoutput = "1011"
    elif strbinary == "0100":
        binaryoutput = "1101"
    elif strbinary == "0101":
        binaryoutput = "0001"
    elif strbinary == "0110":
        binaryoutput = "1000"
    elif strbinary == "0111":
        binaryoutput = "0101"
    elif strbinary == "1000":
        binaryoutput = "0010"
    elif strbinary == "1001":
        binaryoutput = "0000"
    elif strbinary == "1010":
        binaryoutput = "0011"
    elif strbinary == "1011":
        binaryoutput = "1100"
    elif strbinary == "1100":
        binaryoutput = "1110"
    elif strbinary == "1101":
        binaryoutput = "1110"
    elif strbinary == "1110":
        binaryoutput = "1111"
    elif strbinary == "1111":
        binaryoutput = "0111"
    else:
        print "s-boxes are rekt"
    return binaryoutput
def wordgenerator():
    sbox()

def keygenerator():
    keysplitter()
    subkeya = word1
    wordgenerator()
    nibblerotator()
    return subkeya, subkeyb, subkeyc

binaryxor()

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
    return None