from datetime import datetime, timedelta
from sys import byteorder
from re import search
from time import time
from os import path
from random import choices
from hashlib import sha512
from zlib import compress, decompress
from multiprocessing import Pool, cpu_count

# enc 11.7.0 - CREATED BY RAPIDSLAYER101 (Scott Bree)
default_block_size = 5000000  # modifies the chunking size
xor_salt_len = 8  # 94^8 combinations
default_pass_depth = 100000
b96set = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/¬`!\"£$%^&*()- =[{]};:'@#~\\|,<.>?"
b94set = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/`!\"$%^&*() -=[{]};:'@#~\\|,<.>?"


def rand_b96_str(num):
    return "".join(choices(b96set, k=int(num)))


def to_hex(base_fr, base_to, hex_to_convert):
    decimal = 0
    power = len(str(hex_to_convert))-1
    for digit in str(hex_to_convert):
        decimal += b96set.index(digit)*base_fr**power
        power -= 1
    hexadecimal = ""
    while decimal > 0:
        hexadecimal = b96set[decimal % base_to]+hexadecimal
        decimal = decimal // base_to
    return hexadecimal


def get_hex_base(hex_to_check):  # this is only a guess
    for i in range(96):
        if to_hex(i+2, i+2, hex_to_check) == hex_to_check:
            return i+2


def pass_to_key(password, salt, depth):
    password = password.encode()
    salt = salt.encode()
    for i in range(depth):
        password = sha512(password+salt).digest()
    return to_hex(16, 96, password.hex())


def _xor_(data, key, xor_salt):
    key_value = []
    key = key.encode()
    for i in range((len(data)//64)+1):
        key = sha512(key+xor_salt).digest()
        key_value.append(key)
    key = b"".join(key_value)[:len(data)]
    return (int.from_bytes(data, byteorder) ^ int.from_bytes(key, byteorder)).to_bytes(len(data), byteorder)


def _encrypter_(enc, text, key, block_size, compressor, file_output=None):
    if enc:
        if type(text) != bytes:
            text = text.encode()
        if compressor:
            text = compress(text, 9)
        xor_salt = "".join(choices(b94set, k=xor_salt_len)).encode()
    else:
        xor_salt, text = text[:xor_salt_len], text[xor_salt_len:]
    if len(text)//block_size < 11:
        if enc:
            return xor_salt+_xor_(text, key, xor_salt)
        else:
            if compressor:
                block = decompress(_xor_(text, key, xor_salt))
            else:
                block = _xor_(text, key, xor_salt)
            try:
                return block.decode()
            except UnicodeDecodeError:
                return block
    else:
        text = [text[i:i+block_size] for i in range(0, len(text), block_size)]
        print(f"Generating {len(text)} block keys")
        key1 = int(to_hex(96, 16, key), 36)
        alpha_gen = b96set
        counter, keys_salt = [0, ""]
        while len(alpha_gen) > 0:
            counter += 2
            value = int(str(key1)[counter:counter+2]) << 1
            while value > len(alpha_gen) - 1:
                value = value // 2
            if len(str(key1)[counter:]) < 2:
                keys_salt += alpha_gen
                alpha_gen = alpha_gen.replace(alpha_gen, "")
            else:
                chosen = alpha_gen[value]
                keys_salt += chosen
                alpha_gen = alpha_gen.replace(chosen, "")
        block_keys = []
        for i in range(len(text)):
            key = pass_to_key(key, keys_salt, 1)
            block_keys.append(key)
        print(f"Launching {len(text)} threads")
        pool = Pool(cpu_count())
        result_objects = [pool.apply_async(_xor_, args=(text[x], block_keys[x], xor_salt))
                          for x in range(0, len(text))]
        pool.close()
        if file_output:
            if enc:
                with open(file_output, "wb") as f:
                    loop = 0
                    for x in result_objects:
                        loop += 1
                        if loop == 1:
                            data = xor_salt+x.get()
                            f.write(data)
                        else:
                            f.write(x.get())
            else:
                d_data = [x.get() for x in result_objects]
                if type(d_data[0]) == bytes:
                    with open(f"{file_output}", "wb") as f:
                        for block in d_data:
                            f.write(block)
                if type(d_data[0]) == str:
                    with open(f"{file_output}", "w", encoding="utf-8") as f:
                        for block in d_data:
                            f.write(block.replace("\r", ""))
                if compressor:
                    with open(f"{file_output}", "rb") as f:
                        data = decompress(f.read())
                    with open(f"{file_output}", "wb") as f:
                        f.write(data)
            pool.join()
        else:
            d_data = b""
            for x in result_objects:
                d_data += x.get()
            if enc:
                d_data = xor_salt + d_data
            else:
                if compressor:
                    d_data = decompress(d_data)
                try:
                    d_data = d_data.decode()
                except UnicodeDecodeError:
                    pass
            pool.join()
            return d_data


def get_file_size(file):
    size, power, n = [path.getsize(file), 2 ** 10, 0]
    power_labels = {0: '', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
    while size > power:
        size /= power
        n += 1
    return f"{round(size, 2)}{power_labels[n]}"


def _file_encrypter_(enc, file, key, file_output, compressor):
    start = time()
    if path.exists(file):
        file_name = file.split("/")[-1].split(".")[:-1]  # file_type = file.split("/")[-1].split(".")[-1:]
        print(f"{file_name} is {get_file_size(file)}, should take {round(path.getsize(file)/136731168.599, 2)}s")
        with open(file, 'rb') as hash_file:
            data = hash_file.read()
        _encrypter_(enc, data, key, default_block_size, compressor, file_output)
        print(f"ENC/DEC COMPLETE OF {get_file_size(file)} IN {round(time()-start, 2)}s")
    else:
        return "File not found"


def enc_from_pass(text, password, salt, depth=default_pass_depth, block_size=default_block_size):
    return _encrypter_(True, text, pass_to_key(password, salt, depth), block_size, True)


def enc_from_key(text, key, block_size=default_block_size):
    return _encrypter_(True, text, key, block_size, True)


def dec_from_pass(e_text, password, salt, depth=default_pass_depth, block_size=default_block_size):
    return _encrypter_(False, e_text, pass_to_key(password, salt, depth), block_size, True)


def dec_from_key(e_text, key, block_size=default_block_size):
    return _encrypter_(False, e_text, key, block_size, True)


def enc_file_from_pass(file, password, salt, file_output, depth=default_pass_depth, compressor=False):
    return _file_encrypter_(True, file, pass_to_key(password, salt, depth), file_output, compressor)


def dec_file_from_pass(e_file, password, salt, file_output, depth=default_pass_depth, compressor=False):
    return _file_encrypter_(False, e_file, pass_to_key(password, salt, depth), file_output, compressor)


def search(data, filter_fr, filter_to):
    m = search(f"""{filter_fr}(.+?){filter_to}""", str(data))
    if m:
        return m.group(1)
    else:
        return None


def round_tme(dt=None, round_to=30):
    if not dt:
        dt = datetime.now()
    seconds = (dt.replace(tzinfo=None)-dt.min).seconds
    return dt+timedelta(0, (seconds+round_to/2)//round_to*round_to-seconds, -dt.microsecond)


def hash_a_file(file):
    hash_ = sha512()
    with open(file, 'rb') as hash_file:
        buf = hash_file.read(262144)
        while len(buf) > 0:
            hash_.update(buf)
            buf = hash_file.read(262144)
    return to_hex(16, 96, hash_.hexdigest())
