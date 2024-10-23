def shifr(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char
    return result
text = input("введите текст: ")
shift = int(input("сдвиг: "))

print("зашифрованный текст:", shifr(text, shift))
