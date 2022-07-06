# 2021 edit
# this file was originally named encoder 3.0, therefor based on its time of creation this will now be named enc 1.3
# 2021 edit

#ISSUE: rand alphabet only has 51 of 52 letters#
#MAKE RAND LETTER ALPHABET CHOOSABLE#

#NEW LETTER ALPHA CREATOR#

import string
import random

all_chars = list(string.ascii_letters)
random.shuffle(all_chars)
alpha1 =  (''.join(all_chars[:52]))

#END#

print("THIS IS THE ENCODER")
print("COPYRIGHT RAPIDSLAYER101")
text_changes = input("what text do you want to encode\n")



# Python3 code to remove whitespace

def remove(string):
    return string.replace(" ", "_")

number = int(input("what shift would you like to use?\n"))


def letter_to_number(letter):
    letters = alpha1
    # Find the number corresponding to the given letter.
    # In this case a = 0, b = 1, c = 2, ..., z = 26.
    number = letters.index(letter)
    return number

print("----------------------------------------------------------------------------------------------------------------") #P1#
print("using standard alphabet:     abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
print("to rand alphabet:           ", alpha1)

def number_to_letter(index):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Finds the letter corresponding to the given number.
    # In this case 0 = a, 1 = b, 2 = c, ..., 26 = z.
    return letters[index]

def shift(letter):
    if letter.isalpha():
        n = letter_to_number(letter)
        return number_to_letter((n + number) % 52)
    else:
        return letter


def rot1(string):
    ciphertext = ""
    # Creates the cipher text one step at at time
    for letter in string:
        ciphertext += shift(letter)

    return ciphertext


print("shift", number, "chosen")
print("with", rot1)
print("----------------------------------------------------------------------------------------------------------------") #P2#




print("----------------------------------------------------------------------------------------------------------------") #P3#

# Driver Program
print("starting encrytion")
string = text_changes
print((remove(string)))
ciphertext = (remove(string))







plaintext = rot1(ciphertext)

# Python3 code to demonstrate working of
# Converting String to binary
# Using join() + ord() + format()

# initializing string
test_str = plaintext

# printing original string
print(str(test_str))

# using join() + ord() + format()
# Converting String to binary
res = ''.join(format(ord(i), 'b') for i in test_str)

# printing result
print(str(res))
encrypts2 = str(res)

#BASE 64#

import zlib, base64
# encoding the text
code =  base64.b64encode(zlib.compress(encrypts2.encode('utf-8'),9))
code = code.decode('utf-8')
print(code)

# decode the encoded text
decoded_txt = zlib.decompress(base64.b64decode(code))
#BASE 64#

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------") #P3#
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------") #P3#
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------") #2#
print("this is your alphabet decrytion key", alpha1)
print("This is your encrypted text:", code)
print("this is your encrypted text with its decryption key:")
print()
print(alpha1, code)
print()
print("left click the text 3 times to highlight it, then cntrl c to copy it")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------") #P3#
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------") #P3#









print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------") #P4#

print("THIS IS THE DECODING TEST")
print("enter the encrypted text you wish to check")
dataharvestORI = input()

print("----------------------------------------------------------------------------------------------------------------") #P3#

alphainput = dataharvestORI[0:52]
dataharvest2 = dataharvestORI[52:]


print("decryption key:", alphainput)

print("encoded data:", dataharvest2)

decoded_txt2 = zlib.decompress(base64.b64decode(dataharvest2))
print("uncompressed data:", decoded_txt)



decrypttext = decoded_txt2
bin_data = encrypts2

# Python3 code to demonstrate working of
# Converting binary to string
# Using BinarytoDecimal(binary)+chr()

#END#

# Defining BinarytoDecimal() function
def BinaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return (decimal)

# Driver's code
# initializing binary data
bin_data = decrypttext

print("----------------------------------------------------------------------------------------------------------------") #P3#
dataharvest1 = int(input("what shift would you like to use?\n"))
print("shift key:", dataharvest1)
# print binary data
print("decrypting", decrypttext)


# initializing a empty string for
# storing the string data
str_data = ' '

# slicing the input and converting it
# in decimal and then converting it in string
for i in range(0, len(bin_data), 7):
    # slicing the bin_data from index range [0, 6]
    # and storing it as integer in temp_data
    temp_data = int(bin_data[i:i + 7])

    # passing temp_data in BinarytoDecimal() fuction
    # to get decimal value of corresponding temp_data
    decimal_data = BinaryToDecimal(temp_data)

    # Deccoding the decimal value returned by
    # BinarytoDecimal() function, using chr()
    # function which return the string corresponding
    # character for given ASCII value, and store it
    # in str_data
    str_data = str_data + chr(decimal_data)

# printing the result
print(str_data)

# Python3 code to remove whitespace

def remove2(string):
    return string.replace("_", " ")


# Driver Program
string = str_data
print((remove2(string)))
str_data2 = (remove2(string))

number2 = dataharvest1

def letter_to_number2(letter):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Find the number2 corresponding to the given letter.
    # In this case a = 0, b = 1, c = 2, ..., z = 26.
    number2 = letters.index(letter)
    return number2


def number2_to_letter(index):
    letters = alphainput
    # Finds the letter corresponding to the given number2.
    # In this case 0 = a, 1 = b, 2 = c, ..., 26 = z.
    return letters[index]


def shift(letter):
    if letter.isalpha():
        n = letter_to_number2(letter)
        return number2_to_letter((n + number2) % 52)
    else:
        return letter


def rot1(string):
    ciphertext = ""
    # Creates the cipher text one step at at time
    for letter in string:
        ciphertext += shift(letter)

    return ciphertext

print("with", rot1)

ciphertext = str_data2

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------") #P3#
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------") #P3#
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------") #P3#
plaintext = rot1(ciphertext)
print("here is your decryted text:", plaintext)
print("this should be the same as what you were trying to encode")
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------") #P3#
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------") #P3#
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------") #P3#








#END#
#add exit maybe#
#END#





import zipimport



print("please name the file you would like to create with your encrypted data:")
filename0 = input()

print("----------------------------------------------------------------------------------------------------------------")
print("creating encrypted file")
writeinfile1 = alpha1
writeinfile2 = encrypts2

print("----------------------------------------------------------------------------------------------------------------")

ListOfLines = [writeinfile1, writeinfile2]


# Function to create our test file
def createFile():
    print("writing")
    wr = open(filename0, "w")
    for line in ListOfLines:
        # write all lines
        wr.write(line)
        wr.write("\n")
    wr.close()

    print("----------------------------------------------------------------------------------------------------------------")
# Function to demo the readlines() function
def readFile():
    print("file info")
    f = open(filename0, "r")
    print(f)
    print("reading your file")
    print("")
    rd = open(filename0, "r")

    # Read list of lines
    out = rd.readlines()

    # Close file
    rd.close()

    return out

print("----------------------------------------------------------------------------------------------------------------")

# Main test
def main():
    # create Logs.txt
    createFile()

    # read lines from Logs.txt
    outList = readFile()

    # Iterate over the lines
    for line in outList:
        print(line.strip())

    # Run Test


if __name__ == "__main__":
    main()

print("----------------------------------------------------------------------------------------------------------------") #3#
print("----------------------------------------------------------------------------------------------------------------") #3#
print("----------------------------------------------------------------------------------------------------------------") #3#
print("----------------------------------------------------------------------------------------------------------------") #3#
print("----------------------------------------------------------------------------------------------------------------") #3#
print("you have succefully created an encrypted message and created a file containing the encrypted text")
print("you file will be avaliable once this program is stopped")
print("to get your file look on the left hand pannel for the name you typed for the file")
print("----------------------------------------------------------------------------------------------------------------") #3#
print("----------------------------------------------------------------------------------------------------------------") #3#
print("----------------------------------------------------------------------------------------------------------------") #3#
print("----------------------------------------------------------------------------------------------------------------") #3#
print("----------------------------------------------------------------------------------------------------------------") #3#


#END

print("the rest of this program just checks whats written in your file")
input()
#END#

print("please type the name of a file:")
print("opening a file that does not exist will result in an error")

writefile = input()
print("file info")
filedetails = open(writefile, "w+")
print(filedetails)

print("what would you like to overwrite in the file?")
print("click enter to go to next line")
writeinfilee1 = input()
writeinfilee2 = input()
writeinfilee3 = input()
writeinfilee4 = input()
writeinfilee5 = input()
print("----------------------------------------------------------------------------------------------------------------")

ListOfLines = [writeinfilee1, writeinfilee2, writeinfilee3, writeinfilee4, writeinfilee5]


# Function to create our test file
def createFile():
    print("writing")
    wr = open(writefile, "w+")
    for line in ListOfLines:
        # write all lines+
        wr.write(line)
        wr.write("\n")
    wr.close()

# Function to demo the readlines() function
print("----------------------------------------------------------------------------------------------------------------") #1#

print("please type the name of a file:")
print("opening a file that does not exist will result in an error")

var = input()

def readfile1():
    print("file info")
    filedetails = open(var, "r")
    print(filedetails)

    print("reading your file")
    print("")
    rd = open(var, "r")

    rd = open(var, "r")

    # Read list of lines
    wurds = rd.readlines()

    return wurds

# Close file
readfile1()

#END#
exit()
#END#

number = int(input("what shift do you want?\n positive 1-26 = encode\n negative 1-26 = decode\n"))


def letter_to_number(letter):
    letters = "abcdefghijklmnopqrstuvwxyz"
    # Find the number corresponding to the given letter.
    # In this case a = 0, b = 1, c = 2, ..., z = 26.
    number = letters.index(letter)
    return number


def number_to_letter(index):
    letters = "abcdefghijklmnopqrstuvwxyz"
    # Finds the letter corresponding to the given number.
    # In this case 0 = a, 1 = b, 2 = c, ..., 26 = z.
    return letters[index]


def shift(letter):
    if letter.isalpha():
        n = letter_to_number(letter)
        return number_to_letter((n + number) % 26)
    else:
        return letter


def rot1(string):
    ciphertext = ""
    # Creates the cipher text one step at at time
    for letter in string:
        ciphertext += shift(letter)

    return ciphertext


ciphertext = input("what text do you want to encode/decode\n")

plaintext = rot1(ciphertext)

print(plaintext)

input('Press enter to exit.')
