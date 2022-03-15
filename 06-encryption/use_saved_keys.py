import os

import rsa

current_dir = os.path.dirname(__file__)
print(current_dir)

public_file = open(current_dir + "/keys/public.txt", "r")
public_data = public_file.read()
public_key = rsa.PublicKey.load_pkcs1(public_data, 'PEM')

print(public_key)

private_file = open(current_dir + "/keys/private.txt", "r")
private_data = private_file.read()
private_key = rsa.PrivateKey.load_pkcs1(private_data, 'PEM')

print(private_key)