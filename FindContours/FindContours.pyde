add_library('opencv_processing')

# define Polygon class with stored coordinates & centerpoint of detected blobs
class Polygon:
    def __init__(self, coords):
        self.coordinates = coords
        xSum = 0
        ySum = 0
        for coord in self.coordinates:
            xSum += coord[0]
            ySum += coord[1]
        xCenter = xSum / len(self.coordinates)
        yCenter = ySum / len(self.coordinates)
        self.center = [xCenter,yCenter]
        
    # draw module to create a single shape            
    def drawPoly(self):
        shapey = createShape()
        shapey.beginShape()
        for coord in self.coordinates:
            shapey.vertex(coord[0]-self.center[0],coord[1]-self.center[1])
        shapey.endShape(CLOSE)
        shape(shapey,self.center[0],self.center[1])
        
    # scale module for resized polygons    
    def drawPolyScaled(self, faktor):
        shapey = createShape()
        shapey.beginShape()
        for coord in self.coordinates:
            shapey.vertex((coord[0]-self.center[0])*faktor,(coord[1]-self.center[1])*faktor)
        shapey.endShape(CLOSE)
        shape(shapey,self.center[0],self.center[1])
        
    # number of scaled drawn polygons
    def drawMultiplePoly(self):
        i = 0
        while i < 5:
            self.drawPolyScaled(1 + (i * 0.2))
            i = i + 1


src = loadImage("thirteen.jpg")
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
strokeWeight(1.5)

background(0,0,0)
image(src,0,0)
stroke(255)


# store detected contours into a list and transfer data into coords
for c in range(0,len(contours)):
    countour = contours[c]
    points = countour.getPolygonApproximation().getPoints()
    
    #store point coords into a list 
    contourCoords = []
    
    for p in points:
        contourCoords.append([p.x, p.y])
        
    contourPoly = Polygon(contourCoords)
    contourPoly.drawMultiplePoly()
    
save("img/contours_.jpg")

