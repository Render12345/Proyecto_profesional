from antlr4 import CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from ExprParser import ExprParser


class ErroresSintacticos(ErrorListener):

    def __init__(self):
        self.lista = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):

        self.lista.append({
            "linea": line,
            "columna": column,
            "mensaje": msg
        })


class AnalizadorSintactico:

    def __init__(self):

        self.parser = None
        self.arbol = None
        self.errores = ErroresSintacticos()


    def analizar(self, tokens):

        self.parser = ExprParser(tokens)

        # Quitamos errores normales
        self.parser.removeErrorListeners()

        # Agregamos nuestro listener
        self.parser.addErrorListener(self.errores)

        # Regla inicial
        self.arbol = self.parser.root()


    def obtener_arbol(self):

        return self.arbol.toStringTree(recog=self.parser)



    def obtener_errores(self):

        return self.errores.lista