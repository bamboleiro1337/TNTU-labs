# a = '!@#$%^&*()_+=-"№;:?,./\<>|'
# temp = []
# for i in a:
#     temp.append(i)
#     print(temp)

eng_alph = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
            'z', 'x', 'c', 'v', 'b', 'n', 'm']

message = input('Enter a message: ')
key = int(input('Enter your key: ')) % len(eng_alph)

message = message.lower().replace(' ', '')
encrypted_m = ''


for i in message:
    index = (eng_alph.index(i) + key) % len(eng_alph)
    encrypted_m += eng_alph[index]

print('Message: ', message)
print('Encrypted message: ', encrypted_m)

# A little decryptor
# def decryption(encrypted_m, shift):
#     decrypted_m = ""
#     for j in encrypted_m:
#         indexd = (eng_alph.index(j) - shift) % len(eng_alph)
#         decrypted_m += eng_alph[indexd]
#     return decrypted_m

# for n in range(len(eng_alph)):
#     print(f"Спроба {n}: {decryption(encrypted_m, n)}")
