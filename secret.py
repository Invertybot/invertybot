import hashlib
from settings import SECRET_SALT


def generate_user_hash(user_id, secret_salt=SECRET_SALT):
    str2hash = user_id
    result = hashlib.md5(f"{secret_salt}{str2hash}".encode())
    hash = result.hexdigest()
    return hash