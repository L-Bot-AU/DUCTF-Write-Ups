# Challenge
What more could you ask for than a program that loads the flag for you? Just answer a few simple questions and the flag is yours!  
  
# Setup
Host: pwn-2021.duc.tf  
Port: 31919  
Executable: [flag_loader](flag_loader)  
  
# Solution
After decompiling the executable with Ghidra, we see that the program starts by calling `init`, which will set an asynchronous signal `SIGALRM` that will halt execution after 60 seconds. Then, it will call three different "check" functions, take the results of each of them, multiply them together and then sleep for that amount of time before the flag is printed. However, there are some problems.  
Check 1 will take in 5 characters, XOR their integer values with the characters "DUCTF" respectively, add all the final values up and verify that the sum is 0 (otherwise the program will exit). This seems to indicate that our input should be "DUCTF", however we run into another issue in that the integer values of the characters are also multiplied together along with the numbers from 1 to 5, and if the result is equal to 0, then the program will exit. However, from the assembly code, we see that only a byte is analysed, which means that even if the resulting product is a multiple of 256, it will be interpreted as 0 (which is the case for DUCTF). However, we can bypass this issue by leveraging the same issue of an integer overflow: we can select a set of characters which, when XOR'd with the characters "DUCTF" and added, will result in 256. For the same reason, it will be interpreted as 0. This means our input characters will be "\x
