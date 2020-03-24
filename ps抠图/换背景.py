import base64
from PIL import Image
 
from aip import AipBodyAnalysis

def get_file(filePath):
	with open(filePath, "rb") as fp:
		return fp.read()

def body_seg(filename = "./pic/test.jpg", savefilename="./pic/fore.jpg"):
	APP_ID = '19037846'
	API_KEY = 'pi8i47A8jGBH1VZDr8ioqgfC'
	SECRET_KEY = 'qwcqweVfjf9pX2fB6MykU15u6XszXko4'
	client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)
	image = get_file(filename)
	options = {}
	options["type"] = "foreground"
	res = client.bodySeg(image, options)
	foreground = base64.b64decode(res["foreground"])
	with open(savefilename, "wb") as f:
		f.write(foreground)

def combine(foreimage, baseimage, rate):
	base_img = Image.open(baseimage)
	backwidth, backheight = base_img.size

	fore_image = Image.open(foreimage)
	width, height = fore_image.size

	fore_image = fore_image.resize((int(width*rate), int(height*rate)))
	width, height = fore_image.size
	r, g, b, a = fore_image.split()
	box = (int(backwidth/2 - width/2), backheight - height, int(backwidth/2 + width/2), backheight)
	base_img.paste(fore_image, box, mask = a)
	return base_img



if __name__ == "__main__":
	outputimage = "./pic/out.png"
	body_seg(filename = "./pic/test.jpg", savefilename = "./pic/fore.jpg")
	#filename = "out/{}.png".format(outputimage)
	combine(foreimage = "./pic/fore.jpg", baseimage = "./pic/bg.jpg", rate = 0.9).save("./pic/rseult.png")

