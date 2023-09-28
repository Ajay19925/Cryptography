def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        #print("Decrypted Message: Modular inverse does not exist")
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def affine_decrypt(ciphertext, a, b):
    decrypted_message = ""
    for char in ciphertext:
        if char.isalpha():
            char_value = ord(char) - ord('A')
            try:
                plaintext_value = (modinv(a, 26) * (char_value - b)) % 26
                decrypted_char = chr(plaintext_value + ord('A'))
                decrypted_message += decrypted_char
            except Exception as e:
                continue
                #print("Error:", e)
        else:
            decrypted_message += char
    return decrypted_message

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_affine_encryption(plaintext, ciphertext, a, b):
    # Define the alphabet (assuming uppercase letters)
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Calculate the expected values for 'T' and 'O'
    t_expected = (a * alphabet.index('T') + b) % 26
    o_expected = (a * alphabet.index('O') + b) % 26

    # Calculate the actual values for the given ciphertext
    t_actual = alphabet.index(ciphertext[plaintext.index('T')])
    o_actual = alphabet.index(ciphertext[plaintext.index('O')])

    # Check if the actual values match the expected values
    return t_expected == t_actual and o_expected == o_actual

# Find prime numbers between 1 and 26
possible_a_values = [num for num in range(1, 27) if is_prime(num)]

print("Prime numbers between 1 and 26:", possible_a_values)

ciphertext = "QJKESREOGHGXXREOXEO"

for a in possible_a_values:
    #print(a)
    for b in range(1,27):
        #print(b)
        decrypted_message = affine_decrypt(ciphertext, a, b)
        if "T" in decrypted_message and "O" in decrypted_message:
            result = is_affine_encryption(decrypted_message, ciphertext, a, b)
            if result:
                #print("T is encrypted to H, and O is encrypted to E.")
                print("a: ",a,"b: ",b,"Decrypted Message:", decrypted_message)
            else:
                print("T and O are not encrypted as expected.")









