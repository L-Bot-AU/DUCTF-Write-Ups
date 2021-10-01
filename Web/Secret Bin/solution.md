# Challenge
Since everyone loves dumping their secrets into pastebin, I decided to make a dedicated service for it instead! I've added few secrets myself to inflate our marketing numbers, I wonder if you can find them.  
  
# Setup
Website: https://web-secret-bin-beabf0f8.chal-2021.duc.tf  
  
# Solution
The source code of the main page sends a request to the `/api/stats` endpoint to find the number of "bins" made on the website. If we visit this path, we see JSON data of a list of timestamps (which appear to be generated in Python with `time.time()` after importing the `time` library) and a count of the number of secrets. Using Python to figure what day the first timestamp is on:
```python
>>> import datetime
>>> date = datetime.datetime.fromtimestamp(1627995373.4724479)
>>> print(date.strftime("%d/%m/%Y"))
03/08/2021
>>> 
```
This is well before the competition date, so the flag is probably the bin made at this timestamp.  
We can try making our own bin with a POST request to `/api/secret` with the content of the bin as the body of the request:
```python
import requests
requests.post("https://web-secret-bin-beabf0f8.chal-2021.duc.tf/api/secret", "bin content").text
```
We receive a hex-like string (e.g. "f3b8c8ca-226e-11ec-8b1e-0401b7194601"). This is recognisable as the UUID format, which is a timestamp format. Upon sending more requests to this endpoint, we see that the first 4 hex bytes ("f3b8c8ca") seem to increase over time until they reach "ffffffff", and then loop over back to "00000000" and increment the next 2 byte part ("226e" becomes "226f"). This indicates the UUID version is 1, so we can generate a UUID timestamp from the first timestamp and visit the bin with that UUID. I could not find an easy way to generate a UUID given some time (only ones that did it for any time), so I modified the Python UUID to compute a UUID with the previously mentioned timestamp. We must also realise that the last 8 hex bytes are based on the MAC address, but after repeatedly making several POST requests to the  `/api/secret` endpoint, we see that they can only be one of 4 values:
```
8421-00155d1c46cb
880f-000d3acaef36
8b1e-0401b7194601
bb4c-0050568f00a9
```
After testing each of these values with `/api/secret/{uuid}`, we find that `2ed2ab7f-f45a-11eb-bb4c-0050568f00a9` is a bin and it contains our flag.  
Flag: **DUCTF{cant_guess_this_one_9ed609c7-8978-4337-a7de-f618b859b998}**
