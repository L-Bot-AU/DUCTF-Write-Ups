# Challenge

Are you ready to start your journey?

# Solution

In the challenge statement, we are given the bash command `nc pwn-2021.duc.tf 31906`.
Upon running it, we first get a prompt: `wh47 15 y0ur n4m3 h4ck3r?`.
Inputting any string will receive a long message, which ends with a second prompt: `50 4r3 y0u 4c7u4lly 4 h4ck3r?`.
This prompt rquires a specific "yes" answer, upon which the flag is revealed:

DUCTF{w3lc0m3_70_7h3_duc7f_7hund3rd0m3_h4ck3r}
