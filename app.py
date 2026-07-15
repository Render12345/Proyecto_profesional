import streamlit as st
from helpers.archivo import Archivo
from helpers.analizador_lexico import AnalizadorLexico
from helpers.analizador_sintactico import AnalizadorSintactico
 

class App:

    def __init__(self):
        st.set_page_config(page_title="Analizador Lexico", layout="wide")
        self.analizador = AnalizadorLexico()
        self.sintactico = AnalizadorSintactico()

    def ejecutar(self):
        st.title("Analizador Lexico con ANTLR y Streamlit")
        st.write(f"Sube un archivo {Archivo.imprime_extenciones()} para ver tokens y errores lexicos.")

        archivo_subido = st.file_uploader(
            "Selecciona tu archivo",
            type=Archivo.get_extenciones())

        if archivo_subido is None:
            st.info(f"Primero sube un archivo {Archivo.imprime_extenciones()}")
            return

        archivo = Archivo(archivo_subido)

        if not archivo.es_extencion_valida():
            st.error("El archivo debe ser .txt")
            return

        codigo = archivo.leer()
        info = archivo.obtener_info()

        st.subheader("Informacion del archivo")
        st.write("Nombre:", info["nombre"])
        st.write("Extension:", info["extension"])

        st.subheader("Codigo original")
        st.code(codigo, language="text")

        self.analizador.analizar(codigo)

        tokens = self.analizador.obtener_tokens()
        errores = self.analizador.obtener_errores()

        
        if len(tokens) == 0:
            st.warning("No se encontraron tokens")
            return
           

        if len(errores) == 0:
            st.success("No hay errores lexicos")
        else:
            st.subheader("Errores lexicos")
            st.dataframe(errores, use_container_width=True)
            return

        st.subheader("Tokens")
        st.dataframe(tokens, use_container_width=True)

        stream_tokens = self.analizador.obtener_lista_tokens()

        self.sintactico.analizar(stream_tokens)

        errores_sintacticos = self.sintactico.obtener_errores()


        if len(errores_sintacticos) == 0:
            st.success("No hay errores sintacticos")
        else:
            st.subheader("Errores sintacticos")
            st.dataframe(errores_sintacticos, use_container_width=True)
            return
        
        arbol = self.sintactico.obtener_arbol()

        st.subheader("Arbol sintactico")
        st.code(arbol)




if __name__ == "__main__":
    app = App()
    app.ejecutar()