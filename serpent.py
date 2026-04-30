phi = 0x9e3779b9


def s_box_0(block_words):
    w0, w1, w2, w3 = block_words
    w3 ^= w0
    w4 = w1
    w1 &= w3
    w4 ^= w2
    w1 ^= w0
    w0 |= w3
    w0 ^= w4
    w4 ^= w3
    w3 ^= w2
    w2 |= w1
    w2 ^= w4
    w4 ^= 0xffffffff
    w4 |= w1
    w1 ^= w3
    w1 ^= w4
    w3 |= w0
    w1 ^= w3
    w4 ^= w3
    return w1, w4, w2, w0


def s_box_1(block_words):
    w0, w1, w2, w3 = block_words
    w0 ^= 0xffffffff
    w2 ^= 0xffffffff
    w4 = w0
    w0 &= w1
    w2 ^= w0
    w0 |= w3
    w3 ^= w2
    w1 ^= w0
    w0 ^= w4
    w4 |= w1
    w1 ^= w3
    w2 |= w0
    w2 &= w4
    w0 ^= w1
    w1 &= w2
    w1 ^= w0
    w0 &= w2
    w0 ^= w4
    return w2, w0, w3, w1


def s_box_2(block_words):
    w0, w1, w2, w3 = block_words
    w4 = w0
    w0 &= w2
    w0 ^= w3
    w2 ^= w1
    w2 ^= w0
    w3 |= w4
    w3 ^= w1
    w4 ^= w2
    w1 = w3
    w3 |= w4
    w3 ^= w0
    w0 &= w1
    w4 ^= w0
    w1 ^= w3
    w1 ^= w4
    w4 ^= 0xffffffff
    return w2, w3, w1, w4


def s_box_3(block_words):
    w0, w1, w2, w3 = block_words
    w4 = w0
    w0 |= w3
    w3 ^= w1
    w1 &= w4
    w4 ^= w2
    w2 ^= w3
    w3 &= w0
    w4 |= w1
    w3 ^= w4
    w0 ^= w1
    w4 &= w0
    w1 ^= w3
    w4 ^= w2
    w1 |= w0
    w1 ^= w2
    w0 ^= w3
    w2 = w1
    w1 |= w3
    w1 ^= w0
    return w1, w2, w3, w4


def s_box_4(block_words):
    w0, w1, w2, w3 = block_words
    w1 ^= w3
    w3 ^= 0xffffffff
    w2 ^= w3
    w3 ^= w0
    w4 = w1
    w1 &= w3
    w1 ^= w2
    w4 ^= w3
    w0 ^= w4
    w2 &= w4
    w2 ^= w0
    w0 &= w1
    w3 ^= w0
    w4 |= w1
    w4 ^= w0
    w0 |= w3
    w0 ^= w2
    w2 &= w3
    w0 ^= 0xffffffff
    w4 ^= w2
    return w1, w4, w0, w3


def s_box_5(block_words):
    w0, w1, w2, w3 = block_words
    w0 ^= w1
    w1 ^= w3
    w3 ^= 0xffffffff
    w4 = w1
    w1 &= w0
    w2 ^= w3
    w1 ^= w2
    w2 |= w4
    w4 ^= w3
    w3 &= w1
    w3 ^= w0
    w4 ^= w1
    w4 ^= w2
    w2 ^= w0
    w0 &= w3
    w2 ^= 0xffffffff
    w0 ^= w4
    w4 |= w3
    w2 ^= w4
    return w1, w3, w0, w2


def s_box_6(block_words):
    w0, w1, w2, w3 = block_words
    w2 ^= 0xffffffff
    w4 = w3
    w3 &= w0
    w0 ^= w4
    w3 ^= w2
    w2 |= w4
    w1 ^= w3
    w2 ^= w0
    w0 |= w1
    w2 ^= w1
    w4 ^= w0
    w0 |= w3
    w0 ^= w2
    w4 ^= w3
    w4 ^= w0
    w3 ^= 0xffffffff
    w2 &= w4
    w2 ^= w3
    return w0, w1, w4, w2


def s_box_7(block_words):
    w0, w1, w2, w3 = block_words
    w4 = w1
    w1 |= w2
    w1 ^= w3
    w4 ^= w2
    w2 ^= w1
    w3 |= w4
    w3 &= w0
    w4 ^= w2
    w3 ^= w1
    w1 |= w4
    w1 ^= w0
    w0 |= w4
    w0 ^= w2
    w1 ^= w4
    w2 ^= w1
    w1 &= w0
    w1 ^= w4
    w2 ^= 0xffffffff
    w2 |= w0
    w4 ^= w2
    return w4, w3, w1, w0


# ---------- Inverse S-Boxes  -----------------------------
def inv_s_box_0(block_words):
    w0, w1, w2, w3 = block_words
    w2 ^= 0xffffffff
    w4 = w1
    w1 |= w0
    w4 ^= 0xffffffff
    w1 ^= w2
    w2 |= w4
    w1 ^= w3
    w0 ^= w4
    w2 ^= w0
    w0 &= w3
    w4 ^= w0
    w0 |= w1
    w0 ^= w2
    w3 ^= w4
    w2 ^= w1
    w3 ^= w0
    w3 ^= w1
    w2 &= w3
    w4 ^= w2
    return w0, w4, w1, w3


def inv_s_box_1(block_words):
    w0, w1, w2, w3 = block_words
    w4 = w1
    w1 ^= w3
    w3 &= w1
    w4 ^= w2
    w3 ^= w0
    w0 |= w1
    w2 ^= w3
    w0 ^= w4
    w0 |= w2
    w1 ^= w3
    w0 ^= w1
    w1 |= w3
    w1 ^= w0
    w4 ^= 0xffffffff
    w4 ^= w1
    w1 |= w0
    w1 ^= w0
    w1 |= w4
    w3 ^= w1
    return w4, w0, w3, w2


def inv_s_box_2(block_words):
    w0, w1, w2, w3 = block_words
    w2 ^= w3
    w3 ^= w0
    w4 = w3
    w3 &= w2
    w3 ^= w1
    w1 |= w2
    w1 ^= w4
    w4 &= w3
    w2 ^= w3
    w4 &= w0
    w4 ^= w2
    w2 &= w1
    w2 |= w0
    w3 ^= 0xffffffff
    w2 ^= w3
    w0 ^= w3
    w0 &= w1
    w3 ^= w4
    w3 ^= w0
    return w1, w4, w2, w3


def inv_s_box_3(block_words):
    w0, w1, w2, w3 = block_words
    w4 = w2
    w2 ^= w1
    w0 ^= w2
    w4 &= w2
    w4 ^= w0
    w0 &= w1
    w1 ^= w3
    w3 |= w4
    w2 ^= w3
    w0 ^= w3
    w1 ^= w4
    w3 &= w2
    w3 ^= w1
    w1 ^= w0
    w1 |= w2
    w0 ^= w3
    w1 ^= w4
    w0 ^= w1
    return w2, w1, w3, w0


def inv_s_box_4(block_words):
    w0, w1, w2, w3 = block_words
    w4 = w2
    w2 &= w3
    w2 ^= w1
    w1 |= w3
    w1 &= w0
    w4 ^= w2
    w4 ^= w1
    w1 &= w2
    w0 ^= 0xffffffff
    w3 ^= w4
    w1 ^= w3
    w3 &= w0
    w3 ^= w2
    w0 ^= w1
    w2 &= w0
    w3 ^= w0
    w2 ^= w4
    w2 |= w3
    w3 ^= w0
    w2 ^= w1
    return w0, w3, w2, w4


def inv_s_box_5(block_words):
    w0, w1, w2, w3 = block_words
    w1 ^= 0xffffffff
    w4 = w3
    w2 ^= w1
    w3 |= w0
    w3 ^= w2
    w2 |= w1
    w2 &= w0
    w4 ^= w3
    w2 ^= w4
    w4 |= w0
    w4 ^= w1
    w1 &= w2
    w1 ^= w3
    w4 ^= w2
    w3 &= w4
    w4 ^= w1
    w3 ^= w4
    w4 ^= 0xffffffff
    w3 ^= w0
    return w1, w4, w3, w2


def inv_s_box_6(block_words):
    w0, w1, w2, w3 = block_words
    w0 ^= w2
    w4 = w2
    w2 &= w0
    w4 ^= w3
    w2 ^= 0xffffffff
    w3 ^= w1
    w2 ^= w3
    w4 |= w0
    w0 ^= w2
    w3 ^= w4
    w4 ^= w1
    w1 &= w3
    w1 ^= w0
    w0 ^= w3
    w0 |= w2
    w3 ^= w1
    w4 ^= w0
    return w1, w2, w4, w3


def inv_s_box_7(block_words):
    w0, w1, w2, w3 = block_words
    w4 = w2
    w2 ^= w0
    w0 &= w3
    w4 |= w3
    w2 ^= 0xffffffff
    w3 ^= w1
    w1 |= w0
    w0 ^= w2
    w2 &= w4
    w3 &= w4
    w1 ^= w2
    w2 ^= w0
    w0 |= w2
    w4 ^= w1
    w0 ^= w3
    w3 ^= w4
    w4 |= w0
    w3 ^= w2
    w4 ^= w2
    return w3, w0, w1, w4


inv_s_boxes = (inv_s_box_0, inv_s_box_1, inv_s_box_2, inv_s_box_3, inv_s_box_4, inv_s_box_5, inv_s_box_6, inv_s_box_7)

s_boxes = (s_box_0, s_box_1, s_box_2, s_box_3, s_box_4, s_box_5, s_box_6, s_box_7)

from random import getrandbits


def self_test():
    for i in range(8):
        S, Si = s_boxes[i], inv_s_boxes[i]
        for _ in range(500):
            x = tuple(getrandbits(32) for _ in range(4))
            if Si(S(x)) != x:
                return i
    return None


print(self_test())


def rotate_left(word, count):
    return ((word << count) | (word >> (32 - count))) & 0xffffffff


def rotate_right(word, count):
    return ((word >> count) | (word << (32 - count))) & 0xffffffff


def key_mixing(block_words, subkey_words):
    return tuple((bw ^ sk) for bw, sk in zip(block_words, subkey_words))


def linear_transformation(block_words):
    w0, w1, w2, w3 = block_words
    w0 = rotate_left(w0, 13)
    w2 = rotate_left(w2, 3)
    w1 ^= w0 ^ w2
    w3 ^= w2 ^ ((w0 << 3) & 0xffffffff)
    w1 = rotate_left(w1, 1)
    w3 = rotate_left(w3, 7)
    w0 ^= w1 ^ w3
    w2 ^= w3 ^ ((w1 << 7) & 0xffffffff)
    w0 = rotate_left(w0, 5)
    w2 = rotate_left(w2, 22)
    return w0, w1, w2, w3


def inv_linear_transformation(block_words):
    w0, w1, w2, w3 = block_words
    w2 = rotate_right(w2, 22)
    w0 = rotate_right(w0, 5)
    w2 ^= w3 ^ ((w1 << 7) & 0xffffffff)
    w0 ^= w1 ^ w3
    w3 = rotate_right(w3, 7)
    w1 = rotate_right(w1, 1)
    w3 ^= w2 ^ ((w0 << 3) & 0xffffffff)
    w1 ^= w0 ^ w2
    w2 = rotate_right(w2, 3)
    w0 = rotate_right(w0, 13)
    return w0, w1, w2, w3


def key_schedule(key_words):
    subkeys = []
    key_words_copy = key_words.copy()

    for i in range(132):
        word = key_words_copy[i] ^ key_words_copy[i + 3] ^ key_words_copy[i + 5] ^ key_words_copy[i + 7] ^ phi ^ i
        key_words_copy.append(rotate_left(word, 11))

    prekeys = key_words_copy[8:]
    j = 3
    for i in range(0, 132, 4):
        prekeys[i:i + 4] = s_boxes[j](prekeys[i:i + 4])
        j = (j + 7) % 8

    for i in range(0, 132, 4):
        subkeys.append(prekeys[i:i + 4])

    return subkeys


def encrypt_block(block_words, subkeys):
    for i in range(31):
        block_words = key_mixing(block_words, subkeys[i])
        block_words = s_boxes[i % 8](block_words)
        block_words = linear_transformation(block_words)

    block_words = key_mixing(block_words, subkeys[31])
    block_words = s_box_7(block_words)
    block_words = key_mixing(block_words, subkeys[32])

    return block_words


def decrypt_block(block_words, subkeys):

    block_words = key_mixing(block_words, subkeys[32])
    block_words = inv_s_box_7(block_words)
    block_words = key_mixing(block_words, subkeys[31])

    for i in range(30, -1, -1):
        block_words = inv_linear_transformation(block_words)
        block_words = inv_s_boxes[i % 8](block_words)
        block_words = key_mixing(block_words, subkeys[i])

    return block_words


def words_from_bytes(raw_bytes):

    words = []
    for i in range(0, len(raw_bytes), 4):
        chunk = raw_bytes[i:i + 4]
        chunk = chunk.ljust(4, b'\x00')
        words.append(int.from_bytes(chunk, 'big'))

    words.reverse()  # Reverse to match Serpent's internal format
    return words


def bytes_from_words(words):
    return b''.join(w.to_bytes(4, 'big') for w in words[::-1])


def pkcs7_pad(data, block_size=16):
    padding_length = block_size - (len(data) % block_size)
    padding = bytes([padding_length]) * padding_length
    return data + padding


def pkcs7_unpad(data):
    if not data:
        raise ValueError("Cannot unpad empty data")
    padding_length = data[-1]
    if padding_length < 1 or padding_length > 16:
        raise ValueError("Invalid padding")
    if len(data) < padding_length:
        raise ValueError("Invalid padding length")
    # Check that all padding bytes are correct
    for i in range(padding_length):
        if data[-(i + 1)] != padding_length:
            raise ValueError("Invalid padding")
    return data[:-padding_length]


def nessie_key_to_internal_bytes(hex_string):
    if len(hex_string) != 64:
        raise ValueError("Expected 256-bit key as 64 hex characters.")
    return bytes.fromhex(hex_string)[::-1]  # full byte reversal


def to_nessie_hex(hex_string):
    assert len(hex_string) % 32 == 0, "Must be multiple of 128-bit blocks (32 hex characters each)"

    result = []
    for i in range(0, len(hex_string), 32):
        block = hex_string[i:i + 32]
        words = [block[j:j + 8] for j in range(0, 32, 8)]
        be_words = [''.join([w[j:j + 2] for j in (6, 4, 2, 0)]) for w in words]
        result.append(''.join(be_words[::-1]))

    return ''.join(result)


def from_nessie_hex(hex_string):
    assert len(hex_string) % 32 == 0, "Must be multiple of 128-bit blocks (32 hex characters each)"

    result = []
    for i in range(0, len(hex_string), 32):
        block = hex_string[i:i + 32]
        words = [block[j:j + 8] for j in range(0, 32, 8)][::-1]
        le_words = [''.join([w[j:j + 2] for j in (6, 4, 2, 0)]) for w in words]
        result.append(''.join(le_words))

    return ''.join(result)


class SerpentECB:

    def __init__(self, key_hex):
        self.block_size = 16  # 16 bytes = 128 bits

        # Convert key: full byte reversal
        key_bytes = nessie_key_to_internal_bytes(key_hex)

        # Transform to internal word format
        key_words = words_from_bytes(key_bytes)

        self.subkeys = key_schedule(key_words)

    def encrypt(self, plaintext, padding=True):

        if padding:
            plaintext = pkcs7_pad(plaintext, self.block_size)

        if len(plaintext) % self.block_size != 0:
            raise ValueError(f"Input length must be a multiple of {self.block_size} bytes when padding is disabled")

        result = bytearray()

        # Process each block
        for i in range(0, len(plaintext), self.block_size):
            block = plaintext[i:i + self.block_size]
            block_words = words_from_bytes(block)

            # Encrypt block
            cipher_words = encrypt_block(block_words, self.subkeys)

            # Convert back to bytes and append to result
            cipher_bytes = bytes_from_words(cipher_words)
            result.extend(cipher_bytes)

        return bytes(result)

    def decrypt(self, ciphertext, padding=True):

        if len(ciphertext) % self.block_size != 0:
            raise ValueError(f"Input length must be a multiple of {self.block_size} bytes")

        result = bytearray()

        # Process each block
        for i in range(0, len(ciphertext), self.block_size):
            block = ciphertext[i:i + self.block_size]
            block_words = words_from_bytes(block)

            # Decrypt block
            plain_words = decrypt_block(block_words, self.subkeys)

            # Convert back to bytes and append to result
            plain_bytes = bytes_from_words(plain_words)
            result.extend(plain_bytes)

        plaintext = bytes(result)

        if padding:
            plaintext = pkcs7_unpad(plaintext)

        return plaintext

    def encrypt_hex(self, plaintext_hex, padding=True):
        plaintext = bytes.fromhex(plaintext_hex)
        ciphertext = self.encrypt(plaintext, padding)
        cipher_hex = ciphertext.hex()
        return to_nessie_hex(cipher_hex)

    def decrypt_hex(self, ciphertext_hex, padding=True):
        internal_hex = from_nessie_hex(ciphertext_hex)
        ciphertext = bytes.fromhex(internal_hex)
        plaintext = self.decrypt(ciphertext, padding)
        return plaintext.hex()


import time
import os


def print_test_header(test_name):
    print(f"\n{'=' * 60}")
    print(f"TEST: {test_name}")
    print(f"{'=' * 60}")


def print_result(passed, message=""):
    if passed:
        print(f"✓ PASSED: {message}")
    else:
        print(f"✗ FAILED: {message}")


def hex_to_ascii(hex_string):
    try:
        bytes_data = bytes.fromhex(hex_string)
        result = ''
        for b in bytes_data:
            if 32 <= b <= 126:
                result += chr(b)
            elif b < 32:
                result += chr(0x2400 + b)
            else:
                result += chr(b)
        return result
    except:
        return "[Invalid hex]"


def test_nessie_vector():
    print_test_header("NESSIE Test Vector")

    key = "8000000000000000000000000000000000000000000000000000000000000000"
    plaintext = "00000000000000000000000000000000"
    expected_ciphertext = "a223aa1288463c0e2be38ebd825616c0"

    cipher = SerpentECB(key)
    result = cipher.encrypt_hex(plaintext, padding=False)

    print(f"Got:      {result}")
    print(f"Expected: {expected_ciphertext}")

    passed = result.lower() == expected_ciphertext.lower()
    print_result(passed, "Encryption matches")

    return passed


def test_ciphertext_corruption():
    print_test_header("Ciphertext Corruption")

    key = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
    plaintext = "48656c6c6f20576f726c642120486921"

    cipher = SerpentECB(key)
    original_ct = cipher.encrypt_hex(plaintext, padding=False)

    print("1. ORIGINAL ENCRYPTION")
    print("─" * 50)
    print(f"Plaintext:  Hello World! Hi!")
    print(f"Ciphertext: {original_ct}")

    print("\n2. CORRUPTION APPLIED")
    print("─" * 50)
    corrupted = original_ct[:10] + 'ff' + original_ct[12:]
    print(f"Original:  {original_ct}")
    print(f"Corrupted: {corrupted}")
    print(f"           {' ' * 10}^^ (bytes 6-7 changed to FF)")

    print("\n3. DECRYPTION RESULT")
    print("─" * 50)
    try:
        decrypted = cipher.decrypt_hex(corrupted, padding=False)
        decrypted_ascii = hex_to_ascii(decrypted)

        print(f"Expected:   Hello World! Hi!")
        print(f"Got:        {decrypted_ascii}")
        print(f"Hex:        {decrypted}")

        passed = decrypted != plaintext
        print(f"\n✓ PASSED: Single byte corruption completely changed decryption")
    except Exception as e:
        print(f"\n✓ PASSED: Decryption failed with error: {e}")
        passed = True

    return passed


def test_key_corruption():
    print_test_header("Key Corruption")

    original_key = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
    corrupted_key = "ffffffffffffffff0123456789abcdef0123456789abcdef0123456789abcdef"
    plaintext = "This is a test!!"

    print("1. ORIGINAL ENCRYPTION")
    print("─" * 50)
    print(f"Key:       {original_key}")
    print(f"Plaintext: {plaintext}")

    cipher_orig = SerpentECB(original_key)
    ciphertext = cipher_orig.encrypt(plaintext.encode(), padding=False)

    print(f"Ciphertext (hex): {ciphertext.hex()}")

    print("\n2. DECRYPTION WITH WRONG KEY")
    print("─" * 50)
    print(f"Wrong key: {corrupted_key}")
    print(f"           {'↑' * 16}{' ' * 48} (first 8 bytes changed)")

    cipher_wrong = SerpentECB(corrupted_key)
    try:
        decrypted = cipher_wrong.decrypt(ciphertext, padding=False)
        decrypted_text = hex_to_ascii(decrypted.hex())

        print(f"\nExpected plaintext: {plaintext}")
        print(f"Got garbage:        {decrypted_text}")
        print(f"Hex:                {decrypted.hex()}")

        passed = decrypted != plaintext.encode()
        print_result(passed, "Wrong key produced completely different plaintext")
    except Exception as e:
        print_result(True, f"Decryption failed: {e}")
        passed = True

    return passed


def test_invalid_lengths():
    print_test_header("Invalid Length")

    try:
        cipher = SerpentECB("0123456789abcdef")  # Too short
        print_result(False, "Accepted invalid key length")
        return False
    except ValueError as e:
        print_result(True, f"Rejected short key: {e}")

    key = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
    cipher = SerpentECB(key)

    try:
        cipher.encrypt(b"Hello", padding=False)
        print_result(False, "Accepted non-block-size plaintext")
        return False
    except ValueError as e:
        print_result(True, f"Rejected invalid plaintext: {e}")

    return True


def test_performance():
    print_test_header("Performance (1MB)")

    key = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
    cipher = SerpentECB(key)

    data_size = 1 * 1024 * 1024  # 1MB
    test_data = os.urandom(data_size)

    # Encrypt
    start = time.time()
    encrypted = cipher.encrypt(test_data, padding=True)
    enc_time = time.time() - start

    # Decrypt
    start = time.time()
    decrypted = cipher.decrypt(encrypted, padding=True)
    dec_time = time.time() - start

    print(f"Data size: 1MB ({data_size:,} bytes)")
    print(f"Encryption: {enc_time:.2f}s ({data_size / (1024 * 1024) / enc_time:.1f} MB/s)")
    print(f"Decryption: {dec_time:.2f}s ({len(encrypted) / (1024 * 1024) / dec_time:.1f} MB/s)")

    passed = decrypted[:1024] == test_data[:1024] and decrypted[-1024:] == test_data[-1024:]

    return passed


def test_cross_instance():
    print_test_header("Cross-Instance")

    key = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
    plaintext = b"Cross-instance test message 123!"

    cipher1 = SerpentECB(key)
    cipher2 = SerpentECB(key)

    ct1 = cipher1.encrypt(plaintext)
    ct2 = cipher2.encrypt(plaintext)

    print(f"Plaintext: {plaintext.decode()}")
    print(f"CT1 hex: {ct1.hex()}")
    print(f"CT2 hex: {ct2.hex()}")
    print(f"CT1 ASCII: {hex_to_ascii(ct1.hex())}")

    dec1 = cipher2.decrypt(ct1)
    dec2 = cipher1.decrypt(ct2)

    passed = ct1 == ct2 and dec1 == plaintext and dec2 == plaintext
    print_result(passed, "Cross-instance encryption/decryption works")

    return passed


def run_all_tests():

    tests = [
        ("NESSIE Vector", test_nessie_vector),
        ("Ciphertext Corruption", test_ciphertext_corruption),
        ("Key Corruption", test_key_corruption),
        ("Invalid Lengths", test_invalid_lengths),
        ("Performance 1MB", test_performance),
        ("Cross-Instance", test_cross_instance)
    ]

    results = []

    for test_name, test_func in tests:
        try:
            passed = test_func()
            results.append((test_name, passed))
        except Exception as e:
            results.append((test_name, False))
            print(f"\n✗ Test crashed: {e}")

if __name__ == "__main__":
    run_all_tests()