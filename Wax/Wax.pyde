add_library('opencv_processing')


age = int(random(12, 75))  # random age equals amount of circles
list = []  # list contains coordinates of circles


def setup():
    colorMode(HSB, 360, 100, 100)
    size(1200, 600)
    background(0,0,0)
    noStroke()
    smooth()

    for i in range(age): #
        # random values für coordinates x & y and value für the radius
        x1 = int(random(0, width))
        y1 = int(random(0, height))
        r = random(10, 90)  # radius of the circles
        # store generated values in array called list
        list.append([x1, y1, r])

        for j in range(0, len(list)):
            radius = random(20, 80)
            ellipse(list[j][0], list[j][1], list[j][2], list[j][2])
            
    filter(BLUR,30)
    filter(THRESHOLD,0.3)
    
    save("img/test.jpg")

print(age)

