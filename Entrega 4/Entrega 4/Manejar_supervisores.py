# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:11:23 2019

@author: torre
"""
import psycopg2

def numeronuevoID():
    cursor=connection.cursor()
    sen= "Select * from supervisor order by id_supervisor desc limit 1"
    cursor.execute(sen)
    rows=cursor.fetchone()
    idNuevo= rows[0]+1
    cursor.close()
    return idNuevo

def Mostrarsupervisor(id_tennant):
    lista=[]
    cursor=connection.cursor()
    sentencia= "select * from supervisor where id_tennant="+str(id_tennant)
    cursor.execute(sentencia)
    rows=cursor.fetchall()
    for row in rows:
        print("ID supervisor: ",row[0])
        lista.append(row[0])
    cursor.close()
    return lista
    
def verificar(lista,inpu):
    if (lista.count(int(inpu))):
        return True
    else:
        return False

def menuEdit():
    print("1) nombre")
    print("2) apellido")
    print("3) ciudad")
    print("4) calle")
    print("5) numero")
    print("6) telefono")
    
        
def AgregarSupervisor(id_tennant):
    cursor=connection.cursor()
    rut =  input("Ingrese el rut del supervisor:" )
    nombre = input("Ingrese el nombre del supervisor: ")
    apellido = input("Ingrese el apellido del supervisor: ")
    ciudad = input("Ingrese el ciudad del supervisor: ")
    calle = input("Ingrese el calle del supervisor: ")
    numero = input("Ingrese el numero del supervisor: ")
    telef = input("Ingrese el telef del supervisor, sin el +569: ")
    ii=numeronuevoID()
    sentencia = "Insert into supervisor (id_supervisor,id_tennant,rut,nombre,apellido,ciudad,calle,numero,telefono) values('"+ str(ii) +"','"+ str(id_tennant) +"','"+ str(rut) +"','"+ str(nombre) +"','"+ str(apellido) +"','"+ str(ciudad) +"','"+ str(calle) +"','"+ str(numero) +"','"+ str("+569"+telef)+"');"
    cursor.execute(sentencia)
    connection.commit()
    cursor.close()

def EditarInformacion(id_tennant):
    cursor=connection.cursor()
    lista=Mostrarsupervisor(id_tennant)
    d=True
    while(d==True):
        idsu=input("Ingresar ID supervisor: ")
        ver=verificar(lista,idsu)
        while (ver==True):
            menuEdit()
            opcion=input("Ingrese una opcion: ")
            if (opcion=="1"):
                nombre=input("Ingrese nombre: ")
                sentencia="update supervisor set nombre='"+str(nombre)+"' where id_supervisor="+str(idsu)
                cursor.execute(sentencia)
                connection.commit()
                print("Cambio realizado!")
                ver=False
                d=False
            elif (opcion=="2"):
                apellido=input("Ingrese el apellido: ")
                sentencia="update supervisor set apellido='"+str(apellido)+"' where id_supervisor="+str(idsu)
                cursor.execute(sentencia)
                connection.commit()
                print("Cambio realizado!")
                ver=False
                d=False
                
            elif(opcion=="3"):
                ciudad=input("Ingrese la ciudad: ")
                sentencia="update supervisor set cidudad='"+str(ciudad)+"' where id_supervisor="+str(idsu)
                cursor.execute(sentencia)
                connection.commit()
                print("Cambio realizado!")
                ver=False
                d=False
            elif(opcion=="4"):
                calle=input("Ingrese la calle: ")
                sentencia="update supervisor set calle='"+str(calle)+"' where id_supervisor="+str(idsu)
                cursor.execute(sentencia)
                connection.commit()
                print("Cambio realizado!")
                ver=False
                d=False
            elif(opcion=="5"):
                n=input("Ingrese nombre: ")
                sentencia="update supervisor set numero="+str(n)+" where id_supervisor="+str(idsu)
                cursor.execute(sentencia)
                connection.commit()
                print("Cambio realizado!")
                ver=False
                d=False
    
            elif(opcion=="6"):
                telefono=input("Ingrese el telefono, sin incluir +569: ")
                sentencia="update supervisor set telefono='"+str("+569"+telefono)+"' where id_supervisor="+str(idsu)
                cursor.execute(sentencia)
                connection.commit()
                print("Cambio realizado!")
                ver=False
                d=False
            else:
                print("Ingrese opcion valida")
                continue
                
    cursor.close()


def EliminarSupervisor(id_tennant):
    cursor=connection.cursor()
    lista= Mostrarsupervisor(id_tennant)
    d=True
    while(d==True):
        idd=input("Ingrese el  ID del supervisor: ")
        veri=verificar(lista,idd)
        while (veri==True):
            YoN=input("Esta seguro? Y/N")
            if (YoN=="Y" or YoN=="yes" or YoN=="Yes" or YoN=="YES"):
                sentencia="delete from supervisor where id_supervisor="+str(veri)
                cursor.execute(sentencia)
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
    login=2
    #EditarInformacion(2)
    #AgregarSupervisor(2)
    Exit()
