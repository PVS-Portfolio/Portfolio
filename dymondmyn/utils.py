from copy import deepcopy
from datetime import datetime
from os.path import exists

from resources import ENCODINGS

def get_datetime_string(raw=False):
    now = str(datetime.now())
    if raw:
        return now
    now = now[:now.index('.')]
    now = now.replace('-', '')
    now = now.replace(' ', '')
    now = now.replace(':', '')
    return now

def get_bytes_from_file(filename):
    if not exists(filename):
        return None
    with open(filename, 'rb') as f:
        s = f.read()
    return s

def get_decoded(obj, enc):
    try:
        return obj.decode(enc)
    except:
        return None

def get_encoded(obj, enc):
    try:
        return obj.encode(enc)
    except:
        return None

def encoding_search(filename, term):
    results = []
    s = get_bytes_from_file(filename)
    for enc1 in ENCODINGS:
        dec_copy = deepcopy(s)
        dec_copy = get_decoded(dec_copy, enc1)
        if dec_copy is None:
            continue
        for enc2 in ENCODINGS:
            if enc1 is enc2:
                continue
            enc_copy = get_encoded(dec_copy, enc2)
            if enc_copy is None:
                continue
            if term in str(enc_copy):
                results.append([enc1, enc2, str(enc_copy)])
    return results

# s = 'C:\\Users\\pvshe\\Desktop\\PicoCTF\\Transformation\\enc'
