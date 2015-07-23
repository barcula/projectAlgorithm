import json
 
num = 60;
colorL=255 
k = 0
j=100
i=200
 
th=0
step=.1
epi=200
m = 1
n1=-1
n2=0
n3=0
b=1
a=1
counter1=0
json_data = []
 
 
 
def setup():
  global json_data
  size(1600, 720)
  background(0)
  frameRate(100)
  smooth()
    
  with open("/Users/enjoi/GitHub/input-output/slimeMould/superformula/Output.json") as json_file:
    json_data = json.load(json_file)
    print(json_data)
 
 
def draw():
    global counter1
    global json_data
    global epi
    global m
    global th
    global n2
    global n1
    global step
    global n3
    fill(0, 5);
    
        
    if counter1 == 755:
        counter1 = 0
 
    rect(-5, -5, 2000, 1500)
    smooth()
    strokeWeight(2)
    counter1 += 1;
    print(counter1)
    print(json_data[counter1])
    m= 8;
    n1= 20;
    n2= 10
    n3=json_data[counter1] * 0.0001 
    epi= 40
    step=100

    translate(width/2, height/2)
    stroke(colorL, 35)
    noFill()
    beginShape()
    i = 1
    for i in range(num):
        r = epi*pow(((pow(abs(cos(m*th/4)/a), n2))+(pow(abs(sin(m*th/4)/b), n3))), (-1/n1))
        th = th + step
        x = r*cos(th)
        y = r*sin(th)
        curveVertex(x, y)
    
    endShape()
