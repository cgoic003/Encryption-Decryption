#!/usr/bin/env python
# coding: utf-8

# In[5]:


secret = input("Please write a secret message you want encrypted:")

def Encryption(secret):
    
    import math
    import string
    
    
    p = 47
    q = 53
    n = p * q
    phi_n = (p-1)*(q-1) 
    e = 5
    i = 2
    d = int(((i * phi_n) + 1)/e)
    
    div = math.gcd(phi_n, e)
    
    public_key = [n, e]
    private_key = d
    
    values = dict()
    for index, letter in enumerate(string.ascii_lowercase):
         values[letter] = index + 1
    values.update({' ':27})
    values.update({",":28})
    values.update({".":29})
    values.update({";":30})
    values.update({"?":31})
    values.update({"!":32})
    values.update({"'":33})
    values.update({")":34})
    values.update({"(":35})
    
    message = secret.lower()
    
    encrypted_msg = []
    
    for item in (message):
        encrypted_msg.append(((values[item]**e))%n)
    
    return (encrypted_msg)
temp = Encryption(secret)
print(temp)


# In[ ]:




