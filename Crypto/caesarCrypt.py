from collections import Counter

offset = 5
input = "Message à encrypter super secret"

# Encrypt given message with Caesar's code
# @param offset : Caesar code offset
# @param message : message to encrypt
# @return encrypted message
def caesarEncrypt(offset, message):
    output = ""
    for ch in (message):
        output += chr(ord (ch) + offset)
    return output

# Decrypt given encryptedMessage with Caesar's code
# @param offset : Caesar code offset
# @param encryptedMessage : message to decrypt
# @return decrypted message
def caesarDecrypt(offset, encryptedMessage):
    output = ""
    for ch in (encryptedMessage):
        output += chr(ord (ch) - offset)
    return output

# Build frequencial table of the encrypted message to find the mosts reccurent letters
# @param encryptedMessage : message to analyse
# @return frequency table
def frequencialAnalyse(encryptedMessage):
    freq = {}
    for keys in encryptedMessage:
        freq[keys] = freq.get(keys, 0) + 1
    return freq

# Find most reccurent letter from given frequencyTable
# @param freq : frequencyTable
# @return most reccurent letter
def findMostReccurentLetter(freq):
    index=0
    reccurence = 0
    for pairIndex in (freq):
        if(reccurence <= freq[pairIndex]):
            index = pairIndex
            reccurence = freq[pairIndex]
    return index


print("\n###### encrypt/decrypt ######\n")
encryptedMessage = caesarEncrypt(offset, input)
print(encryptedMessage)
print(caesarDecrypt(offset, encryptedMessage))

print("\n###### brut force ######\n")
for i in range (25):
    decrypted = caesarDecrypt(i+1, encryptedMessage)
    if(input == decrypted):
        print("found at offset : " + str(i+1) + " and message is : " + caesarDecrypt(i+1, encryptedMessage))

print("\n###### frequencialAnalyse ######\n")
frequencyTable = frequencialAnalyse(encryptedMessage)
print(frequencyTable)
print("The most reccurent letter is : " + findMostReccurentLetter(frequencyTable))