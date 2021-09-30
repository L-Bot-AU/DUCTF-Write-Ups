# Solution
I found the header by looking at the file in raw bytes, and searched online for the first few characters of the header to determine its file type. I created code to unzip that file, which gave my a new unknown file. I repeated this process alot :'(

For some reason, the python `tarfile` library didn't want to unzip my file - something about invalid file header. I wasted too much time on this problem and created some very ugly code.

```python
# name the original file `flag0.txt`
import bz2
import zipfile
import sys
import lzma
import os
DIRECTORY = "D:\\programming\\competitions CTF\\DownUnder CTF\\"

def BZ2(currF, nextF):
    text = open(currF, 'rb').read()
    text = bz2.decompress(text)
    open(nextF, "wb").write(text)

def ZIPFILE(currF, nextF):
    zip_ref = zipfile.ZipFile(currF, 'r')
    zip_ref.extractall()
    open(nextF, "wb").write(open("flag.txt", "rb").read())

def LZMA(currF, nextF):
    text = open(currF, 'rb').read()
    text = lzma.decompress(text)
    open(nextF, "wb").write(text)

def TARFILE1(currF, nextF):
    cmd = ["tar", "-xzvf", '"' + DIRECTORY + currF + '"']
    response = os.system("tar -xzvf " + currF)
    assert response == 0
    open(nextF, "wb").write(open("flag.txt", "rb").read())

def TARFILE2(currF, nextF):
    tarF = currF.replace("txt", "tar")
    open(tarF, "wb").write(open(currF, "rb").read())
    
    try:
        os.remove("flag.txt")
    except FileNotFoundError:
        pass
    
    cmd = f'''WinRAR.exe x "{DIRECTORY}{tarF}" "{DIRECTORY}"'''
    print(cmd)
    os.system(cmd)
    
    open(nextF, "wb").write(open("flag.txt", "rb").read())

for _ in range(0, 911):
    print(_)
    currF = f'flag{_}.txt'
    nextF = f'flag{_+1}.txt'
    
    try:
        BZ2(currF, nextF)
        continue
    except:
        pass
    
    try:
        ZIPFILE(currF, nextF)
        continue
    except:
        pass
    
    try:
        LZMA(currF, nextF)
        continue
    except:
        pass
    
    try:
        TARFILE1(currF, nextF)
        continue
    except:
        pass
    
    try:
        TARFILE2(currF, nextF)
        continue
    except:
        pass
    
    
    print("ahhh", _)
    fsdds

final = open("flag911.txt").read()
print(base64.b64decode(flag))```

Flag: `DUCTF{babushkas_v0dka_was_h3r3}`
