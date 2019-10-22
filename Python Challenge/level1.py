string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def decipher(string):
    new_string = ''
    for char in string:
        if char == 'y':
            new_string += 'a'
        elif char == 'z':
            new_string += 'b'
        elif ord(char) >= 97 and ord(char) <= 120:
            new_string += chr(ord(char)+2)
        else:
            new_string += char
    return new_string

def decipher2(string):
    table = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
    return(string.translate(table))
