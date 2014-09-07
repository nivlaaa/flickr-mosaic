from PIL import Image

# get the average RGB value for a picture
# box = (left, upper, right, lower)
def get_avg_rgb(img, box):
    r = 0
    g = 0
    b = 0
    num_pixels = (box[2] - box[0]) * (box[3] - box[1])
    for i in range(box[0], box[2]):
	for j in range(box[1], box[3]):
	    pixel = img.getpixel((i, j))
	    r += pixel[0]
	    g += pixel[1]
	    b += pixel[2]
    return (r / num_pixels, g / num_pixels, b / num_pixels)

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
