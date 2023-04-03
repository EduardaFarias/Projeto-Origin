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
  digitalWrite(13, HIGH); // O pino 13 possui sinal alto, apresen-
  //tando 5v eletricamente
  delay(1000); // passa 1 segundo ligado
  digitalWrite(13, LOW); // Sina
  delay(1000);
  digitalWrite(13, HIGH);
  delay(2000); 
  digitalWrite(13, LOW);
  delay(1000);
  digitalWrite(13, HIGH);
  delay(5000); 
  digitalWrite(13, LOW);
  delay(1000);
}