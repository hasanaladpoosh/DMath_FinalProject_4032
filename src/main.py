import random
import math
from pickle import GLOBAL


def is_prime(n):
    k=20
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for __ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_large_prime(bit):
    while True:
        n = random.getrandbits(bit)
        if is_prime(n):
            return n

def generate_publickey():
    while True:
        e=generate_large_prime(512)
        if (math.fmod(T,e)!=0 and e<T):
            return e

def generate_privatekey():
    return pow(E,-1,T)

def Encryption():
    return pow(Message,E,N)

def Decryption():
    return pow(Cipher,D,N)



P = generate_large_prime(512)
Q= generate_large_prime(512)
global N
N = P * Q
global T
T=(P - 1) * (Q - 1)
global E
global D
E=generate_publickey()
D=generate_privatekey()
global Message
global Cipher
print(f"N: {N}\nT: {T}\nE: {E}\nD: {D}\n")
while(True):
    print("1-Message->Cipher\n2-Cipher->Message")
    Input=int(input())
    if Input == 1:
        Message=int(input("Enter Message :"))
        print(Encryption())
    elif Input == 2:
        Cipher = int(input("Enter Cipher :"))
        print(Decryption())
    else :
        break







