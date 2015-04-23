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

# for contour in contours:
#     stroke(255, 255, 255)
#     contour.draw()
scaler = 1.5
stroke(255)
pushMatrix()
translate(100,10)
for c in range(0,len(contours)):
    countour = contours[c]
#     print countour
    points = countour.getPolygonApproximation().getPoints()
    beginShape()
    for p in points:
        vertex(p.x*scaler, p.y*scaler)
    endShape(CLOSE)
popMatrix()


save("img/contours.jpg")

