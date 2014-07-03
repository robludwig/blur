import sys
import opencvfxns

if __name__ == '__main__':
	print "blur.py: simple face detector to blur faces in an image"
	if len(sys.argv) < 2:
		print "usage: blur.py image.png"
		sys.exit(0)
	image = load_image(sys.argv[1])
	faces = detect_faces(image)
	for face in faces:
		x, y, w, h = face
        blur_region(image,(x,y), (x+w, y+h))
	save_image( image,sys.argv[1])