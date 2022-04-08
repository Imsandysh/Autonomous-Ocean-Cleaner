
int portMotorIN1 = 12;
int portMotorIN2 = 11;
int portMotorENA = 5;


int starBoardMotorIN1 = 9;
int starBoardMotorIN2 = 8;
int starBoardMotorENA = 4;

//int speed = 255;






void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(portMotorIN1,OUTPUT);
  pinMode(portMotorIN2,OUTPUT);
  pinMode(portMotorENA,OUTPUT);

  pinMode(starBoardMotorIN1,OUTPUT);
  pinMode(starBoardMotorIN1,OUTPUT);
  pinMode(starBoardMotorENA,OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

  delay(5000);
  turnRight(254,254);

  delay(5000);
  turnLeft(254,254);

  delay(5000);
  forward(254,254);

  delay(5000);
  back(254,254);

  delay(5000);
  stop();
  
  

}


void forward(int speedStar, int speedPort){
  Serial.println("turn Left");
  digitalWrite(starBoardMotorIN1,HIGH);
  digitalWrite(starBoardMotorIN2,LOW);

  digitalWrite(portMotorIN1,LOW);
  digitalWrite(portMotorIN2,HIGH);

  analogWrite(starBoardMotorENA, speedStar);
  analogWrite(portMotorENA, speedPort);
}

void back(int speedStar, int speedPort){
  Serial.println("turn Right");
  digitalWrite(starBoardMotorIN1,LOW);
  digitalWrite(starBoardMotorIN2,HIGH);

  digitalWrite(portMotorIN1,HIGH);
  digitalWrite(portMotorIN2,LOW);

  analogWrite(starBoardMotorENA, speedStar);
  analogWrite(portMotorENA, speedPort);
}

void turnRight(int speedStar, int speedPort){
  Serial.println("forwards");
  digitalWrite(starBoardMotorIN1,LOW);
  digitalWrite(starBoardMotorIN2,HIGH);

  digitalWrite(portMotorIN1,LOW);
  digitalWrite(portMotorIN2,HIGH);

  analogWrite(starBoardMotorENA, speedStar);
  analogWrite(portMotorENA, speedPort);
}


void turnLeft(int speedStar, int speedPort){
  Serial.println("back");
  digitalWrite(starBoardMotorIN1,HIGH);
  digitalWrite(starBoardMotorIN2,LOW);

  digitalWrite(portMotorIN1,HIGH);
  digitalWrite(portMotorIN2,LOW);

  analogWrite(starBoardMotorENA, speedStar);
  analogWrite(portMotorENA, speedPort);
}

void stop(){

  analogWrite(starBoardMotorENA, 0);
  analogWrite(portMotorENA, 0);
}
