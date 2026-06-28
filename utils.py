import hashlib


def hash_password(password):
    """
    Convert a plain text password into a SHA-256 hash.
    """
    return hashlib.sha256(password.encode()).hexdigest()