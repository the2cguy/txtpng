import PIL.Image as Image
import math

# Function to reduce the resolution of the pixels (to avoid compression error)
def reducer(rgb):
    newrgb = [0, 0, 0]
    for i in range(3):
        newrgb[i] = round(rgb[i]/128)*128
    return (newrgb[0], newrgb[1], newrgb[2])

def encodetxt(text: str):
    hex = (text + " ").encode('utf-8').hex()
    pixels = len(hex)/3
    pixels = math.sqrt(pixels)
    pixels = math.ceil(pixels)
    outimg = Image.new('RGB', (pixels, pixels))

    i = 0
    for y in range(outimg.height):
        for x in range(outimg.width):
            try:
                outimg.putpixel((x, y), (int(hex[i], 16)*16, int(hex[i+1], 16)*16, int(hex[i+2], 16)*16))
            except:
                pass
            i+=3
    return outimg

def decodepng(image: Image):
    outhex = ""
    for y in range(image.height):
        for x in range(image.width):
            outk = ""
            for i in range(3):
                outk += hex(math.floor(image.getpixel((x, y))[i]/16)).split("0x")[1]
            outhex += (outk)
    if len(outhex) % 2 != 0:
        outhex += "1"
    return (bytes.fromhex(outhex).decode("ascii", "ignore"))