# Challenge
Fool me once, shame on you. Fool me twice, shame on me.  
  
# Setup
Host: pwn-2021.duc.tf  
Port: 31921  
Executable: [outBackdoor](outBackdoor)  
  
# Solution
After decompiling the executable with Ghidra, we see that input is retrieved through the function `gets`, which does not place a limit on the number of bytes read. We also see that there is another function `outBackdoor`, which acts as a backdoor which, when we execute, will run /bin/sh so that we can print out the flag file.  
  
Our exploit will work by performing overflowing the buffer and overwriting the return pointer stored on the stack with a new one. We can retrieve the address of the `outBackdoor` function by loading the program in gdb and running `info functions` (we can also see from the `checksec` command that PIE is disabled, so all addresses are fixed):  
[GDB output](gdbout.png)  
We run into an issue however: for some reason, our payload seems to work locally, however the server seems to inexplicably close after we run the `outBackdoor` function. This is because the `movaps` command requires the stack to be aligned in 8 bytes, so we can add an address which jumps to a `ret` instruction in order to achieve this.  
Final payload: `thing`  
Flag: THING  
