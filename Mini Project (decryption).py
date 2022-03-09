#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Decryption(secret):
    import math
    import string

    p = 47
    q = 53
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 5
    i = 2
    d = int(((i * phi_n) + 1) / e)

    div = math.gcd(phi_n, e)

    public_key = [n, e]
    private_key = d

    letter = dict()
    for index, value in enumerate(string.ascii_lowercase):
        letter[index + 1] = value
    letter.update({27: ' '})
    letter.update({28: ","})
    letter.update({29: "."})
    letter.update({30: ";"})
    letter.update({31: "?"})
    letter.update({32: "!"})
    letter.update({33: "'"})
    letter.update({34: ")"})
    letter.update({35: "("})

    e_msg = []
    secret = secret.replace("[","")
    secret = secret.replace("]","")

    secret = secret.split(",")

    for item in (secret):
        e_msg.append(((int(item) ** int(private_key)) % n))

    decrypted_msg = ""
    for number in (e_msg):
        decrypted_msg = decrypted_msg + letter[number]

    return decrypted_msg


secret = input("Please write a secret message you want decrypted:")

temp = Decryption(secret)
print(temp)

