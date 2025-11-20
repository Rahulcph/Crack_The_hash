from hashlib import md5, sha256, sha512

# target hashes here (the ones printed by createhashes.py)
target_md5   = "a0422524586f950d9f7fb0aef1300159"
target_sha256= "6f829f43e73066f8470d26c85c2480a206ed81504fcb0928fba6db3e12d075b9"
target_sha512= "1a46b502fb91abc306526776b2828f18d6ed4918056b328d5b0116999ca52cbe8c53999dcb3ea1e203204902abf5db9ddf8aa27233b1fb0d8f3ab077a10e2786"

SALT = "ABCDEFG"
LOW, HIGH = 100000, 999999

def find_md5():
    for n in range(LOW, HIGH + 1):
        h = md5((SALT + str(n)).encode()).hexdigest()
        if h == target_md5:
            return n
    return None

def find_sha256():
    for n in range(LOW, HIGH + 1):
        h = sha256((SALT + str(n)).encode()).hexdigest()
        if h == target_sha256:
            return n
    return None

def find_sha512():
    for n in range(LOW, HIGH + 1):
        h = sha512((SALT + str(n)).encode()).hexdigest()
        if h == target_sha512:
            return n
    return None

if __name__ == "__main__":
    print("Starting brute-force (single-threaded)...")
    n1 = find_md5()
    print("MD5 result:", n1)
    n2 = find_sha256()
    print("SHA256 result:", n2)
    n3 = find_sha512()
    print("SHA512 result:", n3)
