import hashlib, json, sys

def encrypt(msg=""):
    if type(msg) != str:
        msg = json.dumps(msg, sort_keys=True)

    return hashlib.sha256(str(msg).encode('utf-8')).hexdigest()
