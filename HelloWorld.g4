// Definir uma gramática para o programa "Hello, World!"
grammar HelloWorld;

// Define a regra de entrada principal para o programa
program : printStatement;

// Define a regra para a instrução print (simplificada)
printStatement : 'print' '(' STRING ')' ;

// Define uma regra para strings (simplificada)
STRING : '"' .*? '"' ; // Captura uma string entre aspas duplas

// Ignora espaços em branco (espaços, tabs, novas linhas) entre tokens
WS : [ \t\r\n]+ -> skip ;
