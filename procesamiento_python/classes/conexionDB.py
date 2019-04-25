'''
@author: Monkey Coders
@version: 1

Este prototipo en Python con estandar MVC, filtra y procesa los datos para poder ser exportado a otras plataformas.

Condiciones:
2010 - Actualidad
'''
import psycopg2
import json

class ConexionDB:
    def __init__(self):
        try:
            self.connection = psycopg2.connect("dbname='grupomodelo' user='postgres' host='localhost' password='1298Luis'")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print("[✔] Base de datos conectada")
        except:
            print("[x] Error en la conexion")

    def crear_tablas_postgres(self):
        create_table_command = "CREATE TABLE mexico(id serial PRIMARY KEY, poblacion_total JSON, pib JSON)"
        self.cursor.execute(create_table_command)
        create_table_command = "CREATE TABLE entidad_federativa(id serial PRIMARY KEY, nombre_entidad varchar(100), lat varchar, long varchar, exportaciones JSON, poblacion JSON, patentes JSON, unidades_economicas JSON, turismo JSON, actividad_economica_promedio JSON, actividades_economicas JSON)"
        self.cursor.execute(create_table_command)
        create_table_command = "CREATE TABLE municipios(id serial PRIMARY KEY, lat varchar, long varchar, nombre varchar, consumo_cfe JSON, promedio_total_estatal varchar)"
        self.cursor.execute(create_table_command)
        print("[✔] Tablas de la bse de datos creadas")

    def limpiar_tablas_postgres(self):
        drop_table_command = "DROP TABLE mexico"
        self.cursor.execute(drop_table_command)
        drop_table_command = "DROP TABLE entidad_federativa"
        self.cursor.execute(drop_table_command)
        drop_table_command = "DROP TABLE municipios"
        self.cursor.execute(drop_table_command)
        
        print("[✔] Limpieza en las tablas en la base de datos")

    def insertar_entidades_poblacion_2010(self, entidades, poblacion):
        for i, elemento in enumerate(entidades):
            insert_command = "INSERT INTO entidad_federativa(nombre_entidad, poblacion) VALUES('"+elemento+"', '"+json.dumps(poblacion[i])+"')"
            self.cursor.execute(insert_command)
        print("[✔] Indetidades federativas insertados en la base de datos con su poblacion en 2010")
    
    def insertar_poblacion_2010_2017(self, poblacion):
        for x in range(1,33):
            update_command = "UPDATE entidad_federativa SET poblacion='"+json.dumps(poblacion[x-1])+"' WHERE id="+str(x)
            self.cursor.execute(update_command)
        print("[✔] Poblacion hasta el 2017 insertados en la base de datos")
    
    def insertar_poblacion_2018_2019(self, poblacion):
        self.cursor.execute("SELECT * from entidad_federativa")
        entidades_federativas = self.cursor.fetchall()
        for x in range(1, 33):
            contenacion_datos = {**entidades_federativas[x-1][5], **poblacion[x-1]}
            update_command = "UPDATE entidad_federativa SET poblacion='"+json.dumps(contenacion_datos)+"' WHERE id="+str(x)
            self.cursor.execute(update_command)
        print("[✔] Poblacion del 2018 y 2019 insertados en la base de datos")  

    def insertar_patentes_2010_2018(self, patentes):
        for x in range(1, 33):
            update_command = "UPDATE entidad_federativa SET patentes='"+json.dumps(patentes[x-1])+"' WHERE id="+str(x)
            self.cursor.execute(update_command)
        print("[✔] Patentes 2010 hasta el 2018 insertadas en la base de datos")
    
    def insertar_unidades_economicas_2013_2018(self, unidades_economicas_2013_2018):
        for x in range(1, 33):
            update_command = "UPDATE entidad_federativa SET unidades_economicas='"+json.dumps(unidades_economicas_2013_2018[x-1])+"' where id="+str(x)
            self.cursor.execute(update_command)
        print("[✔] Unidades economicas del 2013 hasta el 2018 insertadas en la base de datos")
    
    def insertar_turistas_2010_2018(self, turistas_2010_2018):
        for x in range(1, 33):
            update_command = "UPDATE entidad_federativa SET turismo='"+json.dumps(turistas_2010_2018[x-1])+"' where id="+str(x)
            self.cursor.execute(update_command)
        print("[✔] Turistas por entidad federativa del 2010 hasta el 2018 insertadas en la base de datos")

    def insertar_pib_mexico_2010_2018(self, pib_mexico_2010_2018):
        insert_command = "INSERT INTO mexico(pib) values('"+json.dumps(pib_mexico_2010_2018)+"')"
        self.cursor.execute(insert_command)
        print("[✔] Pib total de Mexico por año del 2010 hasta el 2018 insertado en la base de datos")

    def insertar_poblacion_mexico_2010_2018(self, poblacion_mexico_2010_2018):
        update_command = "UPDATE mexico SET poblacion_total='"+json.dumps(poblacion_mexico_2010_2018)+"'"
        self.cursor.execute(update_command)
        print("[✔] Poblacion total de Mexico por año del 2010 hasta el 2018 insertado en la base de datos")
    
    def insertar_exportaciones_entidades_2010_2018(self, exportaciones_entidades_2010_2018):
        for x in range(1, 33):
            update_command = "UPDATE entidad_federativa SET exportaciones='"+json.dumps(exportaciones_entidades_2010_2018[x-1])+"' where id="+str(x)
            self.cursor.execute(update_command)
        print("[✔] Exportaciones totales por entidad federativa de 2010 hasta el 2018 insertado en la base de datos")

    def insertar_promedio_actividad_trimestral_2010_2017(self,promedio_actividad_trimestral_2010_2017):
        for x in range(1, 33):
            update_command = "UPDATE entidad_federativa SET actividad_economica_promedio='"+json.dumps(promedio_actividad_trimestral_2010_2017[x-1])+"' where id="+str(x)
            self.cursor.execute(update_command)
        print("[✔] Promedio de la actividad economica trimestral por año de 2010 hasta el 2018 insertado en la base de datos")

    def insertar_actividades_economicas_entidades_2010_2017(self,actividades_economicas_entidades_2010_2017):
        for x in range(1, 33):
            update_command = "UPDATE entidad_federativa SET actividades_economicas='"+json.dumps(actividades_economicas_entidades_2010_2017[x-1])+"' where id="+str(x)
            self.cursor.execute(update_command)
        print("[✔] Promedio de la actividad economica trimestral por año de 2010 hasta el 2018 insertado en la base de datos")

    def insertar_consumo_electrico_municipios_2010_2017(self, nombre_municipios, consumo_municipio):
        for i, nombre in enumerate(nombre_municipios):
            insert_command = "INSERT INTO municipios(nombre, consumo_cfe) VALUES ('"+str(nombre)+"','"+json.dumps(consumo_municipio[i])+"')"
            self.cursor.execute(insert_command)
        print("[✔] Consumo electrico por municipio en todo Mexico insertado en la base de datos")
