# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 20:04:40 2019

@author: torre
"""

import psycopg2

def MostrarTennant():
    lista=[]
    cursor=connection.cursor()
    sentencia = "select * from tennant"
    cursor.execute(sentencia)
    rows=cursor.fetchall()
    for row in rows:
        print("ID tennant: ",row[0], " Nombre: ",row[1])
        lista.append(row[0])
    cursor.close()
    return lista

def verificar(lista,inpu):
    if (lista.count(int(inpu))):
        return True
    else:
        return False

def NextId():
    cursor=connection.cursor()
    sen= "Select * from tennant order by id_tennant desc limit 1"
    cursor.execute(sen)
    rows=cursor.fetchone()
    idNuevo= rows[0]+1
    cursor.close()
    return idNuevo

def AgregarTennant():
    cursor=connection.cursor()
    idtennant=NextId()
    nombre= input("Ingrese un nombre para el tennant: ")
    sentencia = "insert into tennant (id_tennant,nombre) values("+str(idtennant)+",'"+str(nombre)+"')"
    cursor.execute(sentencia)
    connection.commit()
    print("Se agrego el tennant!")
    cursor.close()
    
def LlamadasEliminar(listaAgente):
    ll=[]
    cursor=connection.cursor()
    for i in listaAgente:
        sentencia="select * from llamadas where id_agente="+str(i)
        cursor.execute(sentencia)
        rows=cursor.fetchall()
        for row in rows:
            ll.append(row[0])
    
    cursor.close()
    return ll

def EditarInformacion():
    pass

def EliminarTennant():
    cursor=connection.cursor()
    lista=MostrarTennant()
    lis=[]
    d=True
    while(d==True):
        idd=input("Ingrese el  ID del tennant: ")
        veri=verificar(lista,idd)
        while (veri==True):
            YoN=input("Esta seguro? Y/N")
            if (YoN=="Y" or YoN=="yes" or YoN=="Yes" or YoN=="YES"):
                sentencia = "delete from tennant where id_tennant="+str(idd)
                cursor.execute(sentencia)
                connection.commit()
                s="select * from agente where id_tennant="+str(idd)
                cursor.execute(s)
                rows=cursor.fetchall()
                for row in rows:
                    lis.append(row[0])
                sen="delete from agente where id_tennant="+str(idd)
                cursor.execute(sen)
                connection.commit()
                for i in lis:
                    pala="delete from llamadas where  id_agente="+str(i)
                    cursor.execute(pala)
                    connection.commit()
                ll=LlamadasEliminar(lis)
                for d in ll:
                    eli="delete from respuestas_tipificaciones where id_llamada="+str(d)
                    cursor.execute(eli)
                    connection.commit()
                    sup="delete from supervision where id_llamada="+str(d)
                    cursor.execute(sup)
                    connection.commit()
                supp="delete from supervisor where id_tennant="+str(idd)
                cursor.execute(supp)
                connection.commit()
                campa="delete from tennants_campaigns where id_tennant="+str(idd)
                cursor.execute(campa)
                connection.commit()
                print("Supervisor eliminado")
                veri=False
                d=False
            else:
                d=False
                break
    
    cursor.close()

def Connect():
    global connection
    connection=psycopg2.connect(host="201.238.213.114",user="grupo5",password="0BMxCm",database="grupo5",port="54321") 

def Exit():
    connection.close()
    
if __name__ == "__main__": 
    Connect()
    #AgregarTennant()
    #EliminarTennant()
    
    Exit()
