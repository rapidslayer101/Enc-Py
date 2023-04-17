from sys import getsizeof
from random import randbytes
from time import perf_counter
from multiprocessing import freeze_support
import enc11_8
import enc11_5, enc11_4, enc11_3, enc11_1, enc9_8, enc9_7, enc9_6, enc9_5, enc9_4, enc9_3, enc9_0, enc8_6
import enc8_5, enc8_2, enc8, enc7, enc6, enc5, enc4, enc3, enc2
import enc10 as enc10_0
import enc11 as enc11_0
import enclib as enc11_x

if __name__ == '__main__':
    freeze_support()
    text = enc11_x.rand_b96_str(1000000)
    text = text*100
    #text = randbytes(1000000)
    print(f"{len(text)/1000000} Million chars")

    enc2_t = False
    enc3_t = False
    enc4_t = False
    enc5_t = False
    enc6_t = False
    enc7_t = False
    enc8_t = False
    enc8_2_t = False
    enc8_5_t = False
    enc8_6_t = False
    enc9_0_t = False
    enc9_3_t = False
    enc9_4_t = False
    enc9_5_t = False
    enc9_6_t = False
    enc9_7_t = False
    enc9_8_t = False
    enc10_0_t = False
    enc11_0_t = False
    enc11_1_t = False
    enc11_3_t = False
    enc11_4_t = False
    enc11_5_t = False
    enc11_8_t = True
    enc11_x_t = True

    if enc2_t:
        print("ENC2.0", enc2.encrypt(text))

    if enc3_t:
        print("ENC3.0", enc3.encrypt(text))

    if enc4_t:
        start = perf_counter()
        enc4_e = enc4.shorte(text)
        if enc4.shortd(enc4_e) == text:
            print("ENC4.0", round(perf_counter()-start, 4))
        else:
            print("ENC4.0 FAIL")

    if enc5_t:
        start = perf_counter()
        enc5_e = enc5.encrypt(text)
        if enc5.decrypt(enc5_e) == text:
            print("ENC5.5", round(perf_counter()-start, 4))
        else:
            print("ENC5.5 FAIL")

    if enc6_t:
        start = perf_counter()
        enc6_e = enc6.encrypt(text)
        if enc6.decrypt(enc6_e) == text:
            print("ENC6.4", round(perf_counter()-start, 4))
        else:
            print("ENC6.4 FAIL")

    if enc7_t:
        start = perf_counter()
        enc7_e = enc7.encrypt_key(text, "key", "salt")
        if enc7.decrypt_key(enc7_e, "key", "salt") == text:
            print("ENC7.0", round(perf_counter()-start, 4), len(enc7_e), getsizeof(enc7_e))
        else:
            print("ENC7.0 FAIL")

    if enc8_t:
        start = perf_counter()
        enc8_e = enc8.encrypt_key(text, "key", "salt")
        if enc8.decrypt_key(enc8_e, "key", "salt") == text:
            print("ENC8.0", round(perf_counter()-start, 4), len(enc8_e), getsizeof(enc8_e))
        else:
            print("ENC8.0 FAIL")

    if enc8_2_t:
        start = perf_counter()
        enc8_2_e = enc8_2.encrypt_key(text, "key", "salt")
        if enc8_2.decrypt_key(enc8_2_e, "key", "salt") == text:
            print("ENC8.2", round(perf_counter()-start, 4), len(enc8_2_e), getsizeof(enc8_2_e))
        else:
            print("ENC8.2 FAIL")

    if enc8_5_t:
        start = perf_counter()
        enc8_5_e = enc8_5.encrypt_key(text, "key", "salt")
        if enc8_5.decrypt_key(enc8_5_e, "key", "salt") == text:
            print("ENC8.5", round(perf_counter()-start, 4), len(enc8_5_e), getsizeof(enc8_5_e))
        else:
            print("ENC8.5 FAIL")

    if enc8_6_t:
        start = perf_counter()
        enc8_6_e = enc8_6.encrypt_key(text, "key", "salt")
        if enc8_6.decrypt_key(enc8_6_e, "key", "salt") == text:
            print("ENC8.6", round(perf_counter()-start, 4), len(enc8_6_e), getsizeof(enc8_6_e))
        else:
            print("ENC8.6 FAIL")

    if enc9_0_t:
        start = perf_counter()
        enc9_0_e = enc9_0.encrypt_key(text, "key", "salt")
        if enc9_0.decrypt_key(enc9_0_e, "key", "salt") == text:
            print("ENC9.0", round(perf_counter()-start, 4), len(enc9_0_e), getsizeof(enc9_0_e))
        else:
            print("ENC9.0 FAIL")

    if enc9_3_t:
        start = perf_counter()
        enc9_3_e = enc9_3.encrypt_key(text, "key", "salt")
        if enc9_3.decrypt_key(enc9_3_e, "key", "salt") == text:
            print("ENC9.3", round(perf_counter()-start, 4), len(enc9_3_e), getsizeof(enc9_3_e))
        else:
            print("ENC9.3 FAIL")

    if enc9_4_t:
        start = perf_counter()
        enc9_4_e = enc9_4.encrypt_key(text, "key", "salt")
        if enc9_4.decrypt_key(enc9_4_e, "key", "salt") == text:
            print("ENC9.4", round(perf_counter()-start, 4), len(enc9_4_e), getsizeof(enc9_4_e))
        else:
            print("ENC9.4 FAIL")

    if enc9_5_t:
        start = perf_counter()
        enc9_5_e = enc9_5.encrypt_key(text, "key", "salt")
        if enc9_5.decrypt_key(enc9_5_e, "key", "salt") == text:
            print("ENC9.5", round(perf_counter()-start, 4), len(enc9_5_e), getsizeof(enc9_5_e))
        else:
            print("ENC9.5 FAIL")

    if enc9_6_t:
        start = perf_counter()
        enc9_6_e = enc9_6.encrypt_key(text, "key", "salt")
        if enc9_6.decrypt_key(enc9_6_e, "key", "salt") == text:
            print("ENC9.6", round(perf_counter()-start, 4), len(enc9_6_e), getsizeof(enc9_6_e))
        else:
            print("ENC9.6 FAIL")

    if enc9_7_t:
        start = perf_counter()
        enc9_7_e = enc9_7.encrypt_key(text, "key", "salt")
        if enc9_7.decrypt_key(enc9_7_e, "key", "salt") == text:
            print("ENC9.7", round(perf_counter()-start, 4), len(enc9_7_e), getsizeof(enc9_7_e))
        else:
            print("ENC9.7 FAIL")

    if enc9_8_t:
        start = perf_counter()
        enc9_8_e = enc9_8.encrypt_key(text, "key", "salt")
        if enc9_8.decrypt_key(enc9_8_e, "key", "salt") == text:
            print("ENC9.8", round(perf_counter()-start, 4), len(enc9_8_e), getsizeof(enc9_8_e))
        else:
            print("ENC9.8 FAIL")

    if enc10_0_t:
        start = perf_counter()
        enc10_0_e = enc10_0.encrypt_key(text, "key", "salt")
        if enc10_0.decrypt_key(enc10_0_e, "key", "salt") == text:
            print("ENC10.0", round(perf_counter()-start, 4), len(enc10_0_e), getsizeof(enc10_0_e))
        else:
            print("ENC10.0 FAIL")

    if enc11_0_t:
        start = perf_counter()
        enc11_0_e = enc11_0.encrypt_key(text, "key", "salt")
        if enc11_0.decrypt_key(enc11_0_e, "key", "salt") == text:
            print("ENC11.0", round(perf_counter()-start, 4), len(enc11_0_e), getsizeof(enc11_0_e))
        else:
            print("ENC11.0 FAIL")

    if enc11_1_t:
        start = perf_counter()
        enc11_1_e = enc11_1.enc_from_pass(text, "key", "salt")
        if enc11_1.dec_from_pass(enc11_1_e, "key", "salt") == text:
            print("ENC11.1", round(perf_counter()-start, 4), len(enc11_1_e), getsizeof(enc11_1_e))
        else:
            print("ENC11.1 FAIL")

    if enc11_3_t:
        start = perf_counter()
        enc11_3_e = enc11_3.enc_from_pass(text, "key", "salt")
        if enc11_3.dec_from_pass(enc11_3_e, "key", "salt") == text:
            print("ENC11.3", round(perf_counter()-start, 4), len(enc11_3_e), getsizeof(enc11_3_e))
        else:
            print("ENC11.3 FAIL")

    if enc11_4_t:
        start = perf_counter()
        enc11_4_e = enc11_4.enc_from_pass(text, "key", "salt")
        if enc11_4.dec_from_pass(enc11_4_e, "key", "salt") == text:
            print("ENC11.4", round(perf_counter()-start, 4), len(enc11_4_e), getsizeof(enc11_4_e))
        else:
            print("ENC11.4 FAIL")

    if enc11_5_t:
        start = perf_counter()
        enc11_5_e = enc11_5.enc_from_pass(text, "key", "salt")
        if enc11_5.dec_from_pass(enc11_5_e, "key", "salt") == text:
            print("ENC11.5", round(perf_counter()-start, 4), len(enc11_5_e), getsizeof(enc11_5_e))
        else:
            print("ENC11.5 FAIL")

    if enc11_8_t:
        start = perf_counter()
        key = enc11_8.pass_to_key("key", "salt", 100000)
        print("P2K.TME", round(perf_counter()-start, 4))
        start = perf_counter()
        enc11_8_e = enc11_8.enc_from_key(text, key)
        if enc11_8.dec_from_key(enc11_8_e, key) == text:
            print("ENC11.8", round(perf_counter()-start, 4), len(enc11_8_e), getsizeof(enc11_8_e))
        else:
            print("ENC11.8 FAIL")

    if enc11_x_t:
        start = perf_counter()
        key = enc11_x.pass_to_key("key", "salt", 100000)
        print("P2K.TME", round(perf_counter()-start, 4))
        start = perf_counter()
        enc11_x_e = enc11_x.enc_from_key(text, key)
        if enc11_x.dec_from_key(enc11_x_e, key) == text:
            print("ENC11.x", round(perf_counter()-start, 4), len(enc11_x_e), getsizeof(enc11_x_e))
        else:
            print("ENC11.x FAIL")

    graph = False

    if graph:
        import matplotlib.pyplot as plt
        plt.ion()

        x = []
        enc11x_1 = []
        enc11x_2 = []
        enc11x_3 = []
        text_len = 1000000
        key = enc11_x.pass_to_key("key", "salt", 100000)
        while True:
            text_len += 1000000
            text = enc11_x.rand_b96_str(text_len)

            start = perf_counter()
            enc11_x.enc_from_key(text, key)
            enc11x_1.append(float(str(perf_counter() - start)[:-14]))

            start = perf_counter()
            enc11_x.enc_from_key(text, key, 10000000)
            enc11x_2.append(float(str(perf_counter() - start)[:-14]))

            start = perf_counter()
            enc11_x.enc_from_key(text, key, 100000000)
            enc11x_3.append(float(str(perf_counter()-start)[:-14]))

            print(text_len)
            x.append(text_len/1000000)
            plt.plot(x, enc11x_1, label="enc11.x_1", color="red")
            plt.plot(x, enc11x_2, label="enc11.x_2", color="orange")
            plt.plot(x, enc11x_3, label="enc11.x_3", color="green")
            plt.show()
            plt.pause(0.05)

    input("Inp")
    while True:
        enc11_x.enc_file_from_pass("jdk-17.0.4.1_windows-x64_bin.exe", "key", "salt", "enc.renc")
        input("K")
        enc11_x.dec_file_from_pass("enc.renc", "key", "salt", "jdk-17.0.4.1_windows-x64_bin.exe")
        input("Loop.")

