import hashlib

t = input("text to be encrypted enter : ")
md5 = hashlib.md5(t.encode())

print("Your hashed text: ")
print(md5.hexdigest());
