import datetime, re
from time import time
from os import path
from random import choice
from base64 import b85encode, b85decode
from hashlib import sha512
from zlib import compress, decompress
from multiprocessing import Pool, cpu_count

# enc 9.2.0 - CREATED BY RAPIDSLAYER101 (Scott Bree)
ascii_set = """0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~"""  # base85
block_size = 2000000  # todo smart block size allocation


def hex_gens(num):
    hex_gens_ = ""
    while len(hex_gens_) != int(num):
        hex_gens_ += choice(ascii_set)
    return hex_gens_


conv_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a',
             11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: "g", 17: "h", 18: "i", 19: "j", 20: "k",
             21: "l", 22: "m", 23: "n", 24: "o", 25: "p", 26: "q", 27: "r", 28: "s", 29: "t", 30: "u",
             31: "v", 32: "w", 33: "x", 34: "y", 35: "z", 36: "A", 37: 'B', 38: 'C', 39: 'D', 40: 'E',
             41: 'F', 42: "G", 43: "H", 44: "I", 45: "J", 46: "K", 47: "L", 48: "M", 49: "N", 50: "O",
             51: "P", 52: "Q", 53: "R", 54: "S", 55: "T", 56: "U", 57: "V", 58: "W", 59: "X", 60: "Y",
             61: "Z", 62: "¬", 63: "`", 64: "!", 65: "\"", 66: "£", 67: "$", 68: "%", 69: "^", 70: "&",
             71: "*", 72: "(", 73: ")", 74: "-", 75: " ", 76: "=", 77: "+", 78: "[", 79: "{", 80: "]",
             81: "}", 82: ";", 83: ":", 84: "'", 85: "@", 86: "#", 87: "~", 88: "\\", 89: "|", 90: ",",
             91: "<", 92: ".", 93: ">", 94: "/", 95: "?"}

conv_dict_back = {v: k for k, v in conv_dict.items()}


def to_hex(base_fr, base_to, hex_to_convert):
    decimal = 0
    power = len(hex_to_convert)-1
    for digit in hex_to_convert:
        decimal += conv_dict_back[digit]*base_fr**power
        power -= 1
    hexadecimal = ''
    while decimal > 0:
        remainder = decimal % base_to
        hexadecimal = conv_dict[remainder]+hexadecimal
        decimal = decimal // base_to
    return hexadecimal


def to_number(hex_to_convert):
    decimal = ""
    for digit in hex_to_convert:
        decimal += str(conv_dict_back[digit])
    return decimal


def get_hex_base(hex_to_check):  # this is only a guess
    for i in range(96):
        if to_hex(i+2, i+2, hex_to_check) == hex_to_check:
            return i+2


def pass_to_seed(password, salt):
    salt = sha512(sha512(b85encode(salt.encode())).hexdigest().encode()).hexdigest()
    inp = f"{salt[:64]}{password}{salt[64:]}"
    return to_hex(16, 96, sha512(sha512(b85encode(inp.encode())).hexdigest().encode()).hexdigest())


def seed2_to_alpha(seeds):  # this function requires 171 numbers
    alpha_gen = ascii_set
    counter = 0
    alpha = ""
    while len(alpha_gen) > 0:
        counter += 2
        value = int(str(seeds)[counter:counter+2])*2
        while value > len(alpha_gen)-1:
            value = value // 2
        if len(str(seeds)[counter:]) < 2:
            alpha += alpha_gen
            alpha_gen = alpha_gen.replace(alpha_gen, "")
        else:
            chosen = alpha_gen[value]
            alpha += chosen
            alpha_gen = alpha_gen.replace(chosen, "")
    return alpha


def seed_to_data(seed):
    return seed2_to_alpha(int(to_hex(96, 16, seed), 36)), to_hex(10, 96, str(int(to_hex(96, 16, seed), 36)))


def shifter(plaintext, shift_num, alphabet, forwards):
    alphabet2 = alphabet*3
    output_enc = ""
    counter = 0
    if forwards:
        for char in plaintext:
            counter += 2
            output_enc += alphabet2[alphabet.index(char)+int(shift_num[counter:counter+2])]
    else:
        for char in plaintext:
            counter += 2
            output_enc += alphabet2[alphabet.index(char)-int(shift_num[counter:counter+2])]
    return output_enc


def get_file_size(file):
    file_size_kb = path.getsize(file)/1024
    if file_size_kb > 9999:
        file_size_mb = file_size_kb/1024
        if file_size_mb > 750:
            print("This file is not supported due to its large size, the max is 750MB")
            return "NOTSUP"
        else:
            return f"{round(file_size_mb,2)}MB"
    else:
        return f"{round(file_size_kb,2)}KB"


def encrypt_block(data, block_num, alpha, shift_num, enc, send_end=None):
    print(f"Block {block_num} launched")
    if enc == "enc":
        if type(data) == bytes:
            block = shifter(b85encode(compress(data, 9)).decode('utf-8'), str(shift_num), alpha, True)
        else:
            block = shifter(b85encode(compress(data.encode('utf-8'), 9))
                            .decode('utf-8'), str(shift_num), alpha, True)
    if enc == "dec":
        output_end = shifter(data, str(shift_num), alpha, False).replace(" ", "")
        block = decompress(b85decode(output_end))
        try:
            block = block.decode('utf-8')
        except UnicodeDecodeError:
            pass
    print(f"Block {block_num} complete")
    if send_end:
        send_end.send(block)
    else:
        return block


def encrypt(text, alpha, shift_num, enc):
    shift_num = str(int(to_hex(96, 10, str(shift_num)), 36))
    if enc.lower() in ["enc", "dec"]:
        if enc == "enc":
            e_chunks = [text[i:i+block_size] for i in range(0, len(text), block_size)]
        if enc == "dec":
            if type(text) == list:
                e_chunks = text
            else:
                e_chunks = text.split("¬")
        if len(e_chunks) == 1:
            if enc == "enc":
                if type(text) == bytes:
                    plaintext = b85encode(compress(text, 9)).decode('utf-8')
                else:
                    plaintext = b85encode(compress(text.encode('utf-8'), 9)).decode('utf-8')
                while len(str(shift_num)) < len(plaintext)*2:
                    shift_num += f"{int(str(shift_num)[-2048:], 36)}"
                return shifter(plaintext, str(shift_num), alpha, True)
            if enc == "dec":
                while len(str(shift_num)) < len(text)*2:
                    shift_num += f"{int(str(shift_num)[-2048:], 36)}"
                output_end = shifter(text, str(shift_num), alpha, False).replace(" ", "")
                try:
                    output_end = decompress(b85decode(output_end)).decode('utf-8')
                except UnicodeDecodeError:
                    output_end = decompress(b85decode(output_end))
                return output_end
        else:
            print(f"Launching {len(e_chunks)} threads")
            while len(str(shift_num)) < block_size*2.5:
                shift_num += f"{int(str(shift_num)[-2048:], 36)}"
            pool = Pool(cpu_count())
            result_objects = [pool.apply_async(encrypt_block, args=(e_chunks[x-1], x, alpha, shift_num, enc))
                              for x in range(1, len(e_chunks)+1)]
            pool.close()
            if enc == "enc":
                result_list = [x.get() for x in result_objects]
                pool.join()
                return result_list
            if enc == "dec":
                d_data = b""
                for x in result_objects:
                    new_data = x.get()
                    try:
                        d_data += new_data
                    except TypeError:
                        d_data = ""
                        d_data += new_data
                pool.join()
                return d_data
    else:
        print("ENCRYPTION CANCELLED! Enc type is neither 'enc' or 'dec' please change.")


def encrypt_key(text, key, salt):
    alpha1, shift_num = seed_to_data(pass_to_seed(key, salt))
    return encrypt(text, alpha1, shift_num, "enc")


def encrypt_file(file_to_enc, seed, file_output=None):
    start = time()
    if path.exists(file_to_enc):
        file_name = file_to_enc.split("/")[-1]
        if get_file_size(file_to_enc) == "NOTSUP":
            return "File to large"
        else:
            print(f"{file_name} is {get_file_size(file_to_enc)}")
    else:
        return "File not found"  # todo smart find alternative
    try:
        with open(file_to_enc, 'rb') as hash_file:
            data_chunks = hash_file.read()

        alpha, shift_num = seed_to_data(seed)
        result_list = encrypt(data_chunks, alpha, shift_num, "enc")

        with open(file_output, "w", encoding="utf-8") as f:
            for e_block in result_list:
                f.write(f"¬{e_block}")
        # todo show new "compressed" size
        print(f"ENCRYPTION COMPLETE OF {get_file_size(file_to_enc)} ({block_size}*{len(result_list)})"
              f" IN {round(time() - start, 2)}s")
    except Exception as e:
        print("Error", e)


def decrypt_key(e_text, key, salt):
    alpha1, shift_num = seed_to_data(pass_to_seed(key, salt))
    return encrypt(e_text, alpha1, shift_num, "dec")


def decrypt_file(file_to_dec, seed, file_output=None):  # todo rewrite decrypter
    start = time()
    if path.exists(file_to_dec):
        file_name, file_type = file_to_dec.split("/")[-1].split(".")
        if file_type != "renc":
            return "This is not a renc file"
        else:
            print(f"{file_name} is {get_file_size(file_to_dec)}")
    else:
        return "File not found"  # todo smart find alternative
    with open(file_to_dec, encoding="utf-8") as dec_file:
        e_text = dec_file.read().split("¬")

    alpha, shift_num = seed_to_data(seed)
    d_data = encrypt(e_text[1:], alpha, shift_num, "dec")

    if type(d_data) == bytes:
        with open(f"{file_output}", "wb") as f:
            f.write(d_data)
    if type(d_data) == str:
        with open(f"{file_output}", "w", encoding="utf-8") as f:
            f.write(d_data.replace("\r", ""))
    # todo show new "compressed" size
    print(f"DECRYPTION COMPLETE OF {get_file_size(file_to_dec)} ({block_size}*{len(e_text)-1})"
          f" IN {round(time()-start, 2)}s")


def search(data, filter_fr, filter_to):
    data = str(data)
    m = re.search(f"""{filter_fr}(.+?){filter_to}""", data)
    if m:
        return m.group(1)
    else:
        return None


def get_links(data):
    a = (re.findall(r'(https?://[^\s]+)', str(data)))
    b = (re.findall(r'(http?://[^\s]+)', str(data)))
    c = ('\n'.join(a))
    d = ('\n'.join(b))
    return c+d


def round_tme(dt=None, round_to=30):
    if not dt:
        dt = datetime.datetime.now()
    seconds = (dt.replace(tzinfo=None)-dt.min).seconds
    return dt+datetime.timedelta(0, (seconds+round_to/2)//round_to*round_to-seconds, -dt.microsecond)


def hash_a_file(file):
    read_size = 262144
    hash_ = sha512()
    with open(file, 'rb') as hash_file:
        buf = hash_file.read(read_size)
        while len(buf) > 0:
            hash_.update(buf)
            buf = hash_file.read(read_size)
    return to_hex(16, 96, hash_.hexdigest())
