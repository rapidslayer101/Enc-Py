import enclib as enc9
import time
from multiprocessing import freeze_support

if __name__ == '__main__':
    freeze_support()
    text = enc9.hex_gens(100000)
    print(f"TEXT {len(text)}")

    start = time.time()
    enc9_e = enc9.encrypt_key(text, "random_key", "salt")
    if enc9.decrypt_key(enc9_e, "random_key", "salt") == text:
        print("ENC8.x", time.time() - start)  # , enc9_e)
    else:
        print("ENC8.x FAIL")

    seed = enc9.pass_to_seed(input("Input Seed: "), input("Input Salt: "))
    while True:
        print("Encrypt file.")
        enc9.encrypt_file(input("Input file: "), seed, input("Output file: "))
        print("Decrypt file.")
        enc9.decrypt_file(input("Input file: "), seed, input("Output file: "))