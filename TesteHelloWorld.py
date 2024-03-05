# Importamos bibliotecas para o projeto
from antlr4 import *
# Importamos o CommonToken para acessar o tokenIndex do token printStatement que é 1 e o token print que é 0 
from antlr4.Token import CommonToken
# Importamos o Trees para acessar os filhos do token printStatement que é o token STRING que é 2 
from antlr4.tree.Trees import Trees
# Importamos as classes HelloWorldLexer, HelloWorldParser e HelloWorldListener
from HelloWorldLexer import HelloWorldLexer
from HelloWorldParser import HelloWorldParser
from HelloWorldListener import HelloWorldListener
# Importamos as bibliotecas para criar o grafo e plotar o grafo
import networkx as nx
import matplotlib.pyplot as plt

# Criamos a classe PrintHelloWorldListener que herda de HelloWorldListener
class PrintHelloWorldListener(HelloWorldListener):
    # Criamos o método enterPrintStatement que será executado quando o parser detectar o comando Hello World!
    def enterPrintStatement(self, ctx):
        print("Detetado um comando Hello World!")
# Criamos a classe HelloWorldParser que herda de HelloWorldParser
def plot_parse_tree(parser, tree):
    # Criamos o método add_edges que será executado quando o parser detectar o comando Hello World!
    def add_edges(graph, node, tokens):
        for child in Trees.getChildren(node): 
            if child is not None: # ignore empty nodes
                token = child.getPayload() # getPayload() retorna o token STRING que é 2
                if isinstance(token, CommonToken): # CommonToken é a classe que contém o tokenIndex do token printStatement que é 1 e o token print que é 0
                    text = tokens[token.tokenIndex] # tokens[token.tokenIndex] retorna o token printStatement que é 1 e o token print que é 0
                    text = str(token) # str(token) é o token STRING que é 2
                graph.add_node(text) # Adiciona o nó text ao grafo
                graph.add_edge(str(node.getPayload()), text) # Adiciona o nó text ao grafo
                add_edges(graph, child, tokens) # Adiciona os nós filhos ao grafo
                
    graph = nx.DiGraph() # Cria o grafo
    tokens = [token.text for token in parser.getTokenStream().tokens] # Cria a lista de tokens
    add_edges(graph, tree, tokens) # Adiciona os nós ao grafo

    # Usa spring_layout em vez de graphviz_layout
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, arrows=False) # Desenha o grafo
    plt.show() # Mostra o grafo

# Criamos a classe main que será executada quando o programa for executado
def main():
    input_string = 'print("Hello, World!")' # Criamos a string que será analisada
    input_stream = InputStream(input_string) # Criamos o input_stream que será analisado
    lexer = HelloWorldLexer(input_stream) # Criamos o lexer que será analisado
    stream = CommonTokenStream(lexer) # Criamos o stream que será analisado
    parser = HelloWorldParser(stream) # Criamos o parser que será analisado
    tree = parser.program() # Criamos o tree que será analisado
    printer = PrintHelloWorldListener() # Criamos o printer que será analisado 
    walker = ParseTreeWalker() # Criamos o walker que será analisado
    walker.walk(printer, tree) # Criamos o walker que será analisado 
    plot_parse_tree(parser, tree) # Criamos o plot_parse_tree que será analisado

if __name__ == '__main__':
    main() # Executa a função main
