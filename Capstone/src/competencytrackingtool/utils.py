import hashlib

def hash_val(val):
    return str(hashlib.sha256(val.encode('utf-8')).hexdigest())
