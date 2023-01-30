void setup() {
  size(900,700);
}

float xi = 200;
float yi = 350;

float vel = 0;
float acc = 1;
float ang = 0;

int r = 100;
float startx = xi + r + 50;

void draw() {
  background(212);
  
  ang -= 0.01;
  float x = cos(ang)*r + xi;
  float y = sin(ang)*r + yi;
  
  strokeWeight(3);
  noFill();
  circle(xi,yi,r*2);
  
  fill(255);
  
  circle(xi,yi,5);
  line(xi-r,yi,xi+r,yi);
  line(xi,yi+r,xi,yi-r);
  
  circle(x,y,20);
  circle(startx,y,10);
  startx += 0.5;
  
  strokeWeight(1);
  line(x,y,startx,y);
}
