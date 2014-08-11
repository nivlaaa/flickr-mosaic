from PIL import Image

# get the average RGB value for a picture
def get_avg_rgb(file_name):
    image = Image.open(file_name).convert('RGB')
    img = list(image.getdata())
    r = 0
    g = 0
    b = 0
    for pixel in img:
	r += pixel[0]
	g += pixel[1]
	b += pixel[2]
    length = len(img)
    return (r / length, g / length, b / length)
