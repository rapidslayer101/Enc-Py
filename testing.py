import enclib as enc
#[78, 77, 76, 75]

seed = enc.pass_to_seed(enc.hex_gens(10), enc.hex_gens(10))
print(len(seed), seed)
print(enc.to_hex(96, 10, seed))
print(enc.to_number(seed))

print(enc.seed_to_data(seed))
print(enc.hash_a_file("Cubase Projects.zip"))

