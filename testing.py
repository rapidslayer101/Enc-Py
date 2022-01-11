import enclib as enc
from zlib import compress, decompress
from base64 import b85encode, b85decode, b64encode, b64decode
import sys, binascii


def b64echeck(master_key):
    while True:
        if len(master_key) % 4 == 0:
            break
        else:
            master_key += "="
    return master_key


#print(output_end)

ascii_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

text = enc.hex_gens(1000000)
text = b64encode(compress(text.encode("utf-8"), 9))

byte_data = (bytearray(text))
print(len(byte_data))

with open("output0.txt", "wb") as f:
    f.write(byte_data)

with open("output1.txt", "wb") as f:
    print(len(binascii.a2b_base64(text)))
    f.write(binascii.a2b_base64(text))

conv_dict = {65: "000001", 66: '000011', 67: '000111', 68: '001111', 69: '011111', 70: '111111',
             71: '111110', 72: '7', 72: '8', 74: '9',
             }

for i in text:
    print(i, conv_dict[i])





input()
text_b85 = b85encode(compress(text.encode('utf-8')))
print(b85encode(text.encode('utf-8')))
print(sys.getsizeof(b85encode(text.encode('utf-8'))))
print(sys.getsizeof(b85encode(text.encode('utf-8')).decode("utf-8")))
print(text_b85)

input()
test_b64 = b64encode(text)
print(test_b64)






input()

ascii_set = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~"
string = enc.hex_gens(2000000)
#string = string * 1000

string = "iosevu nn384/`@>?<:{l]_)})}_$IM"

print(list(string))


def b85s_to_bits(s):
    bin_data = ''.join(format(i, f'07b') for i in bytearray(s, encoding='utf-8'))
    return int(bin_data, 2).to_bytes((len(bin_data)+7) // 8, 'big')


def bits_to_b85s(b):
    bin_data = bin(int.from_bytes(b, byteorder='big')).replace("0b", "")

    def bits_to_string(bts):
        b85s = ""
        for i in range(0, len(bts), 7):
            b85s += chr(int(bts[i:i+7], 2))
        return b85s

    b85s = bits_to_string(bin_data)
    counter = 0
    while True:
        if b85s[counter] not in ascii_set:
            b85s = bits_to_string(f"0{bin_data}")
            break
        if counter == len(b85s) - 1:
            break
        counter += 1
    return b85s


byte_data = b85s_to_bits(string)
print("Converted")


# file
with open("output1", "wb") as f:
    f.write(byte_data)

with open("output0", "w") as f:
    f.write(string)

output = bits_to_b85s(byte_data)
print("Converted")

if output == string:
    print("success")

with open("output2", "w") as f:
    f.write(output)
input("Done")

def b85s_to_bits(s):
    bin_data = ''.join(format(i, f'07b') for i in bytearray(s, encoding='utf-8'))
    return int(bin_data, 2).to_bytes((len(bin_data)+7) // 8, 'big')


def bits_to_b85s(b):
    bin_data = bin(int.from_bytes(b, byteorder='big')).replace("0b", "")

    def bits_to_string(bts):
        b85s = ""
        for i in range(0, len(bts), 7):
            b85s += chr(int(bts[i:i+7], 2))
        return b85s

    b85s = bits_to_string(bin_data)
    counter = 0
    while True:
        if b85s[counter] not in ascii_set:
            b85s = bits_to_string(f"0{bin_data}")
            break
        if counter == len(b85s) - 1:
            break
        counter += 1
    return b85s
