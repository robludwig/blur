import cv2

CLASSIFIER_XML = "C:\\opencv\\haarcascade_frontalface_alt.xml"

cascade = cv2.CascadeClassifier(CLASSIFIER_XML)

#after experimentation, it seems easier to just use haar frontal cascade for 
#most images, as it gets the best matches for the default use-case
#the following 2 functions are here to allow further experimentation with other cascade detectors
def reload_cascade():
    global cascade
    cascade = cv2.CascadeClassifier(CLASSIFIER_XML)
	
def set_cascade(cascadefile):
	global CLASSIFIER_XML
	CLASSIFIER_XML = cascadefile

def load_image(filename):
    image = cv2.imread(filename)
    return image

def detect_faces(image):
    '''returns a list of all the faces in the image'''
    faces = cascade.detectMultiScale(image)
    return faces

def blur_region(image,x,y,w,h):
	'''blurs a region of the image in-place...'''
    slice = image[y:y+h, x:x+w]
    blurslice = cv2.blur(slice, (50,50))
    image[y:y+h, x:x+w] = blurslice

def save_image(image, filename):
    cv2.imwrite(filename, image)
    
if __name__ == '__main__':
    capture = cv2.VideoCapture(0)
    retval, frame = capture.read()
    filename = "C:\\Users\\Robert\\Desktop\\tester.jpeg"
    outputfilename = "C:\\Users\\Robert\\Desktop\\testerOUT.jpeg"
    cv2.imwrite(filename, frame)
    image = load_image(filename)
    faces = detect_faces(image)
    for face in faces:
        x, y, w, h = faces
        blur_region(image,(x,y), (x+w, y+h))
    cv2.imwrite(outputfilename, image)
