"""
Hello world multi language.

 Dependendo da lingua configurada no ambiente o programa exibe a 
 mensagem correspondente.

 como usar:

 tenha a variavel LANG devidamente configurada ex:
   
       export LANG=pt_BR

       execuçao

        .\app.py

"""
__version__ ="0.0.1"
__author__ = "Italo Lima"
__license__ = "unlicense"

#dunder
 
import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language =="pt_BR":
    msg ="Olá.Mundo!"

elif current_language == "it_IT":
    msg = "Ciao, mondo!"

elif current_language == "es_SP":
    msg = "hola, mundo"

elif current_language == "fr_FR":
    msg = "Bonjour Monde"

print (msg)



