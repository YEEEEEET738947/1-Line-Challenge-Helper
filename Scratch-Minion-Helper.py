try:
    from PIL import Image, ImageColor
except:
    print("Please install PIL using pip install pillow")
    quit()
from time import sleep
c = ""
s = ""
b = ""

print("Put Picture in the same destination as this script\n\n")
sleep(1.5)
print("Ready")
ready = input("(y/n)\t").lower()
if ready != "y":
    print("goodbye")
    quit()
print("What is the name of the file in the destination? + extension\t")
name = input("")



try:
    bee = Image.open(name).resize((360, 360)).transpose(Image.ROTATE_90).transpose(Image.FLIP_LEFT_RIGHT)
    bee = bee.convert('HSV')
    pixels = bee.load()
    for x in range(bee.size[0]):
        
        for y in range(bee.size[1]):
            c += str(round((pixels[x, 359-y][0] / 255) * 100)).zfill(3)
            s += str(round((pixels[x, 359-y][1] / 255) * 100)).zfill(3)
            b += str(round((pixels[x, 359-y][2] / 255) * 100)).zfill(3)

    with open("c.txt", "w+") as f:
        f.write(c)

    with open("s.txt", "w+") as f:
        f.write(s)

    with open("b.txt", "w+") as f:
        f.write(b)
    print("Remix my scratch project and copy and paste c.txt to the c variable, b.txt to the b variable and s.txt to the s variable. Don't forget to thank me @goomaster242")
except:
    print("file not in folder, does not exist or you spelt it wrong")
