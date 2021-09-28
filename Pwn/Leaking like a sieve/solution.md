# Challenge
This program I developed will greet you, but my friend said it is leaking data like a sieve, what did I forget to add?  
  
# Setup
Host: pwn-2021.duc.tf  
Port: 31918  
Executable: [hellothere](hellothere)  
  
# Solution
After decompiling the program with ghidra, we see that the program gets our name with `fgets` (no buffer overflow since strict size is set) before printing "Hello there" and then our input on a new line, both with `printf`. The vulnerability here is clearly a format string exploit which `printf` will process and use to read from the stack. We can simply try to find where the pointer to the character array is located on the stack with %n$s, where n represents the nth value (i.e. nth address). After testing, we find that %6$s works.  
Flag: **DUCTF{f0rm4t_5p3c1f13r_m3dsg!}**
