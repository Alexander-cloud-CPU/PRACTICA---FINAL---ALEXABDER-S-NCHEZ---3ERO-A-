from flask import Blueprint, jsonify, abort , request, render_template, redirect, url_for, flash
from controls.practica.hospitalControl import HospitalControl
from controls.practica.hospitalGrafo import HospitalGrafo
from flask_cors import CORS
router = Blueprint('router', __name__)


@router.route('/') #SON GETS
def home_grafo():
    return render_template('index.html')


#---------------------------------------------------------------------------------#
#LISTA HOSPITALES
@router.route('/hospitales')
def lista_hospitales():
    hc = HospitalControl()  
    list = hc._list()
    return render_template('practica/lista.html', lista=hc.to_dict_lista(list))

#VER
@router.route('/hospitales/agregar')
def ver_hospital():
    return render_template('practica/guardar.html')

#GUARDAR
@router.route('/hospitales/guardar', methods=["POST"])
def guardar_hospital():
    hc = HospitalControl()
    data = request.form
    if not "nombre" in data.keys():
        abort(400)
        
    #TODO ...Validar
    hc._hospital._nombre = data["nombre"]
    hc._hospital._direccion = data["direccion"]
    hc._hospital._horario = data["horario"]
    hc._hospital._latitud= data["latitud"]
    hc._hospital._longitud = data["longitud"]
    hc.save
    return redirect("/hospitales", code=302)

@router.route('/grafo')
def grafo():
    return render_template('d3/grafo.html')


@router.route('/hospitales/grafo_hospital')
def grafo_hospital():
    hcg = HospitalGrafo()
    hc = HospitalControl()
    hcg.create_graph()
    return render_template('d3/grafo.html' , lista = hc.to_dict())



@router.route('/hospitales/grafo_ver_admin')
def grafo_ver_admin():
    hc = HospitalControl()
    grafo = HospitalGrafo()._grafo
    
    arrayHospitales = hc.to_dict()
    matriz_ady = []

    for i in range(len(arrayHospitales)):
        fila = ["-----"] * len(arrayHospitales)
        matriz_ady.append(fila)
        
    for i in range(len(arrayHospitales)):
        for j in range(len(arrayHospitales)):
            if grafo.exist_edge_E(arrayHospitales[i]["nombre"], arrayHospitales[j]["nombre"]):
                matriz_ady[i][j] = grafo.weight_edges_E(arrayHospitales[i]["nombre"], arrayHospitales[j]["nombre"])
    
    return render_template("practica/grafo.html",  lista = hc.to_dict(), matris = matriz_ady)



@router.route('/hospitales/crear_adyacencias', methods=["POST"])
def crear_adyacencias():
    hc = HospitalControl()
    grafo = HospitalGrafo()._grafo
    data = request.form
    origen = data["origen"]
    destino = data["destino"]
    
    if origen == destino:
        flash('Por favor, selecione un destino y origen distintos', 'error')
        return redirect(url_for('router.grafo_ver_admin'))
    

    if grafo.exits_edges(int(origen)-1, int(destino)-1):
        flash('Ya existe una adyacehcia entre estos dos hospital', 'error')
    else:
        hospitalOrigen = hc._list().binary_search_models(int(origen), "_id")
        hospitalDestino = hc._list().binary_search_models(int(destino), "_id")
        hc = HospitalGrafo()
        hc.create_graph(hospitalOrigen, hospitalDestino)
    
    return redirect("/hospitales/grafo_ver_admin", code=302)


@router.route('/hospitales/camino_mas_corto', methods=["POST"])
def camino_mas_corto():
    hc = HospitalControl()
    grafo = HospitalGrafo()._grafo
    data = request.form
    origen = data["origen"]
    destino = data["destino"]
    metodo = data["metodo"]
    
    if origen == destino:
        flash('Por favor, seleccione un destino y origen distintos', 'error')
        return redirect(url_for('router.grafo_ver_admin'))
    
    hospitalOrigen = hc._list().binary_search_models(int(origen), "_id")
    hospitalDestino = hc._list().binary_search_models(int(destino), "_id")
    
    # Aquí debe haber lógica para calcular el camino más corto usando Floyd o Dijkstra
    # Por ejemplo:
    if metodo == '1':  # Floyd
        resultado, distancia = grafo.floyd_warshall(int(origen)-1, int(destino)-1) 
    elif metodo == '2':  # Dijkstra
        resultado, distancia = grafo.dijkstra(int(origen)-1)
    distancia = distancia[int(origen)-1][int(destino)-1]
    # Formatear resultado para pasar al template
    resultado_formateado = {
        'origen': hospitalOrigen._nombre,
        'destino': hospitalDestino._nombre,
        'distancia': distancia,  # Este es un valor de ejemplo
        'ruta': resultado # Este es un valor de ejemplo
    }
    hc._list().print
    hc.to_dict()
    lista = hc.to_dict()
    for i in range(len(lista)):
        print(lista[i])
    

    return render_template("d3/grafo.html", lista=hc.to_dict(), resultado=resultado_formateado)


