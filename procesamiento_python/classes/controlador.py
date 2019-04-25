'''
@author: Monkey Coders
@version: 1

Este prototipo en Python con estandar MVC, filtra y procesa los datos para poder ser exportado a otras plataformas.

Condiciones:
2010 - Actualidad
'''
class ControladorDatos:

    def controlador_poblacion_2010(self, database, datos):
        entidades_federativas = []
        poblacion = []
        for elemento in datos:
            entidades_federativas.append(elemento[0])
            poblacion.append({'2010':elemento[1]})
        print("[✔] datos del 2010 procesados")
        database.insertar_entidades_poblacion_2010(entidades_federativas, poblacion)

    # Obteno los resultados calculado desde el 2010 hasta el 2017 poblacion_2011 = poblacion_2010 + natalidad_2011 - mortalidad_2011 
    def controlador_poblacion_2010_2017(self, database, poblacion_2010, natalidad_2010_2017, mortalidad_2010_2017):
        lista_poblacion_2010 = []
        no_lista_poblacion = []
        lista_final = []
        for elemento_2010 in poblacion_2010:
            lista_final.append({"2010": elemento_2010[1]})
            lista_poblacion_2010.append(elemento_2010[1])
        for contador_ano in range(2011, 2018):
            entidad_federativa = 0
            for natalidad, mortalidad in zip(natalidad_2010_2017, mortalidad_2010_2017): 
                poblacion = int(lista_poblacion_2010[entidad_federativa]) + int(natalidad[str(contador_ano)]) - int(mortalidad[str(contador_ano)])       
                no_lista_poblacion.append({str(contador_ano):str(poblacion)})
                lista_poblacion_2010[entidad_federativa] = str(poblacion)
                entidad_federativa += 1
        for x in range(0, 32):
            lista_final[x] = {**lista_final[x], **no_lista_poblacion[x],**no_lista_poblacion[x+32], **no_lista_poblacion[x+64], **no_lista_poblacion[x+96], **no_lista_poblacion[x+128], **no_lista_poblacion[x+160], **no_lista_poblacion[x+192]}
        print("[✔] Calculos matematicos para obtener la poblacion hasta el 2017 Pt = Pi + Nt - Mt")
        database.insertar_poblacion_2010_2017(lista_final)

    def controlador_poblacion_2018_2019(self,database, poblacion_total):
        poblacion_2018_ordenada = []
        poblacion_2019_ordenada = []
        poblacion_2018_2019 = []
        contador_entidad = 1
        for x in range(0, 32):
            poblacion_2018_ordenada.append(0)
            poblacion_2019_ordenada.append(0)
        for x in range(1, (219*32)):
            poblacion_2018_ordenada[contador_entidad-1] += int(poblacion_total[0][x].replace("\n", ""))
            poblacion_2019_ordenada[contador_entidad-1] += int(poblacion_total[1][x].replace("\n", ""))
            if x == ((219*contador_entidad)+(contador_entidad-1)):
                contador_entidad += 1
        for x in range(0, 32):
            poblacion_2018_2019.append({"2018": poblacion_2018_ordenada[x], "2019": poblacion_2019_ordenada[x]})
        print("[✔] Procesamiento de +500.000 de datos para obtener las aproximaciones del 2018 y 2019")
        database.insertar_poblacion_2018_2019(poblacion_2018_2019)

    def controlador_patentes_2010_2018(self, database, patentes_2010_2018):
        patentes_2010_2018_final = []
        for x in range(0, 32):
            ultimo_valor = patentes_2010_2018[x][9].replace("\n", "")
            patentes_2010_2018_final.append({"2010": patentes_2010_2018[x][1], "2011": patentes_2010_2018[x][2], "2012": patentes_2010_2018[x][3], "2013": patentes_2010_2018[x][4], "2014": patentes_2010_2018[x][5], "2015":patentes_2010_2018[x][6], "2016": patentes_2010_2018[x][7], "2017": patentes_2010_2018[x][8], "2018": ultimo_valor})
        print("[✔] Procesamiento de las patentes 2010 hasta el 2018")
        database.insertar_patentes_2010_2018(patentes_2010_2018_final)

    def controlador_unidades_economicas_2013_2018(self, database, unidades_economicas_2013_2018):
        unidades_economicas_2013_2018_final = []
        for x in range(0, 32):
            for y in range(0, 7):      
                unidades_economicas_2013_2018[x][y] = unidades_economicas_2013_2018[x][y].replace(",","")         
                unidades_economicas_2013_2018[x][y] = unidades_economicas_2013_2018[x][y].replace('"',"")
                unidades_economicas_2013_2018[x][y] = unidades_economicas_2013_2018[x][y].replace('\n',"")
            unidades_economicas_2013_2018_final.append({"2013": unidades_economicas_2013_2018[x][1], "2014": unidades_economicas_2013_2018[x][2], "2015": unidades_economicas_2013_2018[x][3], "2016":unidades_economicas_2013_2018[x][4], "2017": unidades_economicas_2013_2018[x][5], "2018":unidades_economicas_2013_2018[x][6]})
        print("[✔] Procesamiento de las unidades economicas del 2013 hasta el 2018")
        database.insertar_unidades_economicas_2013_2018(unidades_economicas_2013_2018_final)

    def controlador_turistas_2010_2018(self, database, turistas_2010_2018):
        turistas_2010_2018_final = []
        for x in range(0, 32):
            for y in range(0, 10):
                turistas_2010_2018[x][y] = turistas_2010_2018[x][y].replace(",","")         
                turistas_2010_2018[x][y] = turistas_2010_2018[x][y].replace('"',"")
                turistas_2010_2018[x][y] = turistas_2010_2018[x][y].replace('\n',"")
            turistas_2010_2018_final.append({"2010": turistas_2010_2018[x][1], "2011": turistas_2010_2018[x][2], "2012": turistas_2010_2018[x][3],"2013": turistas_2010_2018[x][4],"2014": turistas_2010_2018[x][5],"2015": turistas_2010_2018[x][6], "2016": turistas_2010_2018[x][7],"20107": turistas_2010_2018[x][8],"2018": turistas_2010_2018[x][9]})
        print("[✔] Procesamiento de los turitas por entidad federativa del 2010 hasta el 2018")
        database.insertar_turistas_2010_2018(turistas_2010_2018_final)

    def controlador_pib_mexico_1993_2018(self, database, pib_mexico_1993_2018):
        pib_mexico_2010_2018 = []
        pib_mexico_1993_2018_final = []
        pib_mexico_1993_2018 = pib_mexico_1993_2018[1:len(pib_mexico_1993_2018)]
        for x in range(0, 26):
            pib = 0 #valor inicial
            for y in range(0, 4):
                if x >= 17:
                    pib += float(pib_mexico_1993_2018[y][x])
            if pib != 0:
                pib_mexico_2010_2018.append(pib)
                pib = 0
        for x in range(2010, 2019):
            pib_mexico_1993_2018_final.append({str(x):pib_mexico_2010_2018[x-2010]})
        print("[✔] Procesamiento del pib total en mexico desde 1993 hasta el 2018")
        database.insertar_pib_mexico_2010_2018(pib_mexico_1993_2018_final)

    def controlador_poblacion_mexico_2010_2019(self, database, poblacion_2010, natalidad_2011_2017, mortalidad_2011_2017, poblacion_2018_2019):
        poblacion_mexico_2010_2018 = []
        poblacion_2018_ordenada = []
        poblacion_2019_ordenada = []
        poblacion_2018_2019_final = []
        lista_poblacion_2010 = []
        no_lista_poblacion = []
        lista_final = []
        contador_entidad = 1
        # POBLACION 2018 - 2019
        for x in range(0, 32):
            poblacion_2018_ordenada.append(0)
            poblacion_2019_ordenada.append(0)
        for x in range(1, (219*32)):
            poblacion_2018_ordenada[contador_entidad-1] += int(poblacion_2018_2019[0][x].replace("\n", ""))
            poblacion_2019_ordenada[contador_entidad-1] += int(poblacion_2018_2019[1][x].replace("\n", ""))
            if x == ((219*contador_entidad)+(contador_entidad-1)):
                contador_entidad += 1
        for x in range(0, 32):
            poblacion_2018_2019_final.append({"2018": poblacion_2018_ordenada[x], "2019": poblacion_2019_ordenada[x]})
        # POBLACION 2010 - 2017
        for elemento_2010 in poblacion_2010:
            lista_final.append({"2010": elemento_2010[1]})
            lista_poblacion_2010.append(elemento_2010[1])
        for contador_ano in range(2011, 2018):
            entidad_federativa = 0
            for natalidad, mortalidad in zip(natalidad_2011_2017, mortalidad_2011_2017): 
                poblacion = int(lista_poblacion_2010[entidad_federativa]) + int(natalidad[str(contador_ano)]) - int(mortalidad[str(contador_ano)])       
                no_lista_poblacion.append({str(contador_ano):str(poblacion)})
                lista_poblacion_2010[entidad_federativa] = str(poblacion)
                entidad_federativa += 1
        for x in range(0, 32):
            lista_final[x] = {**lista_final[x], **no_lista_poblacion[x],**no_lista_poblacion[x+32], **no_lista_poblacion[x+64], **no_lista_poblacion[x+96], **no_lista_poblacion[x+128], **no_lista_poblacion[x+160], **no_lista_poblacion[x+192]}
        
        # CALCULO DE LA POBLACION TOTAL.
        for x in range(0, 32):
            lista_final[x] = {**lista_final[x], **poblacion_2018_2019_final[x]}
        
        for x in range(2010, 2020):
            sumatoria = 0
            for y in range(0, 32):
                sumatoria += int(lista_final[y][str(x)]) 
            if x != 2010:
                poblacion_mexico_2010_2018.append({str(x):str(sumatoria-1640000)})
            else:
                poblacion_mexico_2010_2018.append({str(x):str(sumatoria)})

        print("[✔] Procesamiento de la poblacion total de Mexico 2010 - 2018")
        database.insertar_poblacion_mexico_2010_2018(poblacion_mexico_2010_2018)

    def controlador_exportaciones_entidades_2010_2018(self, database, exportaciones_entidades_2010_2018):
        exportaciones_entidades_2010_2018_lista = []
        exportaciones_entidades_2010_2018_final = []

        for entidad in exportaciones_entidades_2010_2018:
            exportaciones_entidades_2010_2018_lista.append(entidad[1:len(entidad)])

        for entidad in exportaciones_entidades_2010_2018_lista:
            contador = 0
            contador_anual = 2011
            valores_anual = {"2010": str(int(entidad[0])+int(entidad[1])+int(entidad[2])+int(entidad[3])) }
            for x in range(0, 36):
                if contador == 4:
                    valor = {str(contador_anual):str(int(entidad[x])+int(entidad[x+1]) + int(entidad[x+2])+int(entidad[x+3]))}
                    valores_anual = {**valores_anual, **valor}
                    contador = 0
                    contador_anual += 1
                contador += 1
            exportaciones_entidades_2010_2018_final.append(valores_anual)
            
        print("[✔] Procesamiento de las exportaciones en entidades federativas del 2010 hasta el 2018")
        database.insertar_exportaciones_entidades_2010_2018(exportaciones_entidades_2010_2018_final)

    def controlador_promedio_actividad_trimestral_2010_2017(self,database, promedio_actividad_trimestral_2010_2017):
        promedio_actividad_trimestral_2010_2017_final = []
        for actividad in promedio_actividad_trimestral_2010_2017:
            contador = 0
            contador_anual = 2011
            valores_anual = {"2010": str((float(actividad[0])+float(actividad[1])+float(actividad[2])+float(actividad[3]))/4)}

            for x in range(0, 32):
                if contador == 4:
                    valor = {str(contador_anual):str((float(actividad[x])+float(actividad[x+1]) + float(actividad[x+2])+ float(actividad[x+3]))/4 )}
                    valores_anual = {**valores_anual, **valor}
                    contador = 0
                    contador_anual += 1
                contador += 1
            promedio_actividad_trimestral_2010_2017_final.append(valores_anual)

        print("[✔] Procesamiento del promedio en el crecimiento de la actividad economicas en entidades federativas del 2010 hasta el 2018")
        database.insertar_promedio_actividad_trimestral_2010_2017(promedio_actividad_trimestral_2010_2017_final)
    
    def controlador_actividades_economicas_entidades_2010_2017(self, database, actividades_economicas_entidades_2010_2017):
        valores_por_entidad = []
        for x in range(0, 32):
            actividades_economicas_entidades = []
            for array_actividad in actividades_economicas_entidades_2010_2017[x]:
                valores = {
                    array_actividad[0]: {
                        "2010": array_actividad[8],
                        "2011": array_actividad[9],
                        "2012": array_actividad[10],
                        "2013": array_actividad[11],
                        "2014": array_actividad[12],
                        "2015": array_actividad[13],
                        "2016": array_actividad[14],
                        "2017": array_actividad[15]
                    }
                }
                actividades_economicas_entidades.append(valores)
            valores_por_entidad.append(actividades_economicas_entidades)
        print("[✔] Procesamiento de las actividades economicas por entidad federativa 2010 - 2017")
        database.insertar_actividades_economicas_entidades_2010_2017(valores_por_entidad)

    def controlador_consumo_electrico_municipios_2010_2017(self, database, consumo_electrico_2010_2017):
        nombre_municipios = [] #LISTO
        consumo_municipio = [] #DEV
        for municipio in consumo_electrico_2010_2017:

            if municipio.find("Total Estatal") == -1:
                municipio = municipio.replace(" ","") 
                municipio_coma = municipio.split(",")
                municipio_separacion = municipio.split(',"')
                
                if len(municipio_separacion) == 9:
                    nombre_municipios.append(municipio_coma[4])

                    for i, municipio in enumerate(municipio_separacion):
                        data = municipio.replace(",", "")
                        data = data.replace('"',"")
                        data = data.replace("\n","")
                        municipio_separacion[i] = data
                
                    municipio_separacion = municipio_separacion[1:len(municipio_separacion)]

                    anual = 2010
                    valores_anuales = {}
                    for x in range(0, 8):
                        valor = {str(anual):str(municipio_separacion[x])}
                        valores_anuales = {**valores_anuales, **valor}
                        anual += 1

                    consumo_municipio.append(valores_anuales)
  
        print("[✔] Procesamiento del consumo electrico con municipios 2010 - 2017")
        database.insertar_consumo_electrico_municipios_2010_2017(nombre_municipios, consumo_municipio)