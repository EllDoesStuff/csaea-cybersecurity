# Hashing: one way function. Same input --> same output. 

import hashlib

password = "Monkey200"

data = password.encode("utf-8")

digest = hashlib.md5(data).hexdigest()

print(f"Password: {password}")
print(f"Hash: {digest}")

passlist = ["Evi1T1m3", "St1nk7P33n", "a", "SuckleOhnDisVeriDIH"]

for p in passlist:
    data = p.encode("utf-8")
    digest = hashlib.sha256(data).hexdigest()

    print(f"Password: {p}")
    print(f"Hash: {digest}", "\n")