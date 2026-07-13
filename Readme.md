# Instrucciones de instlacion mediante consola

## Paso 1: Activar anviente de python
```
python -m venv .venv
```
```
.\.venv\Scripts\Activate.ps1
```

Si genera un error, utilizar el siguiente script 
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
## Paso 2: Instalar dependencias 
Debera ubircar el archivo requirements.txt y ejecutar los siguientes comandos

```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

## Paso 3: Ejecutar aplicacion
Para probar el programa ejecute el siguiente comando
```
streamlit run app.py
```

## paso 4: desactivar entorno
Como buenas practicas de informatica, recuerde desactivar el entorno antes de cerrar la consola 
```
deactivate
```