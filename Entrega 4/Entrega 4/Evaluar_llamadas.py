# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:51:18 2019

@author: torre
"""
import psycopg2

def Mostrarllamadas(id_tennant):
    lista=[]
    cursor=connection.cursor()
    cursor.execute("select l.id_llamada, l.id_supervisor from llamadas l join agente a on a.id_tennant = {} and a.id_agente = l.id_agente".format(id_tennant))
    rows=cursor.fetchall()
    for row in rows:
        print("ID llamada: ", row[0], "   ID Supervisor: ", row[1])
        lista.append(row[0])
    cursor.close()
    return lista
    
def AgregarCalificacion(id_tennant):
    id_sup=[]
    cursor=connection.cursor()
    cursor.execute("select * from supervisor where  id_tennant = {}".format(id_tennant))
    rows=cursor.fetchall()
    for row in rows:
        print("ID supervisor: ", row[0])
        id_sup.append(row[0])
    d=True
    while(d==True):
        supervisor= input("Ingrese el ID del supervisor que quiere para la llamada ")
        verifi = verificar(id_sup,supervisor)
        while (verifi == True):
            lis=LlamadasNoCalifi(id_tennant)
            numLlamada = input("Ingrese el ID de una llamada: ")
            ver= verificar(lis,numLlamada)
            while (ver == True):
                calif = input("Del  1-7 califique la llamada: ")
                if (1<=int(calif)<=7):
                    sentencia = "Insert into supervision (id_llamada,id_supervisor,aprovado) values("+str(numLlamada)+"," + str(supervisor)+ "," +str(calif)+");"
                    cursor.execute(sentencia)
                    connection.commit()
                    sent = "update llamadas set id_supervisor="+ str(supervisor)+" where id_llamada =" + str(numLlamada)
                    cursor.execute(sent)
                    connection.commit()
                    print("Se agrego calificacion!")
                    d=False
                    verifi=False
                    break
                else:
                    print("Ingrese opción valida")
            if (ver == False):
                print("Ingrese opción valida")
        if (d==False and verifi==False):
            break
        elif(verifi==False):
            print("Ingrese opción valida")
          
        
    cursor.close()
    

def verificar(lista,inpu):
    if (lista.count(int(inpu))):
        return True
    else:
        return False
    
def LlamadasNoCalifi(id_tennant):
    print("Llamadas no calificadas")
    lista=[]
    cursor=connection.cursor()
    cursor.execute("select l.id_llamada, l.id_supervisor from llamadas l join agente a on a.id_tennant = {} and a.id_agente = l.id_agente".format(id_tennant))
    rows=cursor.fetchall()
    for row in rows:
        if (str(row[1]) == "None"): 
            print("ID llamada: ", row[0])
            lista.append(row[0])
    cursor.close()
    return lista

def LlamadasCalifi(id_tennant):
    print("Llamadas calificadas")
    lista=[]
    cursor=connection.cursor()
    cursor.execute("select l.id_llamada, l.id_supervisor from llamadas l join agente a on a.id_tennant = {} and a.id_agente = l.id_agente".format(id_tennant))
    rows=cursor.fetchall()
    for row in rows:
        if (str(row[1]) != "None"): 
            print("ID llamada: ", row[0]," ID supervisor: ", row[1])
            lista.append(row[0])
    cursor.close()
    return lista
    
def EditarCalificacion(id_tennant):
    cursor=connection.cursor()
    lista= LlamadasCalifi(id_tennant)
    d=True
    while (d==True):
        idllamada = input("Ingrese el ID de la llamada  a modificar: ")
        verifica = verificar(lista,idllamada)
        while (verifica == True):
            cali= input("Ingrese la calificacion nueva: ")
            if (1<=int(cali)<=7):
                sentencia = "update supervision set aprovado="+ str(cali)+" where id_llamada =" + str(idllamada)
                cursor.execute(sentencia)
                connection.commit()
                print(" Calificacion cambiada!")
                d=False
                break
            else:
                print("Ingrese opcion valida")
    cursor.close()


def EliminarCalificacion(id_tennant):
    cursor=connection.cursor()
    lista= LlamadasCalifi(id_tennant)
    d=True
    while (d==True):
        idllamada = input("Ingrese el ID de la llamada  a modificar: ")
        verifica = verificar(lista,idllamada)
        while(verifica==True):
            YoN=input("Esta seguro? Y/N ")
            if YoN.lower() == "y":
                sen="delete from supervision where id_llamada="+str(idllamada)
                cursor.execute(sen)
                connection.commit()
                sent="update llamadas set id_supervisor=null where id_llamada=" +str(idllamada)
                cursor.execute(sent)
                connection.commit()
                print("Calificacion eliminada!")
                d=False
                break
            elif YoN.lower() == "n":
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
    login=2
    #Mostrarllamadas(login)
    #AgregarCalificacion(login)
    #EditarCalificacion(login)
    #EliminarCalificacion(login)
    Exit()
