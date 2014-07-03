blur
====

command line photo blurring tool for python

usage: blur.py image
where image is a supported image format like png, jpg, tiff, etc. 
blur will overwrite the image in place

This is a port of a web2py webapp I made with a coworker that detects faces in photographs and blurs them out automatically.
This project requires a working installation of OpenCv on the machine its running on.

The haar cascade file included in the project is chosen from those available in OpenCV's main repo. Substituting with a different cascade or training
a new one are some very long-term goals for this project.

