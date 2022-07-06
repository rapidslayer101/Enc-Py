import random, os, time, datetime, re
from base64 import b85encode, b85decode
from hashlib import sha512
from zlib import compress, decompress
from threading import Thread

# enc 8.2.1 - CREATED BY RAPIDSLAYER101 (Scott Bree)
ascii_set = """0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~""" # base85
block_size = 1000000


def hex_gens(num):  # todo upgrade to generate random hex_base nums?
    hex_gens_ = ""
    while len(hex_gens_) != int(num):
        hex_gens_ += random.choice(ascii_set)
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


def shifter(plaintext, new_num_, alphabet, forwards):
    output_enc = ""
    counter = 0
    for msg in plaintext:
        counter += 2
        if msg in alphabet:
            key = int(new_num_[counter:counter+2])
            if key > 96:
                key = int(str(new_num_)[:2])
            if not forwards:
                key = key*(-1)
            if key == 0:
                new_alphabet = alphabet
            else:
                new_alphabet = alphabet[key:]+alphabet[:key]
            encrypted = ""
            alphabet_index = 0
            while True:
                if msg == alphabet[alphabet_index]:
                    encrypted += new_alphabet[alphabet_index]
                    break
                alphabet_index += 1
            output_enc += encrypted
        else:
            output_enc += msg
    return output_enc


def encrypt(text, alpha1, shift_num):
    text_type = type(text)
    if text_type == int:
        text = str(text)
    if text_type == bytes:
        plaintext = b85encode(compress(text, 9)).decode('utf-8')
    else:
        plaintext = b85encode(compress(text.encode('utf-8'), 9)).decode('utf-8')
    shift_num = int(to_hex(96, 10, str(shift_num)),36)
    while len(str(shift_num)) < len(plaintext)*3+100:
        shift_num = str(int(str(shift_num)[:512])//2)+str(shift_num)+str(int(str(shift_num)[:512])*2)
    return shifter(plaintext, str(shift_num), alpha1, True)


def encrypt_key(text, key, salt):
    alpha1, shift_num = seed_to_data(pass_to_seed(key, salt))
    return encrypt(text, alpha1, shift_num)


def decrypt(e_text, alpha1, shift_num):
    shift_num = int(to_hex(96, 10, str(shift_num)),36)
    while len(str(shift_num)) < len(e_text)*3+100:
        shift_num = str(int(str(shift_num)[:512])//2)+str(shift_num)+str(int(str(shift_num)[:512])*2)
    output_end = shifter(e_text, str(shift_num), alpha1, False).replace(" ", "")
    try:
        output_end = decompress(b85decode(output_end)).decode('utf-8')
    except:
        output_end = decompress(b85decode(output_end))
    return output_end


def decrypt_key(e_text, key, salt):
    alpha1, shift_num = seed_to_data(pass_to_seed(key, salt))
    return decrypt(e_text, alpha1, shift_num)


def get_file_size(file):
    file_size_kb = os.path.getsize(file)/1024
    if file_size_kb > 9999:
        file_size_mb = file_size_kb/1024
        if file_size_mb > 80:
            print("This file is not supported due to its large size, the max is 80MB")
            return "NOTSUP"
        else:
            return f"{round(file_size_mb,2)}MB"
    else:
        return f"{round(file_size_kb,2)}KB"


def encrypt_block(data, block_num, alpha, shift_num, output_file):
    try:
        print(f"Block {block_num} launched")
        enc_block = shifter(b85encode(compress(data, 9)).decode('utf-8'), str(shift_num), alpha, True)
        with open(output_file, "a+", encoding="utf-8") as f:
            f.write(f"•{block_num}§{enc_block}")
            print(f"Written block {block_num}")
    except Exception as e:
        print(e)


def encrypt_file(file_to_enc, seed, file_output=None):
    start = time.time()
    if os.path.exists(file_to_enc):
        file_name = file_to_enc.split("/")[-1]
        if get_file_size(file_to_enc) == "NOTSUP":
            return "File to large"
        else:
            print(f"{file_name} is {get_file_size(file_to_enc)}")
    else:
        return "File not found"  # todo smart find alternative

    read_size = 262144
    data_chunks = f"".encode("utf-8")
    try:
        with open(file_to_enc, 'rb') as hash_file:
            buf = hash_file.read(read_size)
            read = 0
            while len(buf) > 0:
                read += len(buf)
                data_chunks += buf
                buf = hash_file.read(read_size)

        data_chunks_list = [data_chunks[i:i+block_size] for i in range(0, len(data_chunks), block_size)]
        print(f"Launching {len(data_chunks_list)} threads")
        loop = 0
        threads = []
        with open(file_output, "w") as f:
            f.write("")
        alpha, shift_num = seed_to_data(seed)  # todo add per block alphas
        shift_num = str(int(to_hex(96, 10, str(shift_num)), 36))
        while len(str(shift_num)) < block_size*3+100:
            shift_num += f"{int(str(shift_num)[-16384:], 36)}"
        for chunk in data_chunks_list:
            loop += 1
            t = Thread(target=encrypt_block, args=(chunk, loop, alpha, shift_num, file_output,))
            t.daemon = True
            t.start()
            threads.append(t)
        for thread in threads:
            thread.join()
    except Exception as e:
        print("Error", e)
    # todo show new "compressed" size
    print(f"ENCRYPTION COMPLETE OF {get_file_size(file_to_enc)} ({block_size}*{len(data_chunks_list)})"
          f" IN {round(time.time()-start, 2)}s")


block_store = {}


class blocks:
    def add_block(self, block_num, data):
        block_store.update({block_num: data})


def decrypt_block(e_data, block_num, alpha, shift_num):
    try:
        print(f"Block {block_num} launched")
        output_end = shifter(e_data, str(shift_num), alpha, False).replace(" ", "")
        try:
            d_data = decompress(b85decode(output_end)).decode('utf-8')
        except:
            d_data = decompress(b85decode(output_end))
        blocks.add_block(0, block_num, d_data)
        print(f"Block {block_num} written to block store class")
    except Exception as e:
        print(e)


def decrypt_file(file_to_dec, seed, file_output=None):  # todo rewrite decrypter
    start = time.time()
    if os.path.exists(file_to_dec):
        file_name, file_type = file_to_dec.split("/")[-1].split(".")
        if file_type != "renc":
            return "This is not a renc file"
        else:
            print(f"{file_name} is {get_file_size(file_to_dec)}")
    else:
        return "File not found"  # todo smart find alternative

    threads = []
    with open(file_to_dec, encoding="utf-8") as dec_file:
        e_text = dec_file.read().split("•")
    print(f"Launching {len(e_text)-1} threads")
    alpha, shift_num = seed_to_data(seed)  # todo add per block alphas
    shift_num = str(int(to_hex(96, 10, str(shift_num)), 36))
    while len(str(shift_num)) < block_size*3+100:
        shift_num += f"{int(str(shift_num)[-16384:], 36)}"
    for chunk in e_text:
        try:
            block_num, data = chunk.split("§")
            t = Thread(target=decrypt_block, args=(data, block_num, alpha, shift_num,))
            t.daemon = True
            t.start()
            threads.append(t)
        except ValueError:
            xx = 0
    for thread in threads:
        thread.join()

    if type(block_store["1"]) == bytes:
        d_data = b""
        data_type = "byte"
    else:
        d_data = ""
        data_type = "string"
    for i in range(len(e_text)-1):
        data = block_store[str(i+1)]
        d_data += data

    if data_type == "byte":
        with open(f"{file_output}", "wb") as f:
            f.write(d_data)
    if data_type == "string":
        with open(f"{file_output}", "w", encoding="utf-8") as f:
            f.write(d_data.replace("\r", ""))
    # todo show new "compressed" size
    print(f"DECRYPTION COMPLETE OF {get_file_size(file_to_dec)} ({block_size}*{len(e_text)-1})"
          f" IN {round(time.time()-start, 2)}s")


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