import rsa

# Create the keys
public_key, private_key = rsa.newkeys(512)

#print(public_key)
#print(private_key)

message = "Hello World!"

# convert char to bytes
message_bytes = message.encode('utf8')
print(message_bytes)

message_encrypted = rsa.encrypt(message_bytes, public_key)
print(message_encrypted)

message_bytes = rsa.decrypt(message_encrypted, private_key)
original_message = message_bytes.decode('utf8')

print(original_message)

