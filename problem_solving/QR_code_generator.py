import qrcode 

x = input('Enter the text or the URL :')
y = input('Enter the file name :')
img = qrcode.make(x)

img.save(y)
print ('QR Code saved as {y}')