import numpy as np
import secrets

characters = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '.', ',', '!', '?', ':', ';', "'", '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '=', '+', '-', '*', '/', '(', ')', '[', ']', '{', '}', '@', '§', '$', '%', '&', '~', '#', '_', '<', '>', '|', '^', 'ä', 'ö', 'ü', 'Ä', 'Ö', 'Ü', 'ß']

#Functions for encryption/decryption

def addition(a, b):
    if a+b<100:
        return a+b
    else:
        return a+b-100

def subtraction(a, b):
    if a-b>=0:
        return a-b
    else:
        return a-b+100

def key_to_pairs(list_key):
    if len(list_key)%2 != 0:
        list_key = list_key[:-1]
    i=0
    two_key = []
    while i<(len(list_key)-1):
        z = ""
        z += list_key[i] + list_key[i+1]
        i += 2
        two_key.append(int(z))
    return two_key

def text_to_num(list_text):
    text_num = []
    for i in range(len(list_text)):
        text_num.append(characters.index(list_text[i]))
    return text_num
    
def encrypt(key, text):
    global shared_key
    
    list_text = text_to_num(list(text))
    list_key = key_to_pairs(list(key))
    
    if len(list_text)>len(list_key): raise ValueError("The key is not long enough!")
    
    enc_message = ""
    for i in range(len(list_text)):
        if addition(list_key[i], list_text[i])<10:
            enc_message += "0"+str(addition(list_key[i], list_text[i]))
        else:
            enc_message += str(addition(list_key[i], list_text[i]))
    
    shared_key = key[len(text)*2:]
    return enc_message

def decrypt(key, text):
    global shared_key
    
    list_text = key_to_pairs(list(text))
    list_key = key_to_pairs(list(key))
    
    if len(list_text)>len(list_key): raise ValueError("The key is not long enough!")
    
    dec_message = ""
    for i in range(len(list_text)):
        dec_message += characters[subtraction(list_text[i], list_key[i])]
    
    shared_key = key[len(text):]
    return dec_message

def test_if_enc(text):
    count = 0
    for i in range(len(text)):
        if text[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            count += 1
    if count==len(text) and len(text)%2==0: return True
    return False

def messenger(key, text):
    if test_if_enc(text): return decrypt(key, text)
    return encrypt(key, text)

def type_message():
    print("Typ a message:")
    global shared_key
    i=1
    while i>0:
        x = input()
        i = len(x)
        if i==0:
            break
        print(messenger(shared_key, x), "\n")
        print("Percentage of left key:", 100*len(shared_key)/key_length, "%" "\n")


#Creating a key

def secure_key(key_size):
    key = ""
    for i in range(key_size):
        key += str(secrets.randbelow(10))
    return key

key_length = 100000
key_file = open("Key.txt", "w")
key_file.write(secure_key(key_length))
key_file.close()

#Importing a key

key_file = open('Key.txt', 'r')
shared_key = key_file.read()
key_length = len(shared_key)
key_file.close()

type_message()