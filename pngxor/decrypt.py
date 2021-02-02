import sys
from PIL import Image

if len(sys.argv) < 2 or sys.argv[1] == '-h':
    print(
        "Usage: {} <inputa.png> <inputb.png> <xoredoutput.png>".format(
            sys.argv[0]
        )
    )
else:
    aimg = Image.open(sys.argv[1])
    bimg = Image.open(sys.argv[2])
    output = Image.new("RGB", aimg.size)

    width, height = aimg.size

    for x in range(width):
        for y in range(height):
            apix = aimg.getpixel((x, y))
            bpix = bimg.getpixel((x, y))
            opix = tuple([apix[i] ^ bpix[i] for i in range(len(apix))])
            #print("{} ^ {} = {}".format(apix, bpix, opix))
            output.putpixel((x, y), opix)

    output.save(sys.argv[3], 'png')
