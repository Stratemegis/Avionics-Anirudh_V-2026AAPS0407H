#include <Adafruit_LiquidCrystal.h>

int wrecked = 0; // 5-seccond timer
int dist = 0;    // Ultrasonic distance sensor reading
int bright = 0;  // Light Sensor reading
int butt = 0;    // Pushbutton input (High/Low)
int anchor = 0;  // Anchored or Nah

long readUltrasonic_time(int triggerPin, int echoPin)
{
  pinMode(triggerPin, OUTPUT);  
  digitalWrite(triggerPin, LOW); //fix as low to begin with
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10); // Sets the trigger pin to HIGH state for 10 microseconds
  digitalWrite(triggerPin, LOW);
  pinMode(echoPin, INPUT);
  // Reads and returns the time for which the echoPin remains HIGH in microseconds
  return pulseIn(echoPin, HIGH);
}

Adafruit_LiquidCrystal lcd_1(0);

void setup()
{
  pinMode(2, INPUT);  //PushButton Input pin
  pinMode(A1, INPUT); //Light Sensor input
  lcd_1.begin(16, 2); 
  pinMode(3, OUTPUT); //Buzzer Output
  pinMode(4, OUTPUT); //LED Output

  while (wrecked != 5) {
    //Initialising Variables
    butt = digitalRead(2);
    dist = 0.01723 * readUltrasonic_time(A0, A0); //converting time in microseconds to distance in cm.
    bright = analogRead(A1);      

    if (digitalRead(2) == HIGH) {
      anchor += 1;      //Increasing 'anchor' by 1 every time the Button is pressed
    }

    if (anchor % 2 == 0) {
      if (bright <= 235 || dist < 100) {  // Range of Analog signal of the Light sensor is 0-471
        wrecked += 1;                     //Either case increases the timer
        if (bright <= 235) {
          if (dist < 100) {
            lcd_1.print("STORM AND CHARYBIDS");
            digitalWrite(3, HIGH);
            digitalWrite(4, HIGH);
          }
          lcd_1.print("STORM");
          digitalWrite(4, HIGH);
        } else {
          lcd_1.print("CHARYBIDS");
          digitalWrite(3, HIGH);
        }
      } else {
        lcd_1.print("OPEN SEA");
        wrecked = 0;
      }
    } else {
      lcd_1.print("ANCHOR DROPPED");
      wrecked = 0;   //Timer resets
    }
    
    delay(1000);
    lcd_1.clear();        //Clearing LCD
    digitalWrite(3, LOW);
    digitalWrite(4, LOW); //Turning off LED and Buzzer
  }
  lcd_1.print("WRECKED"); //Program is in Void Setup() so everything comes to a stop
}

void loop()  //Not Using this :(
{}
