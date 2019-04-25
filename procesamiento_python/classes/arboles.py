'''
@author: Monkey Coders
@version: 1

Este prototipo en Python con estandar MVC, filtra y procesa los datos para poder ser exportado a otras plataformas.

Condiciones:
2010 - Actualidad
'''
class Arboles:
    '''
        Sacar el que tiene mas actividad
        y el que tiene un crecimiento mayor
    '''
    def clasificacion_turismo(self, database):
        sumatorias_totales = {}   
        turismo = database.obtener_turismo()

        for anual in range(2010, 2019):
            sumatoria = 0
            for x in range(0, 32):
                sumatoria += int(turismo[x][0][str(anual)])
            valor = {str(anual):str(sumatoria)}
            sumatorias_totales = {**sumatorias_totales, **valor}
            
        valores_anuales = []
        for anual in range(2010, 2019):
            valores = []
            for x in range(0, 32):
                valor = {str(anual):str(float((int(turismo[x][0][str(anual)])*100)/int(sumatorias_totales[str(anual)])))}
                valores.append(valor)
            valores_anuales.append(valores)
        
        for x in range(0, 32):
            if float(valores_anuales[8][x]["2018"]) >= 6.0:
                database.actualizar_estado_turismo(x,"* Su crecimiento turistico sera alta durante 2019.")
            if float(valores_anuales[8][x]["2018"]) < 6.0 and float(valores_anuales[8][x]["2018"]) > 3.0:
                database.actualizar_estado_turismo(x,"* Su crecimiento turistico estara en la media durante 2019.")
            if float(valores_anuales[8][x]["2018"]) <= 3.0:
                database.actualizar_estado_turismo(x,"* El crecimiento turistico estara muy bajo durante 2019")

        print("[✔] ARBOL DE DECISION: clasificacion de turismo")