add_library('opencv_processing')

src = loadImage("test.jpg")
size(src.width, src.height, P2D)
opencv = OpenCV(this, src)
opencv.gray()
opencv.threshold(150)
dst = opencv.getOutput()
contours = opencv.findContours()
print "found %d contours" % contours.size()


image(src, 0, 0)
image(dst, src.width, 0)
noFill()
strokeWeight(1)

background(0,0,0)

for contour in contours:
    stroke(255, 255, 255)
    contour.draw()

save("img/contours.jpg")


#    with beginShape():
#        for point in contour.getPolygonApproximation().getPoints():
#            vertex(point.x, point.y)

