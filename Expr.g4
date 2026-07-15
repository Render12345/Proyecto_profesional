grammar Expr;

root : expr EOF;

//expr: expr MENOS expr | NUM;

expr: ID ASIG NUM;



//Palabras reservadas
VAR:'var';
LET:'let';
CONST:'const';
FUNCTION:'function';
ASYNC:'async';
AWAIT:'await';
IMPORT:'import';
EXPORT:'export';

CLASS:'class';
EXTENDS:'extends';
CONSTRUCTOR:'constructor';
THIS:'this';
SUPER:'super';
NEW:'new';
STATIC:'static';

IF:'if';
ELSE:'else';
FOR:'for';
WHILE:'while';
DO:'do';
SWITCH:'switch';
CASE:'case';
DEFAULT:'default';
BREAK:'break';
CONTINUE:'continue';
RETURN:'return';
TRY:'try';
CATCH:'catch';
FINALLY:'finally';
THROW:'throw';

TRUE:'true';
FALSE:'false';
NULL:'null';

// ==========================================
// OPERADORES
// ==========================================
// Asignación y Flechas
ARROW:'=>';
ASSIGN_ADD:'+=';
ASSIGN_SUB:'-=';
ASSIGN_MUL:'*=';
ASSIGN_DIV:'/=';
ASSIGN_MOD:'%=';
ASIG:'=';

// Incremento / Decremento
INC:'++';
DEC:'--';

// Aritméticos
MAS:'+';
MENOS:'-';
MULT:'*';
DIV:'/';
MOD:'%';

// Relacionales y Lógicos
STRICT_EQ:'===';
STRICT_NE:'!==';
EQU:'==';
NEQ:'!=';
BE:'>=';
LE:'<=';
BIG:'>';
LESS:'<';

OPTIONAL_CHAIN:'?.';
NULLISH:'??';
AND:'&&';
OR:'||';
NOT:'!';
ELLIPSIS:'...';

// ==========================================
// DELIMITADORES
// ==========================================
PI:'('; 
PD:')';
LI:'{';
LD:'}';
CI:'[';
CD:']';
PC:';'; 
C:',';
P:'.'; 
DP:':';
Q:'?';

// ==========================================
// LITERALES
// ==========================================

// Números (Decimales, Hexadecimales, Notación científica)
NUM : [0-9]+ ('.' [0-9]+)? ([eE] [+-]? [0-9]+)?
    | '.' [0-9]+ ([eE] [+-]? [0-9]+)?
    | '0' [xX] [0-9a-fA-F]+
    | '0' [bB] [01]+
    | '0' [oO] [0-7]+
    ;

// Cadenas de texto
CADENA : '"' ( '\\' . | ~["\\\r\n] )* '"'
       | '\'' ( '\\' . | ~['\\\r\n] )* '\''
       | '`' ( '\\' . | ~[`\\] )* '`' 
       ;

// ==========================================
// IDENTIFICADORES
// ==========================================
ID : [a-zA-Z_$] [a-zA-Z0-9_$]*;

// ==========================================
// ESPACIOS Y COMENTARIOS
// ==========================================
WS            : [ \t\r\n\u00A0]+ -> skip;
LINE_COMMENT  : '//' ~[\r\n]* -> skip;
BLOCK_COMMENT : '/*' .*? '*/' -> skip;