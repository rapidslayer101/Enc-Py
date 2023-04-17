import enclib as enc
from time import perf_counter

start = perf_counter()
key = enc.pass_to_key("hello", "world")
end = perf_counter()
print(end - start)
print(key, len(key))

with open("test.txt", "rb") as file:
    enc_text = file.read()
dec_text = enc.dec_from_key(enc_text, key)
print(dec_text)
