def decode(encoded_pw):
    pw = ''
    for d in encoded_pw:
        d = int(d)
        d -= 3
        d = str(d)
        pw += d
    return pw

