from cryptography.fernet import Fernet

atslega = Fernet.generate_key()
print(atslega)

a = Fernet(atslega)

teksts =  b'Slepeni dati'

sifDati = a.encrypt(teksts)
print(sifDati)

print(a.decrypt(sifDati))
