import csv
import random
from pip._vendor.distlib.compat import raw_input

alphabet = 'abcdefghijklmnopqrstuvwxyz' + ' '

def generateKey():
    newAlphabet = sorted(alphabet, key=lambda s: random.random())
    return dict(zip(alphabet, newAlphabet))

def encrypt(key, plaintext):
    return ''.join(key[i] for i in plaintext)

def decrypt(key, ciphertext):
    decrpytedWord = {v: k for k, v in key.items()}
    return ''.join(decrpytedWord[i] for i in ciphertext)

def ciphertextonlyattack():
    letterFreq = {i:0 for i in alphabet}
    file = "./google-books-common-words.txt"
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")
        sum=0
        for row in reader:
            for j in row[0].lower():
                letterFreq[j] += int(row[1])
                sum=(sum+int(row[1]))

        for k in sorted(letterFreq, key=letterFreq.get, reverse=True):
            print(k, ":", letterFreq[k], ":", str(round(letterFreq[k]/sum*100,2))+'%')

def show_result(plaintext):
    key = generateKey()
    print('\nSubstitution Cipher:\n')
    print('Key: %s' % generateKey())
    print('Plaintext: %s' % plaintext)
    ciphertext = encrypt(key, plaintext)
    print("Encrypted: "+ciphertext)
    decrypted = decrypt(key, ciphertext)
    print("Decrypted: "+decrypted)
    print('\nCiphertext Only Cipher:\n')
    ciphertextonlyattack()

def main():
    while True:
        user = raw_input('Enter a string to encrypt or -1 to Quit:')
        plaintext = user
        if plaintext == '-1':
            print('QUIT')
            break
        show_result(plaintext)

main()