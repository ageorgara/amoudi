import cv2

folder = "/home/ageorg/Documents/amoudi/OsteriaX Free Website Template - Free-CSS.com/markups-osteriax/assets/img/gallery/asd/"
files = [
	'20200606_163642.jpg',
	'20200606_163649.jpg',
	'20200615_200141.jpg',
	'20200615_200150.jpg',
	'20200630_152746.jpg',
	'20200701_193901.jpg',
	'DSC_0453.JPG',
	'DSC_0454.JPG',
	'DSC_0455.JPG',
	'DSC_0456.JPG',
	'DSC_0457.JPG',
	'DSC_0458.JPG',
	'DSC_0459.JPG',
	'DSC_0460.JPG',
	'DSC_0461.JPG',
	'DSC_0462.JPG',
	'DSC_0463.JPG',
	'DSC_0464.JPG',
	'DSC_0465.JPG',
	'DSC_0466.JPG',
	'DSC_0467.JPG',
	'DSC_0468.JPG',
	'DSC_0469.JPG',
	'DSC_0470.JPG',
	'DSC_0471.JPG',
	'DSC_0472.JPG',
	'DSC_0473.JPG',
	'DSC_0474.JPG',
	'DSC_0475.JPG',
	'DSC_0476.JPG',
	'DSC_0477.JPG',
	'DSC_0478.JPG',
	'DSC_0479.JPG',
	'DSC_0480.JPG',
	'DSC_0481.JPG',
	'IMG_20200615_200502_278.jpg',
	'IMG_20200625_162721_534.jpg',


]
for file in files:
	img = cv2.imread(f'{folder}/{file}', cv2.IMREAD_UNCHANGED)
	# print('Original Dimensions : ',img.shape)
	name, suffix = file.split(".")
	scale_percent = 60  # percent of original size
	width = int(img.shape[1] * scale_percent / 100)
	height = int(img.shape[0] * scale_percent / 100)
	dim = (width, height)
	# resize image
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	print('Resized Dimensions : ',resized.shape)

	# cv2.imshow(file,resized)
	filename = f'{folder}/{name}.{suffix}'
	print(filename)
	cv2.imwrite(filename, resized)