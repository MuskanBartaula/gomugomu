from hashlib import sha1
import random
from django.utils.encoding import smart_bytes
from six import text_type


def generate_sha1(string, salt=None):

    if not isinstance(string, (str, text_type)):
        string = str(string)

    if not salt:
        salt = sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]

    salted_bytes = (smart_bytes(salt) + smart_bytes(string))
    hash_ = sha1(salted_bytes).hexdigest()

    return salt, hash_


def generate_activation_key(email):
    _, activation_key = generate_sha1(email)
    return activation_key