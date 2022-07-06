from datetime import datetime, timedelta
from sys import byteorder
from re import search, findall
from time import time
from os import path
from random import choices
from hashlib import sha512
from zlib import compress, decompress
from multiprocessing import Pool, cpu_count

# enc 11.4.0 - CREATED BY RAPIDSLAYER101 (Scott Bree)
# todo not same result with same key every time
# todo new secure seeding
block_size = 1000000  # modifies the chunking size
b96set = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/¬`!\"£$%^&*()- =[{]};:'@#~\\|,<.>?"


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


def pass_to_key(password, salt):  # todo redo
    salt = sha512(sha512(salt.encode()).hexdigest().encode()).hexdigest()
    return to_hex(16, 96, sha512(sha512((salt+password).encode()).hexdigest().encode()).hexdigest())


def key_to_data(key):
    key = int(to_hex(96, 16, key), 36)
    alpha_gen = b96set
    counter, alpha = [0, ""]
    while len(alpha_gen) > 0:
        counter += 2
        value = int(str(key)[counter:counter+2]) << 1
        while value > len(alpha_gen) - 1:
            value = value // 2
        if len(str(key)[counter:]) < 2:
            alpha += alpha_gen
            alpha_gen = alpha_gen.replace(alpha_gen, "")
        else:
            chosen = alpha_gen[value]
            alpha += chosen
            alpha_gen = alpha_gen.replace(chosen, "")
    return alpha.encode(), to_hex(10, 96, str(key))


def _xor_(data, seed, alpha, byte_ord=byteorder):
    shift_value = []
    shift_num = str(to_hex(96, 10, str(seed)))
    for i in range((len(data)//64)+1):
        shift_num = sha512(shift_num.encode()+alpha).hexdigest()
        shift_value.append(shift_num)
    key = bytearray.fromhex("".join(shift_value))[:len(data)]
    key, var = key[:len(data)], data[:len(key)]
    int_enc = (int.from_bytes(var, byte_ord) ^ int.from_bytes(key, byte_ord))
    return int_enc.to_bytes(len(var), byte_ord)


def _encrypter_(enc, text, alpha, seed, salt, compressor, join_dec=None):
    if enc:
        if type(text) != bytes:
            text = text.encode()
        if compressor:
            text = compress(text, 9)
    text = [text[i:i+block_size] for i in range(0, len(text), block_size)]
    if len(text) == 1:
        text = text[0]
        if enc:
            return _xor_(text, str(to_hex(96, 10, str(seed))), alpha)
        else:
            if compressor:
                block = decompress(_xor_(text, str(to_hex(96, 10, str(seed))), alpha))
            else:
                block = _xor_(text, str(to_hex(96, 10, str(seed))), alpha)
            try:
                return block.decode()
            except UnicodeDecodeError:
                return block
    else:
        print(f"Launching {len(text)} threads")
        block_seeds = []
        for i in range(len(text)+1):
            seed = pass_to_key(seed, salt)
            block_seeds.append(seed)
        pool = Pool(cpu_count())
        result_objects = [pool.apply_async(_xor_, args=(text[x], block_seeds[x], alpha))
                          for x in range(0, len(text))]
        pool.close()
        if join_dec:
            d_data = b""
            for x in result_objects:
                d_data += x.get()
            if not enc:
                if compressor:
                    d_data = decompress(d_data)
                try:
                    d_data = d_data.decode()
                except UnicodeDecodeError:
                    pass
        else:
            d_data = [x.get() for x in result_objects]
        pool.join()
        return d_data


def get_file_size(file):
    size, power, n = [path.getsize(file), 2 ** 10, 0]
    power_labels = {0: '', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
    while size > power:
        size /= power
        n += 1
    return f"{round(size, 2)}{power_labels[n]}"


def _file_encrypter_(enc, file, password, salt, file_output):
    start = time()
    if path.exists(file):
        file_name = file.split("/")[-1].split(".")[:-1]  # file_type = file.split("/")[-1].split(".")[-1:]
        print(f"{file_name} is {get_file_size(file)}, should take {round(path.getsize(file)/136731168.599, 2)}s")
        alpha, shift_num = key_to_data(pass_to_key(password, salt))
        if enc:
            with open(file, 'rb') as hash_file:
                e_blocks = _encrypter_(enc, hash_file.read(), alpha, shift_num, salt, False)
            with open(file_output, "wb") as f:
                for block in e_blocks:
                    f.write(block)
            print(f"ENCRYPTION COMPLETE OF {get_file_size(file)} IN {round(time()-start, 2)}s")
        else:
            with open(file, "rb") as hash_file:
                d_data = _encrypter_(enc, hash_file.read(), alpha, shift_num, salt, False)
            if type(d_data[0]) == bytes:
                with open(f"{file_output}", "wb") as f:
                    for block in d_data:
                        f.write(block)
            if type(d_data[0]) == str:
                with open(f"{file_output}", "w", encoding="utf-8") as f:
                    for block in d_data:
                        f.write(block.replace("\r", ""))
            with open(f"{file_output}", "rb") as f:
                data = decompress(f.read())
            with open(f"{file_output}", "wb") as f:
                f.write(data)
            print(f"DECRYPTION COMPLETE OF {get_file_size(file)} IN {round(time()-start, 2)}s")
    else:
        return "File not found"


def enc_from_pass(text, password, salt):
    alpha, shift_num = key_to_data(pass_to_key(password, salt))
    return _encrypter_(True, text, alpha, shift_num, salt, True, True)


def enc_from_key(text, key, salt):
    alpha, shift_num = key_to_data(key)
    return _encrypter_(True, text, alpha, shift_num, salt, True, True)


def dec_from_pass(e_text, password, salt):
    alpha, shift_num = key_to_data(pass_to_key(password, salt))
    return _encrypter_(False, e_text, alpha, shift_num, salt, True, True)


def dec_from_key(e_text, key, salt):
    alpha, shift_num = key_to_data(key)
    return _encrypter_(False, e_text, alpha, shift_num, salt, True, True)


def enc_file_from_pass(file, password, salt, file_output):
    return _file_encrypter_(True, file, password, salt, file_output)


def dec_file_from_pass(e_file, password, salt, file_output):
    return _file_encrypter_(False, e_file, password, salt, file_output)


def rand_b96_str(num):
    return "".join(choices(b96set, k=int(num)))


def search(data, filter_fr, filter_to):
    m = search(f"""{filter_fr}(.+?){filter_to}""", str(data))
    if m:
        return m.group(1)
    else:
        return None


def get_links(data):
    return ('\n'.join((findall(r'(https?://[^\s]+)', str(data))))) + \
           ('\n'.join((findall(r'(http?://[^\s]+)', str(data)))))


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
