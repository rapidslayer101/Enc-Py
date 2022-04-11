import datetime
from re import search, findall
from time import time
from os import path
from random import choices
from base64 import b64encode as b64enc
from hashlib import sha512
from zlib import compress, decompress
from multiprocessing import Pool, cpu_count

# enc 11.1.0 - CREATED BY RAPIDSLAYER101 (Scott Bree)
# todo not same result with same key every time
# todo new secure seeding
block_size = 1000000  # modifies the chunking size
b96set = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/¬`!\"£$%^&*()- =[{]};:'@#~\\|,<.>?"


def to_hex(base_fr, base_to, hex_to_convert):
    decimal = 0
    power = len(hex_to_convert)-1
    for digit in hex_to_convert:
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


def pass_to_seed(password, salt):  # todo redo
    salt = sha512(sha512(salt.encode()).hexdigest().encode()).hexdigest()
    return to_hex(16, 96, sha512(sha512((salt+password).encode()).hexdigest().encode()).hexdigest())


def seed_to_data(seed):
    seed = int(to_hex(96, 16, seed), 36)
    alpha_gen = b96set
    counter, alpha = [0, ""]
    while len(alpha_gen) > 0:
        counter += 2
        value = int(str(seed)[counter:counter+2]) << 1
        while value > len(alpha_gen) - 1:
            value = value // 2
        if len(str(seed)[counter:]) < 2:
            alpha += alpha_gen
            alpha_gen = alpha_gen.replace(alpha_gen, "")
        else:
            chosen = alpha_gen[value]
            alpha += chosen
            alpha_gen = alpha_gen.replace(chosen, "")
    return alpha, to_hex(10, 96, str(seed))


def _otp_(amount, shift_num, alpha):  # todo redesign?
    shift_value = ""
    while len(shift_value) < amount:
        shift_num1 = sha512((shift_num+alpha).encode()).digest()
        shift_num = b64enc(shift_num1).decode()[:-2]
        shift_value += shift_num+b64enc(shift_num1[::-1]).decode()[:-2]
    return shift_value


def _xor_(plaintext, shift_num, enc):
    if enc:
        return bytes([(x ^ ord(y)) for x, y in zip(compress(plaintext, 9), shift_num)])
    else:
        return bytes([x ^ ord(y) for x, y in zip(plaintext, shift_num)])


def _encrypt_block_(enc, data, block_seed, alpha, send_end=None):
    if enc:
        if type(data) != bytes:
            data = data.encode()
        block = _xor_(data, _otp_(len(data), str((to_hex(96, 10, str(block_seed)))), alpha), True)
    else:
        block = decompress(_xor_(data, _otp_(len(data), str((to_hex(96, 10, str(block_seed)))), alpha), False))
        try:
            block = block.decode()
        except UnicodeDecodeError:
            pass
    if send_end:
        send_end.send(block)
    else:
        return block


def _encrypter_(enc, text, alpha, shift_seed, salt, join_dec=None):
    if enc:
        text = [text[i:i+block_size] for i in range(0, len(text), block_size)]
    else:
        if not type(text) == list:
            if type(text) == bytes:
                text = text.split(b"  ")
            else:  # if type(text) == str:
                text = text.split("  ")
    if len(text) == 1:
        text = text[0]
        shift_seed = to_hex(96, 10, str(shift_seed))
        if enc:
            if type(text) != bytes:
                text = text.encode()
            return _xor_(text, _otp_(len(text), str(shift_seed), alpha), True)
        else:
            output_end = decompress(_xor_(text, _otp_(len(text), str(shift_seed), alpha), False))
            try:
                return output_end.decode()
            except UnicodeDecodeError:
                return output_end
    else:
        print(f"Launching {len(text)} threads")
        block_seeds = []
        for i in range(len(text)+1):
            shift_seed = pass_to_seed(shift_seed, salt)
            block_seeds.append(shift_seed)
        pool = Pool(cpu_count())
        result_objects = [pool.apply_async(_encrypt_block_, args=(enc, text[x], block_seeds[x], alpha))
                          for x in range(0, len(text))]
        pool.close()
        if join_dec:
            d_data = b""
            for x in result_objects:
                new_data = x.get()
                try:
                    d_data += new_data
                except TypeError:
                    d_data = ""
                    d_data += new_data
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
        print(f"{file_name} is {get_file_size(file)}, should take {round(path.getsize(file)/58552080.2181, 2)}s")
        alpha, shift_num = seed_to_data(pass_to_seed(password, salt))
        if enc:
            with open(file, 'rb') as hash_file:
                result_list = _encrypter_(enc, hash_file.read(), alpha, shift_num, salt)
            with open(file_output, "wb") as f:
                for e_block in result_list:
                    f.write(b"  ")
                    f.write(e_block)
            print(f"ENCRYPTION COMPLETE OF {get_file_size(file)} IN {round(time()-start, 2)}s")
        else:
            with open(file, "rb") as hash_file:
                d_data = _encrypter_(enc, hash_file.read().split(b"  ")[1:], alpha, shift_num, salt)
            if type(d_data[0]) == bytes:
                with open(f"{file_output}", "wb") as f:
                    for block in d_data:
                        f.write(block)
            if type(d_data[0]) == str:
                with open(f"{file_output}", "w", encoding="utf-8") as f:
                    for block in d_data:
                        f.write(block.replace("\r", ""))
            print(f"DECRYPTION COMPLETE OF {get_file_size(file)} IN {round(time()-start, 2)}s")
    else:
        return "File not found"


def enc_from_pass(text, password, salt):
    alpha, shift_num = seed_to_data(pass_to_seed(password, salt))
    return _encrypter_(True, text, alpha, shift_num, salt)


def dec_from_pass(e_text, password, salt):
    alpha, shift_num = seed_to_data(pass_to_seed(password, salt))
    return _encrypter_(False, e_text, alpha, shift_num, salt, "join_dec")


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
        dt = datetime.datetime.now()
    seconds = (dt.replace(tzinfo=None)-dt.min).seconds
    return dt+datetime.timedelta(0, (seconds+round_to/2)//round_to*round_to-seconds, -dt.microsecond)


def hash_a_file(file):
    hash_ = sha512()
    with open(file, 'rb') as hash_file:
        buf = hash_file.read(262144)
        while len(buf) > 0:
            hash_.update(buf)
            buf = hash_file.read(262144)
    return to_hex(16, 96, hash_.hexdigest())
