# Challenge
I've opened a new store that provides free furnishings and floormats. If you know the secret format we might also be able to give you flags...

# Setup
Host: pwn-2021.duc.tf
Port: 31903
Source code: [floormat.py](floormat.py)

# Solution
The code creates a floormat by asking us for a template type and a pattern to use. The template type can either be "Fundamental", "Flabbergasting" or our own custom template, and the pattern is some class which is passed into the template.  
  
We are instructed the template should be composed of "{f}"'s. Analysing the code, we see this works through Python format string, where the selected pattern class is passed into each "f" through the format string:
```python
floormat = template.format(f=pattern)
```
We can exploit this by using our own custom template with whatever format string we want. We can access the list of global variables by referencing {f.\_\_init\_\_.\_\_globals\_\_), and read the flag from there. Steps of reproduction:
<ol>
  <li> Connect the server with nc pwn-2021.duc.tf 31903 </li>
  <li> Enter a string which is neither "Fundamental" nor "Flabbergasting" </li>
  <li> Enter "{f.__init__.__globals__}" and then "F" on a new line </li>
  <li> Enter "Flutter" </li>
  <li> Read the flag from the printed dictionary (under the key "FLAG") </li>
</ol>
Flag: **DUCTF{fenomenal_flags_from_funky_formats_ffffff}**
