size(100, 100, P2D)
# Creating the PShape as a square. The
# numeric arguments are similar to rect().
square = createShape(RECT, 0, 0, 50, 50)
square.setFill(color(0, 0, 255))
square.setStroke(False)
shape(square, 25, 25)

size(100, 100, P2D)
# Creating a custom PShape as a square, by
# specifying a series of vertices.
s = createShape()
s.beginShape()
s.fill(0, 0, 255)
s.noStroke()
s.vertex(0, 0)
s.vertex(0, 50)
s.vertex(50, 50)
s.vertex(50, 0)
s.endShape(CLOSE)
shape(s, 25, 25)

size(100, 100, P2D)
s = createShape()
s.beginShape(TRIANGLE_STRIP)
s.vertex(30, 75)
s.vertex(40, 20)
s.vertex(50, 75)
s.vertex(60, 20)
s.vertex(70, 75)
s.vertex(80, 20)
s.vertex(90, 75)
s.endShape()
shape(s, 0, 0)

size(100, 100, P2D)
# Create the shape group
alien = createShape(GROUP)
# Make two shapes
head = createShape(ELLIPSE, -25, 0, 50, 50)
head.setFill(color(255))
body = createShape(RECT, -25, 45, 50, 40)
body.setFill(color(0))
# Add the two "child" shapes to the parent group
alien.addChild(body)
alien.addChild(head)

background(204)
translate(50, 15)
shape(alien)  # Draw the group
