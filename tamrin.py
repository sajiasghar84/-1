تمرین یک 


def encrypt(plain_text, key):
    result = ""
    for ch in plain_text:
        if ch.isalpha() and ch.isascii():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + key) % 26 + base)
        else:
            result += ch  # فاصله و علائم بدون تغییر
    return result


def decrypt(cipher_text, key):
    return encrypt(cipher_text, -key)


text = input("Enter text: ")
key = int(input("Enter key (number): "))

cipher = encrypt(text, key)
print("Encrypted:", cipher)
print("Decrypted:", decrypt(cipher, key))


تمرین دو 

text = input("Enter a string: ")

words = text.split()

# 1. تعداد کلمات
print("Number of words:", len(words))

# 2. تعداد کاراکترها
print("Number of characters:", len(text))

# 3. پرتکرارترین کاراکتر (بدون احتساب فاصله)
counts = {}
for ch in text:
    if ch != " ":
        counts[ch] = counts.get(ch, 0) + 1

if counts:
    most = max(counts, key=counts.get)
    print(f"Most frequent character: '{most}' ({counts[most]} times)")

# 4. تکرار هر کلمه
word_counts = {}
for w in words:
    word_counts[w] = word_counts.get(w, 0) + 1

print("Word frequencies:")
for w, c in word_counts.items():
    print(f"  {w}: {c}")