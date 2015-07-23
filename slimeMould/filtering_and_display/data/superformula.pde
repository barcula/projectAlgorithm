add_library 'json'

int num = 60;
int colorL=255, k = 0, j=100, i=200;

float x, y, z;
float r, th=0, step=.1, epi=200;
float m = 1, n1=-1, n2=0, n3=0;
float b=1, a=1;
int counter1=0, counter2=0;



void setup() 
{
  size(900, 450);
  background(0);
  frameRate(50);
  smooth();
  
  json.load('/Users/enjoi/GitHub/input-output/slimeMould/superformula/Output.json')
}

void draw() 
{

  fill(0, 5);
  rect(-5, -5, 1250, 510);
  counter1++;
  if (counter1 == 50) {
    m= 40;
    n1= 1;
    n2=random(3, 8);
    //n3=random(6.);
    epi= 150;
    step=2;
    counter1 = 0;
  }
  translate(width/2, height/2);
  stroke(colorL, 35);
  noFill();
  beginShape();
  for (int i=1; i < num; i++) {
    r = epi*pow(((pow(abs(cos(m*th/4)/a), n2))+(pow(abs(sin(m*th/4)/b), n3))), (-1/n1)); 
    th = th + step;
    x = r*cos(th);
    y = r*sin(th);
    curveVertex(x, y);
  }
  endShape();
}

void mousePressed() {
  background(0);
}

