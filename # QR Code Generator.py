# QR Code Generator
# author: DekuBeats aka Ninjamin
import qrcode
import random
# example data input
data = "https://www.youtube.com/watch?v=hEBwJpfGUl8"

# output file name  

filename = "qrcode"+str(random.randrange(1,9999999))+".png"
# generating qr code

img = qrcode.make(data)
img.save(filename)
print(filename)

