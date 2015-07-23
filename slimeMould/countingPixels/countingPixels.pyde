add_library('video')
add_library('opencv_processing')

video = None
opencv = None

def setup():
    src = loadImage("slime.png")
    size(src.width, src.height, P2D)
    
    image(src, 0, 0)
    
    whitePixels = opencv.countNonZero(src)
    print "Found %d white pixels in" % whitePixels.size()
