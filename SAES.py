from bitstring import *
import binascii
#http://ict.siit.tu.ac.th/~sgordon/reports/simplified-aes-example.pdf
###converting string to binary
####     print "binaryrotnib:"
 #   binaryrotnib = bin(int((introtnib), 2))
 #   print binaryrotnib

plaintext = bin(1101011100101000)
key = "0100101011110101"


def keysplitter():
    word0 = key[:8]
    word1 = key[8:]
    return word0, word1

def binaryxor(binaryone, binarytwo):
    a = "0"
    b = "1"
    y = int(a,2) ^ int(b,2)
    xorbinary = '{0:b}'.format(y)
#http://www.nku.edu/~christensen/2015%20JMM%20SAES.pdf - page 2
#hacky af but this is for fun and i don't understand s-boxes yet
def sbox(binaryone):
    binaryone = str(binaryone)
    binaryonestripped = binaryone.replace("b", "")
    print "binaryone"
    print binaryonestripped
    binaryoutput = 0
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
        binaryoutput = "0010"
    elif strbinary == "1010":
        binaryoutput = "0000"
    elif strbinary == "1011":
        binaryoutput = "0011"
    elif strbinary == "1100":
        binaryoutput = "1100"
    elif strbinary == "1101":
        binaryoutput = "1110"
    elif strbinary == "1110":
        binaryoutput = "1111"
    elif strbinary == "1111":
        binaryoutput = "0111"
    else:
        print "s-boxes are rekt"
    return binaryoutput


#binaryone = "1001"
#result = sbox(binaryone)

#print result
def rotnib():
    #swap the parts around
    wordzero, wordone = keysplitter()
#    print wordone
    print wordone
    wordonenibbleone = wordone[:4]
    wordonenibbletwo = wordone[4:]
    rotnib = wordonenibbletwo + wordonenibbleone
    print "rotnib"
    print rotnib
    return rotnib


def wordgenerator():
    introtnib = rotnib()
    print "introtnib"
 #   introtnib = "'" + introtnib + "'"
  #  print introtnib
  #  print "a.bin"
    ##
#    a = BitArray(bin=introtnib)
#    print a.bin

    subnibvar1 = sbox(introtnib[:4])
    subnibvar2 = sbox(introtnib[4:])
    print "subnib output"
    print subnibvar1
    print subnibvar2
    binarywordzero = bin(int((introtnib), 2))

#    subnibvar = sbox()
#    wordtwo = word0 xor bin(10000000) xor
#    sbox()

wordgenerator()

def keygenerator():
    keysplitter()
    subkeya = word1
    wordgenerator()
    nibblerotator()
    return subkeya, subkeyb, subkeyc

#binaryxor()


rotnib()

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