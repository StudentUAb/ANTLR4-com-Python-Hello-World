<h1 align="center">
    <img width="600" src="three.png" />
</h1>


<p align="center">
ANTLR com Python

# TESTE com ANTLR e Python
    

</p>

📌 ANTLR com Python: Hello World e Visualização da Árvore de Análise
------------------
Este guia descreve como criar, analisar e visualizar uma árvore de análise para uma gramática simples de "Hello World" utilizando ANTLR para gerar os analisadores e Python para executar a análise e a visualização.

Este guia passo a passo descreve como criar uma simples gramática Hello World usando ANTLR, gerar o analisador em Python, e visualizar a árvore de análise sintática utilizando networkx e matplotlib.



## Pré-requisitos

- Java (para executar o ANTLR).
- ANTLR4 (baixe `antlr-4.x-complete.jar` do [site oficial do ANTLR](https://www.antlr.org/)).
- Python 3.
- Bibliotecas Python: `antlr4-python3-runtime`, `networkx`, `matplotlib`.

## Passo a Passo

### 1. Criar a Gramática ANTLR

Defina a gramática no arquivo `HelloWorld.g4`:

```antlr
grammar HelloWorld;

program : printStatement;

printStatement : 'print' '(' STRING ')' ;

STRING : '"' .*? '"' ;

WS : [ \t\r\n]+ -> skip ;
 
## Sintaxe para executar:

<pre>docker compose up -d </pre>

Demo: [http://server.ivo.com.pt:8082](http://server.ivo.com.pt:8082)

Video: [https://youtu.be/Dbs-P95D0Q4](https://youtu.be/wdyRhklgEso)

O projeto foi feito em Html, Javasript e Css


The project was done with Html, Javascript and Css


<img src="print.png" alt="page-home">


🔧 Tecnologias utilizadas:
------------------

- html
- Javascript (biblioteca three.js)
- Css

💬 Fale comigo
------------------
[*Entre em contato comigo*](https://www.linkedin.com/in/ivo-baptista-3712144/)

