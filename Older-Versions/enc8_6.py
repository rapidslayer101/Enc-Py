import datetime, re
from time import time
from os import path
from random import choice
from base64 import b85encode, b85decode
from hashlib import sha512
from zlib import compress, decompress
from multiprocessing import Process, Pipe

# enc 8.6.0 - CREATED BY RAPIDSLAYER101 (Scott Bree)  # THIS IS ENC 9.0 WIP
ascii_set = """0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~""" # base85
block_size = 2000000  # todo smart block size allocation


def hex_gens(num):
    hex_gens_ = ""
    while len(hex_gens_) != int(num):
        hex_gens_ += choice(ascii_set)
    return hex_gens_


conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a',
                    11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: "g", 17: "h", 18: "i", 19: "j", 20: "k",
                    21: "l", 22: "m", 23: "n", 24: "o", 25: "p", 26: "q", 27: "r", 28: "s", 29: "t", 30: "u",
                    31: "v", 32: "w", 33: "x", 34: "y", 35: "z", 36: "A", 37: 'B', 38: 'C', 39: 'D', 40: 'E',
                    41: 'F', 42: "G", 43: "H", 44: "I", 45: "J", 46: "K", 47: "L", 48: "M", 49: "N", 50: "O",
                    51: "P", 52: "Q", 53: "R", 54: "S", 55: "T", 56: "U", 57: "V", 58: "W", 59: "X", 60: "Y",
                    61: "Z", 62: "¬", 63: "`", 64: "!", 65: "\"", 66: "£", 67: "$", 68: "%", 69: "^", 70: "&",
                    71: "*", 72: "(", 73: ")", 74: "-", 75: " ", 76: "=", 77: "+", 78: "[", 79: "{", 80: "]",
                    81: "}", 82: ";", 83: ":", 84: "'", 85: "@", 86: "#", 87: "~", 88: "\\", 89: "|", 90: ",",
                    91: "<", 92: ".", 93: ">", 94: "/", 95: "?"}

conversion_table_back = {v: k for k, v in conversion_table.items()}


def to_hex(base_fr, base_to, hex_to_convert):
    decimal = 0
    power = len(hex_to_convert)-1
    for digit in hex_to_convert:
        decimal += conversion_table_back[digit]*base_fr**power
        power -= 1
    hexadecimal = ''
    while decimal > 0:
        remainder = decimal % base_to
        hexadecimal = conversion_table[remainder]+hexadecimal
        decimal = decimal // base_to
    return hexadecimal


def get_hex_base(hex_to_check):  # this is only a guess
    for i in range(96):
        if to_hex(i+2, i+2, hex_to_check) == hex_to_check:
            return i+2


def pass_to_seed(password, salt):
    salt = sha512(sha512(b85encode(salt.encode())).hexdigest().encode()).hexdigest()
    inp = f"{salt[:64]}{password}{salt[64:]}"
    return to_hex(16, 96, sha512(sha512(b85encode(inp.encode())).hexdigest().encode()).hexdigest())


def seed2_to_alpha(seeds):  # this function requires 192 numbers
    alpha_gen = ascii_set
    counter = 0
    alpha = ""
    while len(alpha_gen) > 1:
        counter += 2
        value = int(str(seeds)[counter:counter+2])*2
        while value > len(alpha_gen)-1:
            value = value // 2
        if len(str(seeds)[counter:])<2:
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
    alphabet2 = alphabet*2
    output_enc = ""
    counter = 0
    for msg in plaintext:
        counter += 2
        if msg in alphabet:
            key = int(shift_num[counter:counter+2])
            if key > 84:
                key = key-84
            if not forwards:
                key = key*(-1)
            output_enc += alphabet2[alphabet.index(msg)+key]
        else:
            output_enc += msg  # todo fix the ignoring of 0
    return output_enc


def encrypt(text, alpha1, shift_num):  # todo, make multiprocess
    text_type = type(text)
    if text_type == int:
        text = str(text)
    if text_type == bytes:
        plaintext = b85encode(compress(text, 9)).decode('utf-8')
    else:
        plaintext = b85encode(compress(text.encode('utf-8'), 9)).decode('utf-8')
    shift_num = str(int(to_hex(96, 10, str(shift_num)), 36))
    while len(str(shift_num)) < len(plaintext)*2:
        shift_num += f"{int(str(shift_num)[-2048:], 36)}"
    return shifter(plaintext, str(shift_num), alpha1, True)


def encrypt_key(text, key, salt):
    alpha1, shift_num = seed_to_data(pass_to_seed(key, salt))
    return encrypt(text, alpha1, shift_num)


def decrypt(e_text, alpha1, shift_num):  # todo, make multiprocess
    shift_num = str(int(to_hex(96, 10, str(shift_num)), 36))
    while len(str(shift_num)) < len(e_text)*2:
        shift_num += f"{int(str(shift_num)[-2048:], 36)}"
    output_end = shifter(e_text, str(shift_num), alpha1, False).replace(" ", "")
    try:
        output_end = decompress(b85decode(output_end)).decode('utf-8')
    except UnicodeDecodeError:
        output_end = decompress(b85decode(output_end))
    return output_end


def decrypt_key(e_text, key, salt):
    alpha1, shift_num = seed_to_data(pass_to_seed(key, salt))
    return decrypt(e_text, alpha1, shift_num)


def get_file_size(file):
    file_size_kb = path.getsize(file)/1024
    if file_size_kb > 9999:
        file_size_mb = file_size_kb/1024
        if file_size_mb > 750:
            print("This file is not supported due to its large size, the max is 750MB")
            return "NOTSUP"
            #file_size_gb = file_size_mb/1024
            #return f"{round(file_size_gb, 2)}GB"
        else:
            return f"{round(file_size_mb,2)}MB"
    else:
        return f"{round(file_size_kb,2)}KB"


def encrypt_block(data, block_num, alpha, shift_num, send_end):
    print(f"Block {block_num} launched")
    enc_block = shifter(b85encode(compress(data, 9)).decode('utf-8'), str(shift_num), alpha, True)
    print(f"Block {block_num} complete")
    send_end.send(enc_block)


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
        data_chunks_list = [data_chunks[i:i+block_size] for i in range(0, len(data_chunks), block_size)]
        print(f"Launching {len(data_chunks_list)} threads")
        with open(file_output, "w") as f:
            f.write("")
        alpha, shift_num = seed_to_data(seed)  # todo add per block alphas
        shift_num = str(int(to_hex(96, 10, str(shift_num)), 36))
        while len(str(shift_num)) < block_size*2.5:
            shift_num += f"{int(str(shift_num)[-4096:], 36)}"
        loop = 0
        threads = []
        pipe_list = []
        for chunk in data_chunks_list:
            loop += 1
            recv_end, send_end = Pipe(duplex=False)
            t = Process(target=encrypt_block, args=(chunk, loop, alpha, shift_num, send_end,))
            t.daemon = True
            t.start()
            threads.append(t)
            pipe_list.append(recv_end)
        result_list = [x.recv() for x in pipe_list]
        for thread in threads:
            thread.join()
        with open(file_output, "w", encoding="utf-8") as f:
            for e_block in result_list:
                f.write(f"¬{e_block}")
    except Exception as e:
        print("Error", e)
    # todo show new "compressed" size
    print(f"ENCRYPTION COMPLETE OF {get_file_size(file_to_enc)} ({block_size}*{len(data_chunks_list)})"
          f" IN {round(time()-start, 2)}s")


def decrypt_block(e_data, block_num, alpha, shift_num, send_end):
    print(f"Block {block_num} launched")
    output_end = shifter(e_data, str(shift_num), alpha, False).replace(" ", "")
    try:
        d_data = decompress(b85decode(output_end)).decode('utf-8')
    except UnicodeDecodeError:
        d_data = decompress(b85decode(output_end))
    print(f"Block {block_num} complete")
    send_end.send(d_data)


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
    print(f"Launching {len(e_text)-1} threads")
    alpha, shift_num = seed_to_data(seed)  # todo add per block alphas
    shift_num = str(int(to_hex(96, 10, str(shift_num)), 36))
    while len(str(shift_num)) < block_size*2:
        shift_num += f"{int(str(shift_num)[-4096:], 36)}"
    loop = 0
    threads = []
    pipe_list = []
    for chunk in e_text:
        if len(chunk) > 0:
            loop += 1
            recv_end, send_end = Pipe(duplex=False)
            t = Process(target=decrypt_block, args=(chunk, loop, alpha, shift_num, send_end,))
            t.daemon = True
            t.start()
            threads.append(t)
            pipe_list.append(recv_end)
    result_list = [x.recv() for x in pipe_list]
    for thread in threads:
        thread.join()

    if type(result_list[0]) == bytes:
        d_data = b""
        data_type = "byte"
    else:
        d_data = ""
        data_type = "string"
    for d_block in result_list:
        d_data += d_block
    if data_type == "byte":
        with open(f"{file_output}", "wb") as f:
            f.write(d_data)
    if data_type == "string":
        with open(f"{file_output}", "w", encoding="utf-8") as f:
            f.write(d_data.replace("\r", ""))
    # todo show new "compressed" size
    print(f"DECRYPTION COMPLETE OF {get_file_size(file_to_dec)} ({block_size}*{len(e_text)-1})"
          f" IN {round(time()-start, 2)}s")


def search(data, filter_fr, filter_to):
    data = str(data)
    m = re.search(f"""{filter_fr}(.+?){filter_to}""", data)
    if m:
        output = m.group(1)
    else:
        output = None
    return output


def get_links(data):
    a = (re.findall(r'(https?://[^\s]+)', str(data)))
    b = (re.findall(r'(http?://[^\s]+)', str(data)))
    c = ('\n'.join(a))
    d = ('\n'.join(b))
    e = c + d
    return e


def round_tme(dt=None, round_to=30):
    if not dt:
        dt = datetime.datetime.now()
    seconds = (dt.replace(tzinfo=None)-dt.min).seconds
    return dt + datetime.timedelta(0, (seconds+round_to/2)//round_to*round_to-seconds, -dt.microsecond)


def hash_a_file(file):
    read_size = 262144
    hash_ = sha512()
    with open(file, 'rb') as hash_file:
        buf = hash_file.read(read_size)
        while len(buf) > 0:
            hash_.update(buf)
            buf = hash_file.read(read_size)
    return to_hex(16, 96, hash_.hexdigest())
