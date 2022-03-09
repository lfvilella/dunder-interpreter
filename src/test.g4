grammar test;

@header {
package testInterpreter.parser;
}

progr   : (line EOL)+
        ;
line    : read          #lineRead
        | write         #lineWrite
        | atr           #lineAtr
        | ifstm         #lineIfStm
        ; 
read    : READ VAR
        ;
write   : WRITE STR     #writeStr
        | WRITE expr    #writeExpr
        ;
atr     : VAR '=' expr
        ;
ifstm   : IF '('boolExpr')' block 
        | IF '('boolExpr')' block ELSE block
        ;
expr    : term '+' expr 
        | term '-' expr
        ;
term    : fact '*' term 
        | fact '/' term 
        | fact '%' term
        ;
fact    : VAR 
        | NUM 
        | '('expr')' 
        ;
boolExpr: fact 
        | '!'boolExpr 
        | fact relop fact 
        | TRUE 
        | FALSE
        ;
relop   : '>' 
        | '<' 
        | '==' 
        | '>=' 
        | '<=' 
        | '!='
        ;
block   : line  
        | '{' progr '}'
        ;

TRUE        : 'true';
FALSE       : 'false';
READ        : 'read';
WRITE       : 'write';
IF          : 'if';
ELSE        : 'else';
GR          : '>'; 
LS          : '<'; 
EQ          : '=='; 
GRT         : '>=';
LST         : '<='; 
NEQ         : '!=';
ATR         : '=';
OEX         : '(';
CEX         : ')';
OBL         : '{';
CBL         : '}';
NOT         : '!'|'NOT';
ADD         : '+';
SUB         : '-';
MUL         : '*';
DIV         : '/';
MOD         : '%';
EOL         : ';';
STR         : '"'(~["\\\r\n])*'"';
NUM         : [+-]?[0-9]+('.'[0-9]+)?;
VAR         : [a-zA-Z][a-zA-Z0-9_]*;
COMMENT     : '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
WS          : [ \t\r\n]+ -> skip;