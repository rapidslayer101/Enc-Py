import enclib11_10 as enc
from time import perf_counter

start = perf_counter()
key = enc.pass_to_key("hello", "world")
end = perf_counter()
print(end - start)
print(key, len(key))

enc_text = enc.enc_from_key("good evening lewis how are you doing?", key)
print(enc_text)

with open("enc.txt", "rb") as file:
    enc_text = file.read()
dec_text = enc.dec_from_key(enc_text, key)
print(dec_text)
