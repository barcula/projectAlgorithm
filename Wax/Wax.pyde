age = int(random (12, 75)) #random age equals amount of circles
list = [] #list contains coordinates of circles


def setup():
    size(1200, 600);
    
    for i in range(age):
        #random values für coordinates x & y
        x1 = int(random(0, width))
        y1 = int(random(0, height))
        #store generated values in array called list
        list.append([x1, y1])
        clear()
        

        print(list)
        
            
        
        
    
