import json
import math
from py4j.java_gateway import JavaGateway
from flask import Flask

app = Flask(__name__)
gateway = JavaGateway()
query_app = gateway.entry_point

import math

mora_hist = {}
with open("morahistorica.csv", "rU") as fd:
    for line in fd:
        a = str(line).split(",")
        mora = math.floor(float(a[2]))
        rango = math.floor(mora/30)
        discmora = 0
        if mora>0:
            discmora = 1
        mora_hist[(a[0], a[1])] = [ str(mora), str(rango), str(discmora) ]


def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError:
    return False
  return True

@app.route('/')
def hello_world():
    return 'Hello World!\n'

@app.route('/api/v0/documento/qry_falencia/<data>')
def query_modelo(data):
    error_dict= {}
    respuesta = {}
    #return data
    if data:
        if is_json(data):
            data_dict = json.loads(data)
            #return json.dumps(data_dict)+'\n'
            argDifPre               = data_dict["DifPre"]
            argEstDoc               = data_dict["EstDoc"]
            argMora                 = data_dict["Mora"]
            argDiscriminarorMora    = data_dict["DiscriminarorMora"]
            argRMora                = data_dict["RMora"]
            argIvaCom               = data_dict["IvaCom"]
            argMonAnt               = data_dict["MonAnt"]
            argMonDoc               = data_dict["MonDoc"]
            argSalCli               = data_dict["SalCli"]
            argTipDoc               = data_dict["TipDoc"]
            argMGO                  = data_dict["MGO"]
            argCTO                  = data_dict["CTO"]
            argPCO                  = data_dict["PCO"]
            argMAO                  = data_dict["MAO"]
            argTGO                  = data_dict["TGO"]
            argdias                 = data_dict["dias"]
            argClasifCliente        = data_dict["ClasifCliente"]
            argRutCliDeu            = data_dict["RutCliDeu"]
            argClasDeu              = data_dict["ClasDeu"]
            argDisCriminadorCastigo = data_dict["DisCriminadorCastigo"]
            if "RutCli" in data_dict:
                argRutCli = data_dict["RutCli"]
            else:
                error_dict["ErrorCode"] = "3"
                error_dict["ErrorText"] = "RutCli no especificado"
                respuesta["Error"] = error_dict
                return json.dumps(respuesta)+'\n'

            if "RutDeu" in data_dict:
                argRutDeu = data_dict["RutDeu"]
            else:
                error_dict["ErrorCode"] = "4"
                error_dict["ErrorText"] = "RutDeu no especificado"
                respuesta["Error"] = error_dict
                return json.dumps(respuesta)+'\n'

            if (argRutCli, argRutDeu) in mora_hist:
                argMora, argRMora, argDiscriminarorMora = mora_hist[(argRutCli, argRutDeu)]
            else:
                argMora, argRMora, argDiscriminarorMora = ("0","0","0")
            values = query_app.qry_modelo(
                 argDifPre, 
                 argEstDoc,
                 argMora,
                 argDiscriminarorMora,
                 argRMora,
                 argIvaCom,
                 argMonAnt,
                 argMonDoc,
                 argSalCli,
                 argTipDoc,
                 argMGO,
                 argCTO,
                 argPCO,
                 argMAO,
                 argTGO,
                 argdias,
                 argClasifCliente,
                 argRutCliDeu,
                 argClasDeu,
                 argDisCriminadorCastigo,)
            print(values)
            data_resp=values
            #data_resp = "0.5"
            respuesta["Respuesta"] = data_resp
            error_dict["ErrorCode"] = "0"
            error_dict["ErrorText"] = "OK"
        else:
            error_dict["ErrorCode"] = "2"
            error_dict["ErrorText"] = "JSON no valido\n"+data+'\n'
    else:
        error_dict["ErrorCode"] = "1"
        error_dict["ErrorText"] = "Data no valida"
    respuesta["Error"] = error_dict
        
    return json.dumps(respuesta)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5005')
