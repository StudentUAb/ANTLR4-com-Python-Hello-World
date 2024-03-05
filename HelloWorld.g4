grammar HelloWorld;

// Define a regra de entrada principal
program : printStatement;

// Define a regra para a instrução print
printStatement : 'print' '(' STRING ')' ;

// Define uma regra para strings (simplificada)
STRING : '"' .*? '"' ; // Captura uma string entre aspas

// Ignora espaços em branco (espaços, tabs, novas linhas)
WS : [ \t\r\n]+ -> skip ;
