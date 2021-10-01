# Challenge
I heard this is the coolest site for cowboys and can you find a way in?  
  
# Setup
Website: https://web-cowboy-world-54f063db.chal-2021.duc.tf  
  
# Solution
Upon visiting the website, we are greeted with a login page containing a user and password field. `/robots.txt` (text file used to indicate to search engines which file(s) or directory/directories not to include) includes an entry for `/sad.eml`. When we visit that path on the website, an email file is downloaded. We can view its contents with a text editor and find this string:
```
thats why a 'sadcowboy' is only allowed to go into our website
```
This indicates that only the username `sadcowboy` allows access to the website. Now, for the password field, upon entering a `'`, an internal server error is raised. This indicates a SQL vulnerability due to unescaped characters, which we can exploit with SQL injection. One common payload is `'OR '1'='1`, which works and allows us to login.  
Flag: **DUCTF{haww_yeeee_downunderctf?}**
