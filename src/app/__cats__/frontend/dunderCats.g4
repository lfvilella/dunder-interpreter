grammar dunderCats;

program
   : statement +
   ;

statement
   : 'function' function statement
   | 'if' paren_expr statement
   | 'if' paren_expr statement 'else' statement
   | 'while' paren_expr statement
   | 'do' statement 'while' paren_expr ';'  /* TODO: remove it */
   | '{' statement* '}'
   | expr ';'
   | 'printf' paren_expr ';'
   | ';'
   ;

function
   : id_ '(' params ')'
   ;

params
   : STRING +  // should be like (a, b, c), think a regex to it
   ;

paren_expr
   : '(' expr ')'
   ;

expr
   : test
   | id_ '=' expr
   ;

test
   : sum_
   | sum_ '<' sum_
   ;

sum_
   : term
   | sum_ '+' term
   | sum_ '-' term
   ;

term
   : id_
   | integer
   | paren_expr
   ;

id_
   : '__' STRING '__'
   ;

integer
   : INT
   ;


STRING
   : [a-z]+
   ;


INT
   : [0-9] +
   ;

WS
   : [ \r\n\t] -> skip
   ;
