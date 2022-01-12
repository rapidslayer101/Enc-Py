ascii_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


import time


def random_shift_gen(n, seed):
    return random.randint(int(range_start), int(range_end))



import random

range_start = "1"
range_end = "9"
for i in range(100000-1):
    range_start += "0"
    range_end += "9"


def random_shift_gen(seed):
    random.seed(seed)
    return random.randint(int(range_start), int(range_end))

start = time.time()
seed = "859499301675296405236573260980273730782061627867522602346063064148676518155629499735534929240054252810134897391349811974456251981491889021231694063781962953158900758173755546115281342431265305732296613897834483584749567163619535291147971429337238783927239452574658899537088927247981360992027203354726605615341"
shift_num = str(random_shift_gen(seed))
while len(str(shift_num)) < 2000000 << 1:
    #print(len(shift_num), time.time()-start)
    shift_num += str(random_shift_gen(shift_num[-256:]))
print(time.time()-start)

input()


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


string = "hi"

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
