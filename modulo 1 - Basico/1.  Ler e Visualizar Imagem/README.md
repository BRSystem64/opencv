### Leitura e Visualização
São as operações primordiais para ler e visualizar uma imagem através do opencv. 


**Leitura**

Para ler uma imagem, você deve utilizar o método `imread()`. É necessário passar o caminho da imagem como paramêtro, Conforme o código abaixo:
```python
import numpy as np
import cv2 as cv

img = cv.imread("caminho_da_imagem.jpg")
```
Também é possível passar um segundo parametro, indicando qual canal de cor a imagem deverá operar, por exemplo:
```python
img = cv.imread("imagem.jpg", cv.IMREAD_GRAYSCALE) # Imagem carregará em tons de cinza
```
O exemplo acima pode ser encontrado no arquivo `ler_mostrar_imagem_tons_cinza.py`.

Caso tenha executado o seu script usando apenas o método `imread()`, foi possível observar que não apareceu nada em tela. Uma vez que o método `ìmread()` apenas lê a imagem e não realiza amostragem em tela.


**Visualização**

Para visualizarmos a imagem em tela, é necessário utilizar o método `imshow()`, conforme o exemplo abaixo:
```python
...
img = cv.imread("caminho_da_imagem.jpg")

cv.imshow('titulo', img)

cv.waitKey(0)
cv.destroyAllWindows()
```
O método `imshow()` necessita que seja passado dois parametros, o primeiro sendo o título da janela que será criada, e o segundo parametro a imagem que será exibida.

Você deve ter observado que também há dois outros métodos em nosso exemplo, o método `waitKey()` e o método `destroyAllWindows()`. Caso você execute o código acima sem o método `waitKey()`, verá que muito rapidamente a imagem irá aparecer e sumir, uma vez que não foi determinado por quanto tempo o `imshow()` deve apresentar a imagem. O `waitKey()` recebe como parametros um valor interior que representa os milisegundos que deverá esperar até que execute a linha seguinte. Caso o valor passado seja 0, significa que o método irá esperar a interação com algum comando do teclado. Já o método `destroyAllWindows()` irá destruir todas as janelas que o programa tenha criado. O arquivo de exemplo é o `ler_mostrar_imagem.py`.


Há uma outra forma de apresentar uma imagem, utilizando o pyplot do matplotlib. Segue o exemplo abaixo:
```python
...
from matplotlib import pyplot as plt 

img = cv.imread('../img/torre-pisa.jpg')

img = img[:, :, ::-1]

plt.imshow(img)
plt.title('Torre de Pisa')

plt.show()
```
Observe que estamos sobrescrevendo a imagem no `img = img[:, :, ::-1]`, mas qual a razão de fazermos isso?

Por padrão, o opencv utiliza o BGR como estrutura de cores, e o matplotlib utiliza o RGB. Portanto é necessário realizar essa conversão para que seja possível apresentar a imagem. Caso a imagem esteja em escala de cinza, não é necessário realizar a conversão, uma vez que só estará sendo utlizado um canal de cor.

> Para saber mais sobre o tema abordado acima, consulte a documentação do opencv <a href="https://docs.opencv.org/master/dc/d2e/tutorial_py_image_display.html">cliquando aqui</a>.
