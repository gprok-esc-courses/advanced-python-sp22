import rsa

public_key, private_key = rsa.newkeys(512)

pub_file = open("keys/public.txt", "w")
pub_file.write(public_key.save_pkcs1().decode('utf8'))
pub_file.close()

pri_file = open("keys/private.txt", "w")
pri_file.write((private_key.save_pkcs1().decode('utf8')))
pri_file.close()
