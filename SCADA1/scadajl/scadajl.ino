int orden;
const int  analogInPin = A0;
int sensorNivel;
int led13;
int led12; 
void setup()
{
  Serial.begin(9600);
  pinMode(13,OUTPUT);
  pinMode(12,OUTPUT);
  pinMode(2,INPUT);
  pinMode(4,INPUT);
}
void loop() 
{ 
  if (Serial.available())
  {
    orden=Serial.read();
    
    if (orden=='H')
    {
     digitalWrite(13,HIGH);
    }
    if (orden=='L')
    { 
     digitalWrite(13,LOW);
    }
    if (orden=='A')
    {
     digitalWrite(12,HIGH);
    }
    if (orden=='B')
    { 
     digitalWrite(12,LOW);
    }
    if (orden=='N')
    {
    sensorNivel = analogRead ( analogInPin );
    led13=digitalRead(13);
    led12=digitalRead(12);
    Serial.println ("["+String(led13)+","+String(led12)+","+String(sensorNivel)+"]"); //Serial.println ("{"+"'E_led13':"String(led13)+","+"'E_led12':"String(led12)+","+"'E_nivel':"String(sensorNivel)+"}");
    }  
  }
  else
  {
  if (digitalRead(2)==HIGH&&digitalRead(13)==LOW)
    {
      digitalWrite(13,HIGH);
      delay(200);
    }
  if (digitalRead(2)==HIGH&&digitalRead(13)==HIGH)
    {
      digitalWrite(13,LOW);
      delay(200);  
    }
  if (digitalRead(4)==HIGH&&digitalRead(12)==LOW)
    {
      digitalWrite(12,HIGH);
      delay(200);
    }
  if (digitalRead(4)==HIGH&&digitalRead(12)==HIGH)
    {
      digitalWrite(12,LOW);
      delay(200);
    }
  }
  //orden=0;
}
  
