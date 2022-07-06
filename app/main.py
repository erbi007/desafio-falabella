from typing import Union
from fastapi import FastAPI
import string

app = FastAPI()

def get_dic_patentes():
    patentes = {}
    alphabeto = list(string.ascii_uppercase)
    identificador = 0

    for letra in alphabeto:
        for i in range(1, 1001):
            if identificador <= 1000:
                if len(str(i)) == 1:
                    patentes[i] = str(letra+letra+letra+letra)+str('00'+str(i-1))
                elif len(str(i)) == 2:
                    patentes[i] = str(letra+letra+letra+letra)+str('0'+str(i-1))
                elif len(str(i)) >= 3:
                    patentes[i] = str(letra+letra+letra+letra)+str(i-1)
            else:
                if len(str(i)) == 1:
                    patentes[identificador + i] = str(letra+letra+letra+letra)+str('00'+str(i-1))
                elif len(str(i)) == 2:
                    patentes[identificador + i] = str(letra+letra+letra+letra)+str('0'+str(i-1))
                elif len(str(i)) >= 3:
                    patentes[identificador + i] = str(letra+letra+letra+letra)+str(i-1)
        
            identificador = identificador + 1000

    print(patentes)
    return patentes


@app.get("/")
def read_root():
    return {"Tes API": "OK"}


@app.get("/patente/{param_patente}")
def read_patente(param_patente: str):

    diccionario = get_dic_patentes()
    jsonPatente = {}

    if str(param_patente).isdigit() == True:

        for clave, valor in diccionario.items():
            if clave == int(param_patente):
                jsonPatente['patente'] = valor
    else:
        for clave, valor in diccionario.items():
            if valor == param_patente:
                jsonPatente['patente_id'] = clave

    return jsonPatente
