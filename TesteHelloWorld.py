from antlr4 import *
from antlr4.Token import CommonToken
from antlr4.tree.Trees import Trees
from HelloWorldLexer import HelloWorldLexer
from HelloWorldParser import HelloWorldParser
from HelloWorldListener import HelloWorldListener
import networkx as nx
import matplotlib.pyplot as plt

class PrintHelloWorldListener(HelloWorldListener):
    def enterPrintStatement(self, ctx):
        print("Detetado um comando Hello World!")

def plot_parse_tree(parser, tree):
    def add_edges(graph, node, tokens):
        for child in Trees.getChildren(node):
            if child is not None:
                token = child.getPayload()
                if isinstance(token, CommonToken):
                    text = tokens[token.tokenIndex]
                else:
                    text = str(token)
                graph.add_node(text)
                graph.add_edge(str(node.getPayload()), text)
                add_edges(graph, child, tokens)

    graph = nx.DiGraph()
    tokens = [token.text for token in parser.getTokenStream().tokens]
    add_edges(graph, tree, tokens)

    # Usa spring_layout em vez de graphviz_layout
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, arrows=False)
    plt.show()

def main():
    input_string = 'print("Hello, World!")'
    input_stream = InputStream(input_string)
    lexer = HelloWorldLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = HelloWorldParser(stream)
    tree = parser.program()
    printer = PrintHelloWorldListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    plot_parse_tree(parser, tree)

if __name__ == '__main__':
    main()
