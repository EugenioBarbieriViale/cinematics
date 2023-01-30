void setup() {
  size(900,800);
}

float x = 450;
float y = 400;

float vel = 0;
float acc = 1;
float ang = 0;

int r = 200;
float[] positions = new float[10000];
float[] positions1 = new float[10000];

public class Trail {
  public Trail(float x, float y, float ang) {
    float x_ = x;
    float y_ = y;
    float ang_ = ang;
  }
}


void draw() {
  background(212);
  strokeWeight(3);
  circle(x,y,50);
  line(x,30,x,y);
  
  ang += 0.05;
  y = cos(ang)*r + 400;
  
  positions1 = append(positions, y);
  println(positions1);
}
