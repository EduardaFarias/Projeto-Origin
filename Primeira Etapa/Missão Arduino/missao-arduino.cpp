// C++ code
//
void setup()
{
  // A função setup é executada 1 vez, está configurando o pino
  // 13 como saída
  pinMode(13, OUTPUT);
}

void loop()
{
  digitalWrite(13, HIGH); // Liga o LED
  delay(1000); // LED permanece 1 segundo ligado
  digitalWrite(13, LOW); // LED desligado
  
  delay(1000); // LED 1 segundo desligado
  
  digitalWrite(13, HIGH); 
  delay(2000); // LED 2 segundos ligado
  digitalWrite(13, LOW); 
  
  delay(1000); 
  
  digitalWrite(13, HIGH);
  delay(5000); // LED 5 segundos ligado
  digitalWrite(13, LOW);
  delay(1000);
}