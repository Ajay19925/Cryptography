import itertools

def read_dictionary_file_to_list(filename):
    word_list = []
    with open(filename, 'r') as file:
        for line in file:
            # Remove leading/trailing whitespace and add the word to the list
            word_list.append(line.strip())
    return word_list


def vigenere_decrypt(ciphertext, keyword):
    plaintext = ""
    keyword_length = len(keyword)

    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            # Determine the shift value based on the keyword
            keyword_char = keyword[i % keyword_length]
            shift = ord(keyword_char) - ord('A')

            # Decrypt the character using the shift value
            if char.isupper():
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            else:
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))

            plaintext += decrypted_char
        else:
            plaintext += char

    return plaintext


# Define the ciphertext and keyword
ciphertext = "CTMYRDOIBSRESRRRIJYREBYLDIYMLCCYQXSRRMLQFSDXFOWFKTCYJRRIQZSMX"

alphabet = 'abcdefghijklmnopqrstuvwxyz'

dictionary_file = 'C:/Users/ajayb/Downloads/3-letter-words.txt'
dictionary_word_list = read_dictionary_file_to_list(dictionary_file)
dictionary_word_list = [word.upper() for word in dictionary_word_list]
#print(len(dictionary_word_list))

dictionary_file2 = 'C:/Users/ajayb/Downloads/Oxford_English_Dictionary.txt'
dictionary_word_list2 = read_dictionary_file_to_list(dictionary_file2)
dictionary_word_list2 = [word.upper() for word in dictionary_word_list2]

# Generate all 3-letter English words and store them in a list
three_letter_words = [''.join(p) for p in itertools.product(alphabet, repeat=3)]
three_letter_words = [word.upper() for word in three_letter_words]
#print(three_letter_words)
#keyword = "KEY"  # Replace with the actual 3-letter keyword
decryption_list = []
# Decrypt the ciphertext using the keyword
for keyword in three_letter_words:
    #print(keyword)
    if keyword in dictionary_word_list:
        #print(keyword)
        decrypted_message = vigenere_decrypt(ciphertext, keyword)
        #print("Decrypted Message:")
        #print(decrypted_message)
        count = 0
        for word_to_find in dictionary_word_list2:
            word_index = decrypted_message.find(word_to_find)
            if word_index != -1:
                count += 1
                #print(count)
                if count>8:
                    #print("Decrypted Message:")
                    item = {keyword: decrypted_message}
                    if item not in decryption_list:
                        decryption_list.append(item)
                    #print(decrypted_message)
for item in decryption_list:
    print(item)


#print(decryption_list)