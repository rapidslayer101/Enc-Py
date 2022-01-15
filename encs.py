import sys, time
from multiprocessing import freeze_support
import enc9_5, enc9_4, enc9_3, enc9_0, enc8_6, enc8_5, enc8_2, enc8, enc7, enc6, enc5, enc4, enc3, enc2
import enclib as enc10_x

if __name__ == '__main__':
    freeze_support()
    text = enc10_x.hex_gens(1000000)
    #text = enc9_x.hex_gens(100)
    text = text*10
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
    enc9_5_t = True
    enc10_x_t = True

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

    if enc10_x_t:
        start = time.time()
        enc10_x_e = enc10_x.encrypt_key(text, "random_key", "salt")
        if enc10_x.decrypt_key(enc10_x_e, "random_key", "salt") == text:
            print("ENC9.x", time.time()-start, len(enc10_x_e), sys.getsizeof(enc10_x_e))
            #with open("output.txt", "wb") as f:
            #    if type(enc10_x_e) == list:
            #        for block in enc10_x_e:
            #            f.write(block)
            #    else:
            #        f.write(enc10_x_e)
        else:
            print("ENC9.x FAIL")

    #enc10_x_e = enc10_x.encrypt_key(input(), "random_key", "salt")
    #print(enc10_x_e)
    #print(enc10_x.decrypt_key(enc10_x_e, "random_key", "salt"))

    input("Inp")
    while True:
        #enc10_x.encrypt_file("enc", "Beacon.jar", "key", "salt", "enc.renc")
        enc10_x.encrypt_file("enc", "CubaseProjects.zip", "key", "salt", "enc.renc")
        enc10_x.encrypt_file("dec", "enc.renc", "key", "salt", "test")
        input("Loop.")

    #import time
    #loop = 0
    #start_time = time.time()
    #while True:
    #    loop += 1
    #    random_stuff = enc10_x.hex_gens(1000000)
    #    encrypted = enc10_x.encrypt_key(random_stuff, "random_key", "salt")
    #    if loop % 1 == 0:
    #        print(loop*1000, time.time() - start_time)
    #    if not random_stuff == enc10_x.decrypt_key(encrypted, "random_key", "salt"):
    #        print("fail")
    #        input()

