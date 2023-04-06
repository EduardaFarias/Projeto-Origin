# Relatório da Missão 2.0 (Missão OpenCV)
O presente relatório é referente à segunda missão do projeto Origin. O objetivo da missão é abir um arquivo de imagem do disco e exibi-la na tela, após isso caso qualquer tecla seja pressionada a janela com a imagem será fechada e o programa será encerrado.

### Observação importante
O arquivo em python só funciona se tanto o arquivo missao-openCV.py quanto a imagem shooky.png estiverem no diretório global do projeto(ou seja, se esses dois arquivos estiverem no diretório Missão Arduino), caso contrário, ao executar um programa você terá um erro do tipo "can't open/read file: check file path/integrity".

## Recursos utilizados
- Python3
- Biblioteca Numpy
- Biblioteca OpenCV

## Descrição do Procedimento

**1º Passo**: Escolher a imagem que irá ser exibida, no exemplo da apostila é usado um arquivo .jpg mas observando a documentação vi que a biblioteca possui suporte a outros formatos, incluindo .png, talk qual foi usado por mim na missão.

**2º Passo**: A imagem é lida e guardada dentro da varável imagem, uma variável que dará acesso ao objeto da imagem, esse processo é feito através da função imread() importada da biblioteca openCV

**3ºPasso**: São explorados e printados propriedades da imagem:
- Largura em Pixels
- Altura em Pixels
- Quantidade de Canais

Essas características da imagem podem ser observadas através do shape[] da imagem, sendo shape[0] referente à altura da imagem, shape[1] referente à largura da imagem e shape[2] referente a quantidade de canais

**4º Passo**: Exibir na tela a imagem
- Para exibir na tela a imagem, foi usada a função imshow(), importada da biblioteca openCV, recebe como parâmetro o nome que será o título da janela de exbição da imagem e a foto que seŕa exibida

**5º Passo**: Definindo como encerrar a janela de exibição da imagem e o programa .py
- Para isso foi utilizada a função waitKey(), passando o argumento 0 nessa função fica garantido que o programa será encerrado e a foto deixará de ser exibida apenas quando alguma tecla(qualquer tecla) seja pressionada.

**6º Passo**: Salvar a imagem utilizando a função imwrite(), passando como argumento o nome que será colocado na mesma imagem e a imagem na qual será aplicado esse procedimento. Desta forma, no missao-openCV.py a mesma imagem é duplicada e salva com o nome de saida.png

## Conclusão:
Este programa abre uma imagem, mostra suas propiedades de largura e altura em pixels, mostra a quantidade de canais utilizados e exibe a imagem na tela, espera que seja pressionado alguma tecla para fechar a imagem, e por fim a imagem é salva no repositório com o nome de saida.png



<p align="center"> Maria Eduarda Batista de Farias</p>
<p align="center"> 05/04/2023</p>
