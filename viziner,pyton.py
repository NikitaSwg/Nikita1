def extend_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return "".join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def shirfv(text, key):
    key = extend_key(text, key)
    cipher_text = []
    for i in range(len(text)):
        if text[i].isalpha():
            base = ord('A') if text[i].isupper() else ord('a')
            key_base = ord('A') if key[i].isupper() else ord('a')
            cipher_char = (ord(text[i]) - base + (ord(key[i]) - key_base)) % 26 + base
            cipher_text.append(chr(cipher_char))
        else:
            cipher_text.append(text[i])

    return "".join(cipher_text)
text = input("введите текст: ")
key = input("ключ: ")

print("зашифрованный текст:", shifrv(text, key))
