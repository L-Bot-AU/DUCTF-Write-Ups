# Challenge
You and two friends have spent the past year playing an ARG that promises valuable treasures to the first team to find three secret shares scattered around the world. At long last, you have found all three and are ready to combine the shares to figure out where the treasure is. Of course, being the greedy individual you are, you plan to use your cryptography skills to deceive your friends into thinking that the treasure is in the middle of no where...  
  
# Setup
Host: pwn-2021.duc.tf  
Port: 31901  
Source code: [treausre.py](treasure.py)  
  
# Solution
On inspection, the algorithm seems to work as follows:
<ol>
  <li> Two random integers between 0 and some known prime (not including either) are generated. </li>
  <li> Three different numbers are created using these two numbers (say a and b) and some secret value (say s): abs, a^2bs and ab^2s, all in modulus p </li>
  <li> We are given abc (now known to you) and two other people receieve a^2bs and ab^2s (not known to us) </li>
  <li> We have to reveal abc so s can be retrieved by having the multiplicative inverse of a^2bs * ab^2s (which is a^3b^3s^2) in mod p multiplied with the cube of our share (a^3b^3s^3). This will result in a^3b^3s^3/a^3/b^3/s^2, which will in turn give s mod p (which are coordinates to some treasure)</li>
</ol>
Our goal is to provide a fake set of coordinates (a constant value defined in the code) and then retrieve the real coordinates ourselves. A useful functionality to achieve this goal is our ability to send fake shares twice before our friends find us too suspicious (i.e. before the server closes).  
  
We can first send the number 1 to have a fake secret with a value of 1/(a^3b^3s^2) mod p revealed. Now that we have the multiplicative inverse of the product of the other two shares, we can compute a solution to the fake set of coordinates (say f) by taking the multiplicative inverse of 1/(a^3b^3s^2) in mod p, multiplying it with f (a^3b^3s^2f mod p) and then taking the cube root of this through the [following algorithm](https://stackoverflow.com/questions/6752374/cube-root-modulo-p-how-do-i-do-this). We then send this value to the server, and it will now compute: (a^3b^3s^2f * 1/(a^3b^3s^2)) = f. Now that our friends have the fake set of coordinates, the server will ask us for the real coordinates. We compute this by simply multiplying our real share with the 1/(a^3b^3s^2) we received in modulus p and then sending it to the server.
