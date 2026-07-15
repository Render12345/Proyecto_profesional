grammar Expr;

// ==========================================
// RAÍZ: secuencia de expresiones separadas por ;
// ==========================================
root : expr (PC expr)* PC? EOF ;

// ==========================================
// EXPR — PATRÓN INDIRECTO/AUTO-RECURSIVO
// expr : expr OP expr | ATOMO
// ==========================================
expr
    // Bloques { ... }
    : LI (expr (PC expr)* PC?)? LD                                      # blockExpr

    // Declaración de variables
    | variableModifier ID (ASIG expr)? (C ID (ASIG expr)?)*              # variableDecl

    // Funciones declaradas
    | ASYNC? FUNCTION ID PI paramList? PD LI (expr (PC expr)* PC?)? LD   # functionDecl

    // Funciones flecha
    | ASYNC? arrowParams ARROW expr                                     # arrowFunction

    // Clases
    | CLASS ID (EXTENDS expr)? LI classMember* LD                       # classDecl

    // Estructuras de control
    | IF PI expr PD expr (ELSE expr)?                                   # ifExpr
    | WHILE PI expr PD expr                                             # whileExpr
    | DO expr WHILE PI expr PD                                          # doWhileExpr
    | FOR PI (variableModifier ID | ID) IN expr PD expr                 # forInExpr
    | FOR PI (variableModifier ID | ID) OF expr PD expr                 # forOfExpr
    | FOR PI forInit? PC expr? PC forUpdate? PD expr                    # forExpr
    | SWITCH PI expr PD LI caseClause* defaultClause? caseClause* LD    # switchExpr
    | TRY expr (CATCH (PI ID PD)? expr)? (FINALLY expr)?                # tryExpr
    | WITH PI expr PD expr                                              # withExpr
    | DEBUGGER                                                          # debuggerExpr

    // Saltos de control
    | THROW expr                                                        # throwExpr
    | RETURN expr?                                                      # returnExpr
    | BREAK                                                             # breakExpr
    | CONTINUE                                                          # continueExpr

    // Módulos
    | IMPORT (ID | LI ID (C ID)* LD) FROM CADENA                        # importExpr
    | EXPORT DEFAULT? expr (AS ID)?                                     # exportExpr

    // Acceso a miembros / índices / llamadas / optional chaining
    | expr P ID                                                         # memberAccess
    | expr CI expr CD                                                   # indexAccess
    | expr OPTIONAL_CHAIN (ID | PI argumentList? PD | CI expr CD)       # optionalChainExpr
    | expr PI argumentList? PD                                          # callExpr
    | NEW expr                                                          # newExpr

    // Incremento / decremento
    | expr (INC | DEC)                                                  # postIncDec
    | <assoc=right> (INC | DEC) expr                                    # preIncDec

    // Unarios (incluye los de palabra clave)
    | <assoc=right> (NOT | MENOS | MAS | TYPEOF | VOID | DELETE) expr   # unaryExpr
    | <assoc=right> AWAIT expr                                         # awaitExpr

    // Exponenciación (mayor precedencia que * / %, asociativa a la derecha)
    | <assoc=right> expr EXP expr                                       # exponentExpr

    // Aritméticos
    | expr (MULT | DIV | MOD) expr                                      # multiplicative
    | expr (MAS | MENOS) expr                                           # additive

    // Relacionales (incluye instanceof / in)
    | expr (LESS | BIG | LE | BE | INSTANCEOF | IN) expr                # relational

    // Igualdad
    | expr (EQU | NEQ | STRICT_EQ | STRICT_NE) expr                     # equality

    // Lógicos
    | expr AND expr                                                     # logicalAnd
    | expr OR expr                                                      # logicalOr
    | expr NULLISH expr                                                 # nullishExpr

    // Ternario
    | <assoc=right> expr Q expr DP expr                                 # conditionalExpr

    // Asignación (incluye **=)
    | <assoc=right> expr assignmentOperator expr                        # assignmentExpr

    // Primarios / literales
    | primaryExpr                                                       # primaryS
    ;

// ==========================================
// REGLAS DE APOYO
// ==========================================
variableModifier   : VAR | LET | CONST ;
assignmentOperator : ASIG | ASSIGN_ADD | ASSIGN_SUB | ASSIGN_MUL | ASSIGN_DIV | ASSIGN_MOD | ASSIGN_EXP ;

arrowParams : ID
            | PI (param (C param)*)? PD
            ;
paramList   : param (C param)* ;
param       : ELLIPSIS? ID (ASIG expr)? ;

classMember      : STATIC? methodDefinition | STATIC? fieldDefinition ;
methodDefinition : ASYNC? propertyName PI paramList? PD LI (expr (PC expr)* PC?)? LD ;
fieldDefinition  : propertyName (ASIG expr)? ;
propertyName     : ID | CADENA | NUM | CONSTRUCTOR ;

caseClause    : CASE expr DP (expr PC?)* ;
defaultClause : DEFAULT DP (expr PC?)* ;

forInit   : variableModifier ID (ASIG expr)? (C ID (ASIG expr)?)* | expr ;
forUpdate : expr (C expr)* ;

argumentList : argument (C argument)* ;
argument     : ELLIPSIS? expr ;

primaryExpr
    : THIS
    | SUPER
    | ID
    | literal
    | arrayLiteral
    | objectLiteral
    | PI expr PD
    ;

literal : NUM | CADENA | TRUE | FALSE | NULL ;

arrayLiteral : CI elementList? CD ;
elementList  : elementItem (C elementItem)* ;
elementItem  : ELLIPSIS? expr ;

objectLiteral : LI propertyList? LD ;
propertyList  : property (C property)* ;
property
    : propertyName DP expr
    | ELLIPSIS expr
    | ID
    ;

// ==========================================
// PALABRAS RESERVADAS (LÉXICO)
// ==========================================
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

// --- Nuevas palabras reservadas ---
TYPEOF:'typeof';
INSTANCEOF:'instanceof';
DELETE:'delete';
VOID:'void';
IN:'in';
WITH:'with';
ENUM:'enum';
DEBUGGER:'debugger';
FROM:'from';
AS:'as';
OF:'of';

// ==========================================
// OPERADORES
// ==========================================

ARROW:'=>';
ASSIGN_ADD:'+=';
ASSIGN_SUB:'-=';
ASSIGN_MUL:'*=';
ASSIGN_DIV:'/=';
ASSIGN_MOD:'%=';
ASSIGN_EXP:'**=';   // nuevo (antes de EXP y ASIG por longest-match)
ASIG:'=';


INC:'++';
DEC:'--';

EXP:'**';           // nuevo (antes de MULT por longest-match)
MAS:'+';
MENOS:'-';
MULT:'*';
DIV:'/';
MOD:'%';


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
NUM : [0-9]+ 'n'                                        // BigInt entero
    | [0-9]+ ('.' [0-9]+)? ([eE] [+-]? [0-9]+)?
    | '.' [0-9]+ ([eE] [+-]? [0-9]+)?
    | '0' [xX] [0-9a-fA-F]+ 'n'?                          // Hex (+ BigInt opcional)
    | '0' [bB] [01]+ 'n'?                                 // Binario (+ BigInt opcional)
    | '0' [oO] [0-7]+ 'n'?                                // Octal (+ BigInt opcional)
    ;


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