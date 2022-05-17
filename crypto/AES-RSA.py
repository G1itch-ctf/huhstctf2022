from Crypto.Cipher import AES
from gmpy2 import *
from Crypto.Util.number import *

e = 65537
p = getPrime(256)
q = getPrime(256)
n = p * q
d = invert(e, (p - 1) * (q - 1))
dp = d % (p - 1)
c = pow(iv, e, n)
print("n: ", n)
print("dp: ", dp)
print("c: ", c)
# n: 5766743508310714073075161276120917490163868280795133567084592868982001955629702827313910931600794072674283091302146147322282502505929962892644016648996053
# dp: 41852205477497822452506248961946170598313615327504272425961239039237399320533
# c: 986109478730712690324523855082887490415597684402163294749443046067281967871549245153673979135488909876922850914508937986802561520397496236961396574611610


key = '+++++ +++[- >++++ ++++< ]>+++ ++++. --.<+ +++[- >++++ <]>++ +++.< ++++[->--- - <] > - -----.-.< + +++[- > ++++ <] > ++ ++++.+.--- --.< + ++[-> --- <]> ---- -.< ++ ++[-> ++++ <] > ++.< ++++ ++[-> ----- - <] > - -.< ++ ++[-> ++++ <] > +.-.< +++ [->++ + <] > + ++.< + ++[-> --- <] > ----.< +++ +[->+ +++ <] > +++++++.< ++++[ ->--- - <] > - -.--.< ++++ [->-- -- <] > -.< ++ ++[-> ++++ <] > +++.----.< +++ [->++ + <] > +.++++ +++.< ++++[ ->--- - <] > - -.< ++ +[->+ ++ <] >++.++ +++.+.< +++ [->-- - <] > - -----.++++ +.+++ ++.-- --.< + ++[-> +++ <]> +++.< +++[ ->--- <] > -- ----.--.< + +++[- > ---- <] > -- -.< ++ ++[-> ++++ <] > ++.-.< ++ +[->+ ++ <] > ++.++ ++.++ +.< ++ +[->- -- <] > -----.++++ +++.++++.< +++[- > --- <] > --.++.++ +++.< +++[- > +++ <] > +++.--.< ++++[ ->---- <] > -.+++.< +++[ ->+++ <] > +.< ++++ [->-- -- <] > ---.- ---.... < ++ ++++[->--- --- <] > ---- ----- ---.- --.< '

# Encrypt flag
flag = 'xxxxxxxxxxxxxx'
aes = AES.new(key, AES.MODE_CBC, iv)
ciphertext = aes.encrypt(flag)
print(ciphertext)

# ciphertext= 'a141692e832cc24b21c136a98daff057'