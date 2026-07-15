# Generated from ./Expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,78,12,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,0,2,
        0,2,0,0,9,0,4,1,0,0,0,2,7,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,
        0,0,0,7,8,5,75,0,0,8,9,5,40,0,0,9,10,5,73,0,0,10,3,1,0,0,0,0
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'let'", "'const'", "'function'", 
                     "'async'", "'await'", "'import'", "'export'", "'class'", 
                     "'extends'", "'constructor'", "'this'", "'super'", 
                     "'new'", "'static'", "'if'", "'else'", "'for'", "'while'", 
                     "'do'", "'switch'", "'case'", "'default'", "'break'", 
                     "'continue'", "'return'", "'try'", "'catch'", "'finally'", 
                     "'throw'", "'true'", "'false'", "'null'", "'=>'", "'+='", 
                     "'-='", "'*='", "'/='", "'%='", "'='", "'++'", "'--'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'==='", "'!=='", 
                     "'=='", "'!='", "'>='", "'<='", "'>'", "'<'", "'?.'", 
                     "'??'", "'&&'", "'||'", "'!'", "'...'", "'('", "')'", 
                     "'{'", "'}'", "'['", "']'", "';'", "','", "'.'", "':'", 
                     "'?'" ]

    symbolicNames = [ "<INVALID>", "VAR", "LET", "CONST", "FUNCTION", "ASYNC", 
                      "AWAIT", "IMPORT", "EXPORT", "CLASS", "EXTENDS", "CONSTRUCTOR", 
                      "THIS", "SUPER", "NEW", "STATIC", "IF", "ELSE", "FOR", 
                      "WHILE", "DO", "SWITCH", "CASE", "DEFAULT", "BREAK", 
                      "CONTINUE", "RETURN", "TRY", "CATCH", "FINALLY", "THROW", 
                      "TRUE", "FALSE", "NULL", "ARROW", "ASSIGN_ADD", "ASSIGN_SUB", 
                      "ASSIGN_MUL", "ASSIGN_DIV", "ASSIGN_MOD", "ASIG", 
                      "INC", "DEC", "MAS", "MENOS", "MULT", "DIV", "MOD", 
                      "STRICT_EQ", "STRICT_NE", "EQU", "NEQ", "BE", "LE", 
                      "BIG", "LESS", "OPTIONAL_CHAIN", "NULLISH", "AND", 
                      "OR", "NOT", "ELLIPSIS", "PI", "PD", "LI", "LD", "CI", 
                      "CD", "PC", "C", "P", "DP", "Q", "NUM", "CADENA", 
                      "ID", "WS", "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_root = 0
    RULE_expr = 1

    ruleNames =  [ "root", "expr" ]

    EOF = Token.EOF
    VAR=1
    LET=2
    CONST=3
    FUNCTION=4
    ASYNC=5
    AWAIT=6
    IMPORT=7
    EXPORT=8
    CLASS=9
    EXTENDS=10
    CONSTRUCTOR=11
    THIS=12
    SUPER=13
    NEW=14
    STATIC=15
    IF=16
    ELSE=17
    FOR=18
    WHILE=19
    DO=20
    SWITCH=21
    CASE=22
    DEFAULT=23
    BREAK=24
    CONTINUE=25
    RETURN=26
    TRY=27
    CATCH=28
    FINALLY=29
    THROW=30
    TRUE=31
    FALSE=32
    NULL=33
    ARROW=34
    ASSIGN_ADD=35
    ASSIGN_SUB=36
    ASSIGN_MUL=37
    ASSIGN_DIV=38
    ASSIGN_MOD=39
    ASIG=40
    INC=41
    DEC=42
    MAS=43
    MENOS=44
    MULT=45
    DIV=46
    MOD=47
    STRICT_EQ=48
    STRICT_NE=49
    EQU=50
    NEQ=51
    BE=52
    LE=53
    BIG=54
    LESS=55
    OPTIONAL_CHAIN=56
    NULLISH=57
    AND=58
    OR=59
    NOT=60
    ELLIPSIS=61
    PI=62
    PD=63
    LI=64
    LD=65
    CI=66
    CD=67
    PC=68
    C=69
    P=70
    DP=71
    Q=72
    NUM=73
    CADENA=74
    ID=75
    WS=76
    LINE_COMMENT=77
    BLOCK_COMMENT=78

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_root




    def root(self):

        localctx = ExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.expr()
            self.state = 5
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def ASIG(self):
            return self.getToken(ExprParser.ASIG, 0)

        def NUM(self):
            return self.getToken(ExprParser.NUM, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7
            self.match(ExprParser.ID)
            self.state = 8
            self.match(ExprParser.ASIG)
            self.state = 9
            self.match(ExprParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





