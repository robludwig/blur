import sys
import opencvfxns

if __name__ == '__main__':
	print "blur.py: simple face detector to blur faces in an image"
	if len(sys.argv) < 2:
		print "usage: blur.py image.png"
		sys.exit(0)
	image = opencvfxns.load_image(sys.argv[1])
	gray_image = opencvfxns.gray_image(image) #do the detection on a grayscale image to speed it up
	faces = opencvfxns.detect_faces(gray_image)
	for face in faces:
		x, y, w, h = face
        opencvfxns.blur_region(image,x,y,w,h)
	opencvfxns.save_image( image,sys.argv[1])