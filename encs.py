import sys, time
import random
from multiprocessing import freeze_support
import enc11_1, enc9_8, enc9_7, enc9_6, enc9_5, enc9_4, enc9_3, enc9_0, enc8_6
import enc8_5, enc8_2, enc8, enc7, enc6, enc5, enc4, enc3, enc2
import enc10 as enc10_0
import enc11 as enc11_0
import enclib as enc11_x

if __name__ == '__main__':
    freeze_support()
    text = enc11_x.rand_b96_str(1000000)
    #text = text*20
    #text = random.randbytes(1000000)
    print(f"TEXT {len(text)}")

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
    enc11_1_t = True
    enc11_x_t = True

    if enc2_t:
        print("ENC2.0", enc2.encrypt(text))

    if enc3_t:
        print("ENC3.0", enc3.encrypt(text))

    if enc4_t:
        start = time.time()
        enc4_e = enc4.shorte(text)
        if enc4.shortd(enc4_e) == text:
            print("ENC4.0", time.time()-start)
        else:
            print("ENC4.0 FAIL")

    if enc5_t:
        start = time.time()
        enc5_e = enc5.encrypt(text)
        if enc5.decrypt(enc5_e) == text:
            print("ENC5.5", time.time()-start)
        else:
            print("ENC5.5 FAIL")

    if enc6_t:
        start = time.time()
        enc6_e = enc6.encrypt(text)
        if enc6.decrypt(enc6_e) == text:
            print("ENC6.4", time.time()-start)
        else:
            print("ENC6.4 FAIL")

    if enc7_t:
        start = time.time()
        enc7_e = enc7.encrypt_key(text, "random_key", "salt")
        if enc7.decrypt_key(enc7_e, "random_key", "salt") == text:
            print("ENC7.0", time.time()-start, len(enc7_e), sys.getsizeof(enc7_e))
        else:
            print("ENC7.0 FAIL")

    if enc8_t:
        start = time.time()
        enc8_e = enc8.encrypt_key(text, "random_key", "salt")
        if enc8.decrypt_key(enc8_e, "random_key", "salt") == text:
            print("ENC8.0", time.time()-start, len(enc8_e), sys.getsizeof(enc8_e))
        else:
            print("ENC8.0 FAIL")

    if enc8_2_t:
        start = time.time()
        enc8_2_e = enc8_2.encrypt_key(text, "random_key", "salt")
        if enc8_2.decrypt_key(enc8_2_e, "random_key", "salt") == text:
            print("ENC8.2", time.time()-start, len(enc8_2_e), sys.getsizeof(enc8_2_e))
        else:
            print("ENC8.2 FAIL")

    if enc8_5_t:
        start = time.time()
        enc8_5_e = enc8_5.encrypt_key(text, "random_key", "salt")
        if enc8_5.decrypt_key(enc8_5_e, "random_key", "salt") == text:
            print("ENC8.5", time.time()-start, len(enc8_5_e), sys.getsizeof(enc8_5_e))
        else:
            print("ENC8.5 FAIL")

    if enc8_6_t:
        start = time.time()
        enc8_6_e = enc8_6.encrypt_key(text, "random_key", "salt")
        if enc8_6.decrypt_key(enc8_6_e, "random_key", "salt") == text:
            print("ENC8.6", time.time()-start, len(enc8_6_e), sys.getsizeof(enc8_6_e))
        else:
            print("ENC8.6 FAIL")

    if enc9_0_t:
        start = time.time()
        enc9_0_e = enc9_0.encrypt_key(text, "random_key", "salt")
        if enc9_0.decrypt_key(enc9_0_e, "random_key", "salt") == text:
            print("ENC9.0", time.time()-start, len(enc9_0_e), sys.getsizeof(enc9_0_e))
        else:
            print("ENC9.0 FAIL")

    if enc9_3_t:
        start = time.time()
        enc9_3_e = enc9_3.encrypt_key(text, "random_key", "salt")
        if enc9_3.decrypt_key(enc9_3_e, "random_key", "salt") == text:
            print("ENC9.3", time.time()-start, len(enc9_3_e), sys.getsizeof(enc9_3_e))
        else:
            print("ENC9.3 FAIL")

    if enc9_4_t:
        start = time.time()
        enc9_4_e = enc9_4.encrypt_key(text, "random_key", "salt")
        if enc9_4.decrypt_key(enc9_4_e, "random_key", "salt") == text:
            print("ENC9.4", time.time()-start, len(enc9_4_e), sys.getsizeof(enc9_4_e))
        else:
            print("ENC9.4 FAIL")

    if enc9_5_t:
        start = time.time()
        enc9_5_e = enc9_5.encrypt_key(text, "random_key", "salt")
        if enc9_5.decrypt_key(enc9_5_e, "random_key", "salt") == text:
            print("ENC9.5", time.time()-start, len(enc9_5_e), sys.getsizeof(enc9_5_e))
        else:
            print("ENC9.5 FAIL")

    if enc9_6_t:
        start = time.time()
        enc9_6_e = enc9_6.encrypt_key(text, "random_key", "salt")
        if enc9_6.decrypt_key(enc9_6_e, "random_key", "salt") == text:
            print("ENC9.6", time.time()-start, len(enc9_6_e), sys.getsizeof(enc9_6_e))
        else:
            print("ENC9.6 FAIL")

    if enc9_7_t:
        start = time.time()
        enc9_7_e = enc9_7.encrypt_key(text, "random_key", "salt")
        if enc9_7.decrypt_key(enc9_7_e, "random_key", "salt") == text:
            print("ENC9.7", time.time()-start, len(enc9_7_e), sys.getsizeof(enc9_7_e))
        else:
            print("ENC9.7 FAIL")

    if enc9_8_t:
        start = time.time()
        enc9_8_e = enc9_8.encrypt_key(text, "random_key", "salt")
        if enc9_8.decrypt_key(enc9_8_e, "random_key", "salt") == text:
            print("ENC9.8", time.time()-start, len(enc9_8_e), sys.getsizeof(enc9_8_e))
        else:
            print("ENC9.8 FAIL")

    if enc10_0_t:
        start = time.time()
        enc10_0_e = enc10_0.encrypt_key(text, "random_key", "salt")
        if enc10_0.decrypt_key(enc10_0_e, "random_key", "salt") == text:
            print("ENC10.0", time.time()-start, len(enc10_0_e), sys.getsizeof(enc10_0_e))
        else:
            print("ENC10.0 FAIL")

    if enc11_0_t:
        start = time.time()
        enc11_0_e = enc11_0.encrypt_key(text, "random_key", "salt")
        if enc11_0.decrypt_key(enc11_0_e, "random_key", "salt") == text:
            print("ENC11.0", time.time()-start, len(enc11_0_e), sys.getsizeof(enc11_0_e))
        else:
            print("ENC11.0 FAIL")

    if enc11_1_t:
        start = time.time()
        enc11_1_e = enc11_1.enc_from_pass(text, "random_key", "salt")
        if enc11_1.dec_from_pass(enc11_1_e, "random_key", "salt") == text:
            print("ENC11.1", time.time()-start, len(enc11_1_e), sys.getsizeof(enc11_1_e))
        else:
            print("ENC11.1 FAIL")

    if enc11_x_t:
        start = time.time()
        enc11_x_e = enc11_x.enc_from_pass(text, "random_key", "salt")
        if enc11_x.dec_from_pass(enc11_x_e, "random_key", "salt") == text:
            print("ENC11.x", time.time()-start, len(enc11_x_e), sys.getsizeof(enc11_x_e))
        else:
            print("ENC11.x FAIL")

    #num = ~*~*60408046820
    #print(num)
    #num2 = enc11_x.to_hex(10, 96, num)
    #print(num2)
    #num3 = enc11_x.pass_to_key(num2, str(num))
    #print(num3)

    input("Inp")
    while True:
        enc11_x.enc_file_from_pass("Setup_Factorio_x64_1.1.57.exe", "key", "salt", "enc.renc")
        input()
        enc11_x.dec_file_from_pass("enc.renc", "key", "salt", "test.exe")
        input("Loop.")

