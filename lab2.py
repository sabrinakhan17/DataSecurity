from pip._vendor.distlib.compat import raw_input
import csv

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def generateKey(column, row):
  alph = ord('a')
  index = ((ord(column) - alph) + (ord(row) - alph)) % 26
  return chr(alph + index)

def encrypt(string, key):
  ciphertext = ''
  key_index = 0
  for letter in string.lower():
    if ord(letter) in range(ord('a'), ord('z') + 1):
      ciphertext += generateKey(letter, key[key_index % len(key)].lower())
      key_index += 1
    else:
      ciphertext += letter
  return ciphertext

def reverse(column, target):
  x = ord('a')
  index = ((ord(column) - x) - (ord(target) - x)) % 26
  return chr(x + index)

def decrypt(cipher, key):
  m = ''
  key_index = 0
  for letter in cipher.lower():
    if ord(letter) in range(ord('a'), ord('z') + 1):
      m += reverse(letter, key[key_index % len(key)].lower())
      key_index += 1
    else:
      m += letter
  return m

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

def showResult(string, key):
    print('Plaintext: '+string)
    print('Key: '+key)
    ciphertext = encrypt(string, key)
    print('Encryption: '+ciphertext)
    decrypted = decrypt(ciphertext, key)
    print('Decryption: '+decrypted)
    ciphertextonlyattack()

def main():
    while True:
        string = raw_input('Enter a string to encrypt:')
        key = raw_input('Enter a keyword or -1 to Quit:')
        if key == '-1':
            print('QUIT')
            break
        showResult(string, key)

main()