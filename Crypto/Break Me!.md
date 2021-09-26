# Challenge
AES encryption challenge.

Author: 2keebs

# Server
Host: pwn-2021.duc.tf
Port: 31914
Source code: [aes_ecb.py](aes_ecb.py)

# Solution
From the source code, we see that our input is encoded into bytes, prepended with the `flag` and encrypted with the `enc` function:
```python
msg = input('Enter plaintext:\n').strip()
pt = flag + str.encode(msg)
ct = enc(pt)
```
However, this is not the full plaintext to be encrypted: in the `enc` function, `key` is also appended to the entire thing before it is padded with 0's into 16 byte blocks and then encrypted with AES ECB. This algorithm encrypts each 16-byte block of a message separately with the same key, however this is a major vulnerability as blocks with the same content will result in the [same output](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_codebook_(ECB)).

After connecting to the server with `nc pwn-2021.duc.tf 31914` and entering nothing, we get the base64 string `8MAq3pGs7/KTcv0c3ijqTJhv/z9V8QA7l9TkMkU72YKbxdZ2EbAlvdn8lZjYaWuV`, which decodes to a 48-byte string. If we enter 1 character (such as 0), we get `8MAq3pGs7/KTcv0c3ijqTJhv/z9V8QA7l9TkMkU72YL2PTAWGv6g8+vkWN9v1s/UySPAtunw8lTSmucLjij7WA==`, which decodes to a 64-byte string. Since the key 128-bit AES-ECB has to be 16 bytes long, it indicates adding a character to the plaintext required another 16-byte block to be added, so the flag must be 32 bytes. This is the format of the plaintext:
`[16 bytes of flag][16 bytes of flag][our payload][16 bytes of key][padding]`

Realise we can "dislodge" the key partially with our payload so that only part of it falls in a 16 byte block (and we can control the rest of the block with whatever characters we want), and then progressively bruteforce what each character is (much more efficient than bruteforcing the entire key) by checking if the two blocks are the same or not. For example, to get the first character, we send 15 0's, some `check_char` character which we will bruteforce for and 15 more 0's:
`[16 bytes of flag][16 bytes of flag][[15 0's] + [check_char]][[15 0's] + first byte of key][rest of key + padding]`
While bruteforcing for each possible value of `check_char`, once the third and fourth blocks in the encrypted ciphertext are the same, we know `check_char` will be the same as the first byte of the key. We can repeat this for the second byte with 14's, the first byte of the key, `check_char` and then 14 more 0's:
`[16 bytes of flag][16 bytes of flag][[14 0's] + [first byte of key] + [check_char]][[14 0's] + first byte of key + second byte of key][rest of key + padding]`
and so on until we figure out all characters in the key: **!\_SECRETSOURCE\_!**. Finally, we can decrypt our original output after entering nothing (which would be the encryption of `flag + key`) with the known `key` through AES-ECB and retrieve the flag: **DUCTF{ECB_M0DE_K3YP4D_D474_L34k}**

# Note
There was a problem with using the socket module in that requests seemed to be unexpectedly stitched together or mixed up, so we had to alternate between appending the current value and previous value of `chec_char`, and we also had to progressively modify our code with the part of the key that we knew was correct.
