'''
@author: Monkey Coders
@version: 1

Este prototipo en Python con estandar MVC, filtra y procesa los datos para poder ser exportado a otras plataformas.

Condiciones:
2010 - Actualidad
'''
from classes.conexionDB import ConexionDB
from classes.csvScanner import CsvScanner
from classes.controlador import ControladorDatos

if __name__ == "__main__":
    #Contenedores de informacion
    poblacion_2010 = []
    natalidad_2010_2017 = []
    mortalidad_2010_2017 = []
    poblacion_2018_2019 = []
    patentes_2010_2018 = []
    unidades_economicas_2013_2018 = []
    turistas_2010_2018 = []
    pib_mexico_1993_2018 = []
    pib_entidades_2010_2017 = []
    promedio_actividad_trimestral_2010_2017 = [] #PROMEDIO
    exportaciones_entidades_2010_2018 = []