import json
import subprocess
from flask import Flask

app = Flask(__name__)

dictCliCluster = {}
dictDeuCluster = {}

def init_cache_cli():
    with open("clicluster.csv", "rU") as fd:
        for line in fd:
            if line:
                output=str(line).replace("\n","").replace('\\r','').replace('b\'','').replace('\'','')
                datos=dict(zip(campos, output.split(",")))
                dictCliCluster[datos['rut']]=datos['cluster']
    #print(dictCliCluster.keys())

def init_cache_deu():
    with open("deucluster.csv", "rU") as fd:
        for line in fd:
            if line:
                output=str(line).replace("\n","").replace('\\r','').replace('b\'','').replace('\'','')
                datos=dict(zip(campos, output.split(",")))
                dictDeuCluster[datos['rut']]=datos['cluster']

def get_cluster(rut, tipo):
    if tipo == 'cliente':
        if rut in dictCliCluster:
            lista_paso=[rut,dictCliCluster[rut]]
        else:
            lista_paso=[rut,'C']
    if tipo == 'deudor':
        if rut in dictDeuCluster:
            lista_paso=[rut,dictDeuCluster[rut]]
        else:
            lista_paso=[rut,'C']
    datos = dict(zip(campos, lista_paso))
    str_ret = json.dumps(datos)+'\n'

    return str_ret

@app.route('/')
def hello_world():
    return 'Hello World\n'

@app.route('/api/v0/cliente/qry_cluster/<rut>')
def cliente_qry_cluster(rut):
    return get_cluster(rut,"cliente")

@app.route('/api/v0/deudor/qry_cluster/<rut>')
def deudor_qry_cluster(rut):
    return get_cluster(rut,"deudor")

if __name__ == '__main__':
    campos = ['rut','cluster']
    init_cache_cli()
    init_cache_deu()
    print(dictCliCluster.keys())
    print(dictDeuCluster.keys())
    app.run(host='0.0.0.0', port='5000')
