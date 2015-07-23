"""
Simple empty sketch
"""

# add the needed libs
add_library('video')
add_library('opencv_processing')
import json

# declare the global variables we need
video = None
opencv = None
points = []
brightPixels = []
frameCounty = 0

# setup is run once
def setup():
#     make sure processing knows we are
#     using the global objects
    global video
    global opencv
    global frameCounty
    textAlign(LEFT)
#     create a new Video object from our video
    video = Movie(this, "slimeEmma.mp4")
    video.frameRate(5)
#     create a new opencv object
#     in the size of the video
    opencv = OpenCV(this, 798, 710)
#     setup size of the sketch
    size(798, 710)
#     now loop and play the video
    video.play()
#     we love hsb
    colorMode(HSB, 360, 100, 100, 100)
    background(0, 0, 100)
    print "End of def setup():"
    
    frameCounty = 0

# now our loop
def draw():
    
    global frameCounty
    global video
    
    video.speed(0.2)
    
    if (video.available()):
        video.read()
    
    count = 0
    frameCounty = frameCounty +1

    ##### CAPTURE #####
#     load the current frame into opencv
    opencv.loadImage(video)
    ##### FILTER #####
    # get a snapshot for displaying the filtered images
    opencv.gray()  # make it grayscale
    grey_image = opencv.getSnapshot()
    opencv.contrast(0.5)  # raise contrast
    contrast_image = opencv.getSnapshot()
    opencv.threshold(50)  # clip all below 240
    threshold_image = opencv.getSnapshot()
    
    for x in range(threshold_image.width):
        for y in range(threshold_image.height):
            if threshold_image.get(x,y) != -16777216:
                count += 1
    brightPixels.append(count)
    print count
    
    image(threshold_image, video.width / 1000, video.height / 1000,
          threshold_image.width, threshold_image.height)
    
    if video.time() == video.duration():
        with open ("/Users/enjoi/GitHub/input-output/slimeMould/filtering_and_display/^Output.txt", "w") as text_file:
            print 'success'
            text_file.write(json.dumps(brightPixels))
            print "Frame Count: " + str(frameCounty)
            exit()
        
        


