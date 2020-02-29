import hashlib

def encode_func(filepath):
    with open(filepath, 'r') as f:
        text = f.read()
    key = [0x10, 0x11, 0x12, 0x13, 0x14, 0x15]
    key_num = 0
    flag = 3
    encode = ""

    for code in text:
        encode = encode + chr(ord(code)^key[key_num])
        if key_num/2 == 0:
            if flag != 0:
                flag = flag - 1
                continue
            flag = 3
        key_num = (key_num + 1)%len(key)

    print(hashlib.md5(text.encode(encoding='UTF-8')).hexdigest())

    with open(filepath, 'w') as f:
        f.write(encode)
