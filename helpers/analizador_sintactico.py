from antlr4 import CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from ExprParser import ExprParser


class ErroresSintacticos(ErrorListener):

    def __init__(self):
        self.lista = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):

        self.lista.append({
            "linea": line,
            "columna": column + 1,   # ANTLR reporta 0-indexed; +1 para que coincida con el editor
            "mensaje": msg
        })


class AnalizadorSintactico:

    def __init__(self):

        self.parser = None
        self.arbol = None
        self.errores = ErroresSintacticos()

    def analizar(self, tokens):

        self.parser = ExprParser(tokens)

        self.parser.removeErrorListeners()
        self.parser.addErrorListener(self.errores)

        self.arbol = self.parser.root()

    def obtener_arbol(self):

        return self.arbol.toStringTree(recog=self.parser)

    def obtener_errores(self):

        return self.errores.lista

    def es_correcto(self):
        # Útil para mostrar en Streamlit "El código es correcto" cuando no hay errores
        return len(self.errores.lista) == 0