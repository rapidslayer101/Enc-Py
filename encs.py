import time
from multiprocessing import freeze_support
import enc9_0, enc8_6, enc8_5, enc8_2, enc8, enc7, enc6, enc5, enc4, enc3, enc2
import enclib as enc9_x

if __name__ == '__main__':
    freeze_support()
    text = enc9_x.hex_gens(1000000)
    #text = enc9_x.hex_gens(100)
    #text = text*10
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
    enc9_0_t = True
    enc9_x_t = True

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
            print("ENC7.0", time.time()-start)
        else:
            print("ENC7.0 FAIL")

    if enc8_t:
        start = time.time()
        enc8_e = enc8.encrypt_key(text, "random_key", "salt")
        if enc8.decrypt_key(enc8_e, "random_key", "salt") == text:
            print("ENC8.0", time.time()-start)
        else:
            print("ENC8.0 FAIL")

    if enc8_2_t:
        start = time.time()
        enc8_2_e = enc8_2.encrypt_key(text, "random_key", "salt")
        if enc8_2.decrypt_key(enc8_2_e, "random_key", "salt") == text:
            print("ENC8.2", time.time()-start)
        else:
            print("ENC8.2 FAIL")

    if enc8_5_t:
        start = time.time()
        enc8_5_e = enc8_5.encrypt_key(text, "random_key", "salt")
        if enc8_5.decrypt_key(enc8_5_e, "random_key", "salt") == text:
            print("ENC8.5", time.time()-start)
        else:
            print("ENC8.5 FAIL")

    if enc8_6_t:
        start = time.time()
        enc8_6_e = enc8_6.encrypt_key(text, "random_key", "salt")
        if enc8_6.decrypt_key(enc8_6_e, "random_key", "salt") == text:
            print("ENC8.6", time.time()-start)
        else:
            print("ENC8.6 FAIL")

    if enc9_0_t:
        start = time.time()
        enc9_0_e = enc9_0.encrypt_key(text, "random_key", "salt")
        if enc9_0.decrypt_key(enc9_0_e, "random_key", "salt") == text:
            print("ENC9.0", time.time()-start)
        else:
            print("ENC9.0 FAIL")

    if enc9_x_t:
        start = time.time()
        enc9_x_e = enc9_x.encrypt_key(text, "random_key", "salt")
        if enc9_x.decrypt_key(enc9_x_e, "random_key", "salt") == text:
            print("ENC9.2", time.time()-start)
        else:
            print("ENC9.2 FAIL")

    seed = enc9_x.pass_to_seed("key", "salt")
    input("Inp")
    while True:
        enc9_x.encrypt_file("enc", "Beacon.jar", seed, "enc.renc")
        input()
        enc9_x.encrypt_file("dec", "enc.renc", seed, "test")
        input("Loop.")

    #import time
    #loop = 0
    #start_time = time.time()
    #while True:
    #    loop += 1
    #    random_stuff = enc9.hex_gens(1000)
    #    encrypted = enc9.encrypt(random_stuff, "key-", "salt")
    #    print(loop*1000, time.time()-start_time)
    #    if not random_stuff == enc9.decrypt(encrypted, "key-", "salt"):
    #        print("fail")
    #       input()

