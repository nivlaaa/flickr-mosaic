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

# resize image to a square with a certain side length
def resize_img(img, length):
    w = img.size[0]
    h = img.size[1]

    longer = w if w > h else h
    shorter = w if w < h else h
    lower_bound = (longer / 2) - (shorter / 2)
    upper_bound = (longer / 2) + (shorter / 2)

    # crop image to a square first
    bounding_box = (0, lower_bound, h, upper_bound) if w > h else (lower_bound, 0, upper_bound, w)
    bounding_box = (lower_bound, 0, upper_bound, h) if w > h else (0, lower_bound, w, upper_bound)
    cropped = img.crop(bounding_box)

    # resize image to be length long
    resized = cropped.resize((length, length))
    return resized 
