from PIL import Image
# some basic rule

# mac = Image.open('imag\example.jpg')
# # type(mac)
# print(mac.size)
# print(mac.filename)
# print(mac.format_description)
# mac.crop((0,0,100,100)).show()
# mac.show()

# pencil layout
pencils = Image.open("imag\pencils.jpg")
# pencils.show()

# Start at top corner (0,0)
x = 0
y = 0

# Grab about 10% in y direction , and about 30% in x direction
w = 1950/3
h = 1300/10

# some = pencils.crop((x,y,w,h))
some = pencils.crop((0,0,200,100))
pencils.paste(some,box = (700,0))
# pencils.show()

# resize

h,w = pencils.size
new_h = int(h/3)
new_w = int(w/3)
pencils.resize((new_h,new_w))
pencils.show()