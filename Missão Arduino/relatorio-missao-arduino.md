# Relatório da Missão 1.0 (Missão Arduino)

O presente relatório é referente à primeira missão do projeto Origin. O objetivo da missão é ascender um LED com arduino, fazendo o LED piscar com três períodos de tempo diferentes.

## Materiais Utilizados: 
- 1 Protoboard (Placa de ensaio pequena)
- 1 LED na cor azul
- 1 Resistor com resistência de 220V
- Uma placa Arduino Uno R3
- Fios condutores

## Descrição dos procedimentos:
Após consumir os conteúdos disponibilizados e alguns materiais a mais foram iniciadas as etapas do projeto

### Primeira etapa:
A primeira etapa consiste na montagem da parte fisíca do circuito

- **Primeiro Passo**: Selecionar uma placa Arduino Uno R3, o arduino é uma plataforma de prototipagem eletrônica, a placa é o hardware que vamos usar para construir nossos projetos e o Arduino IDE é o software onde vou escrever o que a placa deve fazer(nesse caso, fazer o LED piscar em períodos de tempo diferentes), para programar na IDE Arduino podemos escrever o código em c++.

- **Segundo Passo**: Selecionar uma placa protoboard pequena. Uma protoboard é uma placa com diversos furos e conexões condutoras verticais e horizontais para a montagem de circuitos elétricos.

- **Terceiro Passo**: Selecionar um resitor com resistência de 220ohm (equivalente a 220 Volts/Ampére), limitando o fluxo de cargas elétricas

- **Quarto Passo**: Posicionando o resistor nos furos g3 e e3

- **Quinto Passo**: Foi selecionado um LED  na cor azul, esse led foi posicionado nos furos b2 e b3, com o posicionamento de respectivamente seu catodo e anodo,  o anodo junto ao terminal do resistor

- **Sexto Passo**: Vamos usar fios condutores na cor preta para a trilha de furos como negativa e conectar ao pino de energia GND, esse pino GND é a porta que dá acesso ao terra da placa, então o resistor está ligado ao pino GND.

- **Sétimo Passo**: Vamos usar fios condutores na cor vermelha para a trilha de furos como positiva e conectar ao pino 13(porta digital que serve para entradas e saídas), o LED está ligado a este pino.

## Segunda Etapa 

Com o circuito montado vamos à parte do código, antes disso algumas considerações. A linguagem C para arduino precisa de duas funções:
- **Função setUp()**: Serve para definir o pino de entrada e o pino de saída, portanto é executada apenas uma vez
- **Função loop()**: Repete em Loop infinito os comandos que estão dentro da função

Agora sim, vamos aos comentários do código:

- Na função setUp() temos a função **pinMode(13, OUTPUT)**, essa função está configurando o pino 13 como saída

- Na função **loop()** temos os comandos 
    - digitalWrite(13, HIGH): Eletricamente esse comando faz com que o pino 13 apresente uma fonte de tensão de 5v, em outras palavras faz o LED ascender.
    - delay(1000): Esse comando faz com que o led permaneça em algum modo 1000 milissegundos, ou, melhor dizendo 1 segundo
    - digitalWrite(13, LOW): Eletricamente esse comando faz com que o pino 13 apresente uma fonte de tensão de Ov, em outras palavras faz o LED apagar.
 
 Assim o comportamento do código é:

 **1 -** LED ascende por 1000 milissegundos(1 segundo)

 **2 -** LED permance apagada por 1000 milissegundos(1 segundo)

 **3 -** LED ascende por 2000 milissegundos(2 segundos)

 **4 -** LED permance apagada por 1000 milissegundos(1 segundo)

 **5 -** LED ascende por 5000 milissegundos(5 segundos)

 **6 -** LED permance apagada por 1000 milissegundos(1 segundo)


## Conclusão

Dessa forma concluimos que o programa com Arduino fez piscar com sucesso um LED piscar com 3 períodos de tempo diferentes.


<p align="center"> Maria Eduarda Batista de Farias</p>
<p align="center"> 05/04/2023</p>
