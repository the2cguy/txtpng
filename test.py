import txtpng
import PIL.Image as Image

# Save text inside an image using rgb values
txtpng.encodetxt("Hello, world!").save("output.png")

# Read text inside an image
print(txtpng.decodepng(Image.open("output.png")))