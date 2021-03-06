grammar logo;

prog
   : (line? EOL)* line
   ;

line
   : cmd+ comment?
   | comment
   | procedureDeclaration
   ;

cmd
   : repeat
   | fd
   | bk
   | rt
   | lt
   | cs
   | pu
   | pd
   | ht
   | st
   | home
   | label
   | setxy
   | make
   | procedureInvocation
   | ife
   | stop
   | fore
   | line_print
   ;

procedureInvocation
   : name expression*
   ;

procedureDeclaration
   : 'to' name parameterDeclarations* EOL? (line? EOL)+ 'end'
   ;

parameterDeclarations
   : ':' name (',' parameterDeclarations)*
   ;

func
   : random
   ;

repeat
   : 'repeat' n=expression block
   ;

block
   : '[' cmd+ ']'
   ;

ife
   : 'if' comparison block
   ;

comparison
   : expression comparisonOperator expression
   ;

comparisonOperator
   : LESS_
   | MORE_
   | EQUAL_
   ;

make
   : 'make' STRINGLITERAL value
   ;

line_print
   : 'print' (value | quotedstring)
   ;

quotedstring
   : '[' (quotedstring |~']')* ']'
   ;

name
   : STRING
   ;

value
   : STRINGLITERAL
   | expression
   | deref
   ;

signExpression
   : ((ADD | SUB))* (number | deref | func)
   ;

multiplyingExpression
   : left=signExpression (op=(MUL | DIV) right=signExpression)*
   ;

expression
   : left=multiplyingExpression (op=(ADD | SUB) right=multiplyingExpression)*
   ;

deref
   : ':' name
   ;

fd
   : ('fd' | 'forward') expression
   ;

bk
   : ('bk' | 'backward') expression
   ;

rt
   : ('rt' | 'right') expression
   ;

lt
   : ('lt' | 'left') expression
   ;

cs
   : 'cs'
   | 'clearscreen'
   ;

pu
   : 'pu'
   | 'penup'
   ;

pd
   : 'pd'
   | 'pendown'
   ;

ht
   : 'ht'
   | 'hideturtle'
   ;

st
   : 'st'
   | 'showturtle'
   ;

home
   : 'home'
   ;

stop
   : 'stop'
   ;

label
   : 'label'
   ;

setxy
   : 'setxy' expression expression
   ;

random
   : 'random' expression
   ;

fore
   : 'for' '[' name from_e=expression to_e=expression step_e=expression ']' block
   ;

number
   : NUMBER
   ;

comment
   : COMMENT
   ;

MUL:'*';
DIV:'/';
ADD:'+';
SUB:'-';

LESS_ : '<';
MORE_ : '>';
EQUAL_ : '=';

STRINGLITERAL
   : '"' STRING
   ;


STRING
   : [a-zA-Z] [a-zA-Z0-9_]*
   ;


NUMBER
   : [0-9]+ ([.][0-9]+)?
   ;


COMMENT
   : ';' ~ [\r\n]*
   ;


EOL
   : '\r'? '\n'
   ;


WS
   : [ \t\r\n] -> skip
   ;