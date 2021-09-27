# Challenge

We intercepted further communications between the two. This text was sent shortly before we lost track of one of the suspects, with an image attached. Can you work out what they're talking about?

Okay, please promise not to judge me, but I might have ended up catching the wrong train again. Though I think I'm still in Australia this time (at least it isn't like that time in Norway LOL). I managed to snap a picture before we went past this station… you have any ideas where I might be?

Please tell us the name of the station, with any spaces replaced by underscores.

Flag format: `DUCTF{station_name}`

File: [image.png](https://github.com/L-Bot-SBHS/DUCTF-Write-Ups/blob/master/OSINT/(back)%20On%20the%20rails/image.png)

# Solution

This problem was fairly straightforward, given the context of the other OSINT problems. With the prompts of a) recalling that a team member had mentioned a plane
touching down in Melbourne during a rant about the problem [eyespy](https://github.com/L-Bot-SBHS/DUCTF-Write-Ups/tree/master/OSINT/eyespye), and b) another team
member's comment that the station looked "abandoned", a quick search of "abandoned train stations melbourne" on google images led to [this](https://www.google.com/search?q=abandoned+train+stations+melbourne&sxsrf=AOaemvI6fnLZ9nkK03qY_mbrxWDQKAXR-Q:1632617322883&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj5kda8tZvzAhVpwjgGHb7mDuoQ_AUoAnoECAEQBA&biw=1440&bih=706&dpr=1#imgrc=DyhapvndtFAZAM)
image, which is strikingly similar due to the graffiti on the left side of the image along with other giveaways. Thus, we get the flag:

DUCTF{general_motors_station}
