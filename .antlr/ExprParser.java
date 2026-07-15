// Generated from c:/Users/joseb/Music/proyecto_profecional/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ExprParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		VAR=1, LET=2, CONST=3, FUNCTION=4, ASYNC=5, AWAIT=6, IMPORT=7, EXPORT=8, 
		CLASS=9, EXTENDS=10, CONSTRUCTOR=11, THIS=12, SUPER=13, NEW=14, STATIC=15, 
		IF=16, ELSE=17, FOR=18, WHILE=19, DO=20, SWITCH=21, CASE=22, DEFAULT=23, 
		BREAK=24, CONTINUE=25, RETURN=26, TRY=27, CATCH=28, FINALLY=29, THROW=30, 
		TRUE=31, FALSE=32, NULL=33, ARROW=34, ASSIGN_ADD=35, ASSIGN_SUB=36, ASSIGN_MUL=37, 
		ASSIGN_DIV=38, ASSIGN_MOD=39, ASIG=40, INC=41, DEC=42, MAS=43, MENOS=44, 
		MULT=45, DIV=46, MOD=47, STRICT_EQ=48, STRICT_NE=49, EQU=50, NEQ=51, BE=52, 
		LE=53, BIG=54, LESS=55, OPTIONAL_CHAIN=56, NULLISH=57, AND=58, OR=59, 
		NOT=60, ELLIPSIS=61, PI=62, PD=63, LI=64, LD=65, CI=66, CD=67, PC=68, 
		C=69, P=70, DP=71, Q=72, NUM=73, CADENA=74, ID=75, WS=76, LINE_COMMENT=77, 
		BLOCK_COMMENT=78;
	public static final int
		RULE_root = 0, RULE_expr = 1;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'var'", "'let'", "'const'", "'function'", "'async'", "'await'", 
			"'import'", "'export'", "'class'", "'extends'", "'constructor'", "'this'", 
			"'super'", "'new'", "'static'", "'if'", "'else'", "'for'", "'while'", 
			"'do'", "'switch'", "'case'", "'default'", "'break'", "'continue'", "'return'", 
			"'try'", "'catch'", "'finally'", "'throw'", "'true'", "'false'", "'null'", 
			"'=>'", "'+='", "'-='", "'*='", "'/='", "'%='", "'='", "'++'", "'--'", 
			"'+'", "'-'", "'*'", "'/'", "'%'", "'==='", "'!=='", "'=='", "'!='", 
			"'>='", "'<='", "'>'", "'<'", "'?.'", "'??'", "'&&'", "'||'", "'!'", 
			"'...'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "','", "'.'", 
			"':'", "'?'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "VAR", "LET", "CONST", "FUNCTION", "ASYNC", "AWAIT", "IMPORT", 
			"EXPORT", "CLASS", "EXTENDS", "CONSTRUCTOR", "THIS", "SUPER", "NEW", 
			"STATIC", "IF", "ELSE", "FOR", "WHILE", "DO", "SWITCH", "CASE", "DEFAULT", 
			"BREAK", "CONTINUE", "RETURN", "TRY", "CATCH", "FINALLY", "THROW", "TRUE", 
			"FALSE", "NULL", "ARROW", "ASSIGN_ADD", "ASSIGN_SUB", "ASSIGN_MUL", "ASSIGN_DIV", 
			"ASSIGN_MOD", "ASIG", "INC", "DEC", "MAS", "MENOS", "MULT", "DIV", "MOD", 
			"STRICT_EQ", "STRICT_NE", "EQU", "NEQ", "BE", "LE", "BIG", "LESS", "OPTIONAL_CHAIN", 
			"NULLISH", "AND", "OR", "NOT", "ELLIPSIS", "PI", "PD", "LI", "LD", "CI", 
			"CD", "PC", "C", "P", "DP", "Q", "NUM", "CADENA", "ID", "WS", "LINE_COMMENT", 
			"BLOCK_COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Expr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ExprParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RootContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode EOF() { return getToken(ExprParser.EOF, 0); }
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(4);
			expr();
			setState(5);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(ExprParser.ID, 0); }
		public TerminalNode ASIG() { return getToken(ExprParser.ASIG, 0); }
		public TerminalNode NUM() { return getToken(ExprParser.NUM, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(7);
			match(ID);
			setState(8);
			match(ASIG);
			setState(9);
			match(NUM);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001N\f\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0000\u0000\u0002\u0000\u0002\u0000\u0000\t\u0000\u0004"+
		"\u0001\u0000\u0000\u0000\u0002\u0007\u0001\u0000\u0000\u0000\u0004\u0005"+
		"\u0003\u0002\u0001\u0000\u0005\u0006\u0005\u0000\u0000\u0001\u0006\u0001"+
		"\u0001\u0000\u0000\u0000\u0007\b\u0005K\u0000\u0000\b\t\u0005(\u0000\u0000"+
		"\t\n\u0005I\u0000\u0000\n\u0003\u0001\u0000\u0000\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}