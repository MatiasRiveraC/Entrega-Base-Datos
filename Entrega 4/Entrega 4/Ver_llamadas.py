#Funcion que calcula el siguiente ID para insertar
def nextIDLlamada():
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM llamadas order by id_llamada desc limit 1")
    rows=cursor.fetchone()
    nextIDLlamada=rows[0]+1
    cursor.close()
    return nextIDLlamada
    
#Funcion que crear una lista de los Id_llamadas existentes. Esta funcion para crear una lista la cual se usa para comprobar si es que un id pertencese a una llamda real
def CantidadLLamadas(Login):
    cursor=connection.cursor()
    DiccLlamadas=[]
    cursor.execute("SELECT * FROM llamadas order by id_llamada")
    rows=cursor.fetchall()
    for a in rows:
        DiccLlamadas.append(a[0])
    cursor.close()
    return DiccLlamadas
#Funcion que crea un alista con los id_llamadas existentes para un tennant dado
def IdLlamadasPorTennant(Login):
    cursor=connection.cursor()
    DiccLlamadas=[]
    cursor.execute("select l.id_llamada from (llamadas l join agente a on l.id_agente=a.id_agente) join tennant t on a.id_tennant = t.id_tennant where t.id_tennant ="+str(Login))
    rows=cursor.fetchall()
    for a in rows:
        DiccLlamadas.append(a[0])
    cursor.close()
    return DiccLlamadas
    
#Funcion que muestra agentes
def mostrarAgentes(Login):
    cursor=connection.cursor()
    DiccAgent=[]
    cursor.execute("SELECT id_agente, nombre, rut FROM agente where id_tennant="+str(Login))
    rows=cursor.fetchall()
    for a in rows:
        print("ID:" ,a[0])
        print("Nombre:" ,a[1])
        print("Rut:" ,a[2])
        print("-------------------------------")
        DiccAgent.append(a[0])
    cursor.close()
    return DiccAgent

#Funcion que muestra clientes
def mostrarCliente():
    cursor=connection.cursor()
    DiccClient=[]
    cursor.execute("SELECT rut, nombre FROM cliente")
    rows=cursor.fetchall()
    for a in rows:
        print("Rut:" ,a[0])
        print("Nombre:" ,a[1])
        print("-------------------------------")
        DiccClient.append(a[0])
    cursor.close()
    return DiccClient

#Funcion que muestra clientes y que te deja seleccionar uno
def ChoosedClient(): 
    DiccClient=mostrarCliente()
    while True:
        choice=input("Seleccione rut del Cliente \n")
        try:
            if choice in DiccClient:
                ChoosedClient=choice
                return ChoosedClient
            else:
                print("Ingrese Opcion Valida")
        except:
            print("Ingrese Opcion Valida")

#Funcion que muestra agente y que te deja seleccionar uno
def ChoosedAgent(Login): 
    DiccAgent=mostrarAgentes(Login)
    while True:
        choice=input("Seleccione id del Agente \n")
        try:
            choice=int(choice)
            if choice in DiccAgent:
                ChoosedAgent=choice
                return ChoosedAgent
            else:
                print("Ingrese Opcion Valida")
        except:
            print("Ingrese Opcion Valida")

#Funcion que hace preguntas de verdadero o falso         
def TrueOrFalse(pregunta):
    while True:
        choice=input(pregunta).lower()
        if choice == "true" or choice =="false":
            return choice
        else:
            print("Ingrece opcion valida")
            

#Funcion para mostrar campañas disponibles
def ShowCampaigns(Fecha,Login):
    ListCampaign=[]
    cursor=connection.cursor()
    sentencia="select c.id_campaign , c.nombre from  campaign c join  tennants_campaigns t on c.id_campaign=t.id_campaign where c.fecha_inicio < '"+Fecha+"' and c.fecha_termino > '"+Fecha+"'  and t.id_tennant ="+str(Login)
    cursor.execute(sentencia)
    rows=cursor.fetchall()
    if len(rows)!=0:
        for a in rows:
            print("Id_Campaign",a[0])
            print("-------------------------------")
            ListCampaign.append(a[0])
    else:
        print("No hay campañas para esta fecha")
    cursor.close()  
    return ListCampaign
#Funcion para seleccionar de las campañas disponibles
def IfInCampaign(Fecha,Login):
    answ=YesOrNo("Desea que su llamada pertenesca a una campaña Y/N \n")
    if answ =="y": 
        ListCampaign=ShowCampaigns(Fecha,Login)
        if len(ListCampaign)==0:
            return "null"
        else:
            while True:
                choice=input("Seleccione un ID_campaña\n")
                try:
                    choice=int(choice)
                    if choice in ListCampaign:
                        ChoosedCampaign=choice
                        return ChoosedCampaign
                    else:
                        print("Ingrese opcion valida")
                except:
                    print("Ingrese opcion Valida")
    else:
        return "null"
                    
            
#funcion para crear una llamda            
def InsertLlamada(Login):
    Agente= ChoosedAgent(Login)
    Cliente= ChoosedClient()
    realizada= TrueOrFalse("Ingrese si la llamda fue realizada por el agente (True) o realizada por el cliente (False) \n")
    cursor=connection.cursor()
    nombre_archivo= str(input("Nombre del archivo \n"))
    Fecha=str(input("Ingrese fecha EJ: 2017-5-28 \n"))
    Hora=str(input("Ingrese la hora de la llamada EJ: 0:2:12 Hora:Minutos:Segundos \n"))
    Duracion=str(input("Ingrese duracion EJ: 0:2:12 Hora:Minutos:Segundos \n"))
    Transcripcion=str(input("Ingrese transcripcion \n"))
    Motivo=str(input("Ingrese motivo \n"))
    Supervisor="null"
    Campaign= IfInCampaign(Fecha,Login)
    sentencia="Insert into llamadas values("+str(nextIDLlamada())+","+str(realizada)+",'"+str(nombre_archivo)+"','"+str(Fecha)+"','"+str(Hora)+"','"+str(Duracion)+"','"+str(Transcripcion)+"','"+str(Motivo)+"','"+str(Cliente)+"',"+str(Agente)+","+str(Supervisor)+","+str(Campaign)+")"
    cursor.execute(sentencia)
    connection.commit()
    cursor.close()


#Mostrar todas las llamadas del tennant
def ShowCall(Login):
    cursor=connection.cursor()
    sentencia="select l.id_llamada from (llamadas l join agente a on l.id_agente=a.id_agente) join tennant t on a.id_tennant = t.id_tennant where t.id_tennant ="+str(Login)
    cursor.execute(sentencia)
    rows=cursor.fetchall()
    for a in rows:
        print("Id_llamada",a[0])
        print("-------------------------------")
    cursor.close()
#Funcion que muestra la info de una llamda    
def ShowCallInfo(Login):
    DiccLlamadas=CantidadLLamadas(Login)
    while True:
        choice=input("Ingrese Id_Llamada \n")
        try:
            choice=int(choice)
            if choice in DiccLlamadas:
                cursor=connection.cursor()
                sentencia="select l.id_llamada,l.realizada,l.nombre_archivo,l.fecha_llamada,l.duracion,l.transcripcion,l.motivo,l.rut,l.id_agente,l.id_supervisor,l.id_campaign,l.hora from (llamadas l join agente a on l.id_agente=a.id_agente) join tennant t on a.id_tennant = t.id_tennant where l.id_llamada ="+str(choice)+" and t.id_tennant ="+str(Login)
                cursor.execute(sentencia)
                rows=cursor.fetchall()
                for a in rows:
                    print()
                    print("Id_llamada:",a[0])
                    print("Realizada:",a[1])
                    print("Nombre Archivo:",a[2])
                    print("Fecha Llamada:",a[3])
                    print("Hora de la llamada:",a[11])
                    print("Duracion:",a[4])
                    print("Transcripcion:",a[5])
                    print("Motivo:",a[6])
                    print("Rut Cliente:",a[7])
                    print("Id_Agente:",a[8])
                    print("Id_Supervisor:",a[9])
                    print("Id_Campaña:",a[10])
                cursor.close()
                break
            else:
                print("Ingrese Opcion Valida")
        except:
                    
            print("Ingrese Opcion Valida")

#Funcion para eliminar llamadas
def KillCall(Login):
    DiccLlamadas=CantidadLLamadas(Login)
    while True:
        choice=input("Ingrese Id_Llamada \n")
        try:
            choice=int(choice)
            if choice in DiccLlamadas:
                sure=YesOrNo("Estas seguro que quieres eliminar la llamada "+str(choice)+" ? Y/N \n")
                if sure=="y":
                    cursor=connection.cursor()
                    sentencia="Delete from llamadas where id_llamada ="+str(choice)
                    cursor.execute(sentencia)
                    connection.commit()
                    cursor.close()
                    print("Llamada Eliminada")
                    break
                else:
                    sure1=YesOrNo("Desea borrar otra llamada? Y/N \n")
                    if sure1=="n": 
                        break
            else:
                print("Ingrese Opcion Valida")
        except:
            print("Ingrese Opcion Valida")  

#Funcion Editar llamadas
def EditCall(Login):
    DiccLlamadas=IdLlamadasPorTennant(Login)
    while True:
        choice=input("Ingrese Id_Llamada \n")
        try:
            choice=int(choice)
            if choice in DiccLlamadas:
                cursor=connection.cursor()
                while True:
                    choice1=input("Ingrese que opcion que quiere editar\n1) Realizada\n2) Nombre Archivo\n3) Fecha Llamada\n4) Duración\n5) Transcripción\n6) Motivo\n7) Rut Cliente\n8) Id Agente\n9) Id_campaña\n10) Hora Llamada\n11) Salir\n")
                    try:
                        choice1=int(choice1)
                        if choice1==1:
                            aux=TrueOrFalse("Ingrese true para llamada realizada o false para llamda recibida\n")
                            sentencia="Update llamadas set realizada='"+str(aux)+"' where id_llamada ="+str(choice)
                            cursor.execute(sentencia)
                            connection.commit()
                            print("EDICIÓN REALIZADA")
                            if YesOrNo("Desea hacer otra operacion? Y/N\n")=="n":
                                break
                        elif choice1 == 2:
                            aux=input("Ingrese el nuevo nombre del archivo\n")
                            sentencia="Update llamadas set nombre_archivo='"+str(aux)+"' where id_llamada ="+str(choice)
                            cursor.execute(sentencia)
                            connection.commit()
                            print("EDICIÓN REALIZADA")
                            if YesOrNo("Desea hacer otra operacion? Y/N\n")=="n":
                                break
                        elif choice1== 3:
                            aux=input("Ingrese la nueva fecha de llamda Ej: 2017-5-28\n")
                            sentencia="Update llamadas set fecha_llamada='"+str(aux)+"' where id_llamada ="+str(choice)
                            cursor.execute(sentencia)
                            connection.commit()
                            print("EDICIÓN REALIZADA")
                            if YesOrNo("Desea hacer otra operacion? Y/N\n")=="n":
                                break
                        elif choice1 == 4:
                            aux=input("Ingrese la nueva duración de llamda Ej: 2:5:12\n")
                            sentencia="Update llamadas set duracion='"+str(aux)+"' where id_llamada ="+str(choice)
                            cursor.execute(sentencia)
                            connection.commit()
                            print("EDICIÓN REALIZADA")
                            if YesOrNo("Desea hacer otra operacion? Y/N\n")=="n":
                                break
                        elif choice1 == 5:
                            aux=input("Ingrese la nueva transcripción del archivo\n")
                            sentencia="Update llamadas set transcripcion='"+str(aux)+"' where id_llamada ="+str(choice)
                            cursor.execute(sentencia)
                            connection.commit()
                            print("EDICIÓN REALIZADA")
                            if YesOrNo("Desea hacer otra operacion? Y/N\n")=="n":
                                break
                        elif choice1 == 6:
                            aux=input("Ingrese el nuevo motivo del archivo\n")
                            sentencia="Update llamadas set motivo='"+str(aux)+"' where id_llamada ="+str(choice)
                            cursor.execute(sentencia)
                            connection.commit()
                            print("EDICIÓN REALIZADA")
                            if YesOrNo("Desea hacer otra operacion? Y/N\n")=="n":
                                break
                        elif choice1 == 7:
                            Cliente= ChoosedClient()
                            sentencia="Update llamadas set rut='"+str(Cliente)+"' where id_llamada ="+str(choice)
                            cursor.execute(sentencia)
                            connection.commit()
                            print("EDICIÓN REALIZADA")
                            if YesOrNo("Desea hacer otra operacion? Y/N\n")=="n":
                                break
                        elif choice1 == 8:
                            Agente= ChoosedAgent(Login)
                            sentencia="Update llamadas set id_agente='"+str(Agente)+"' where id_llamada ="+str(choice)
                            cursor.execute(sentencia)
                            connection.commit()
                            print("EDICIÓN REALIZADA")
                            if YesOrNo("Desea hacer otra operacion? Y/N\n")=="n":
                                break
                        elif choice1 == 9:
                            sentencia="select fecha_llamada from llamadas where id_llamada="+str(choice)
                            cursor.execute(sentencia)
                            rows=cursor.fetchone()
                            Fecha=str(rows[0])
                            ListCampaign=ShowCampaigns(Fecha,Login)
                            if len(ListCampaign)==0:
                                break
                            else:
                                while True:
                                    choice2=input("Seleccione un ID_campaña\n")
                                    try:
                                        choice2=int(choice2)
                                        if choice2 in ListCampaign:
                                            sentencia="Update llamadas set id_campaign="+str(choice2)+" where id_llamada ="+str(choice)
                                            cursor.execute(sentencia)
                                            connection.commit()
                                            print("EDICIÓN REALIZADA")
                                            if YesOrNo("Desea hacer otra operacion? Y/N\n")=="n":
                                                break
                                        else:
                                            print("Ingrese opcion valida")
                                    except:
                                        print("Ingrese opcion Valida")
                        elif choice1 == 10:
                            aux=input("Ingrese la nueva hora de llamda Ej: 2:2:12\n")
                            sentencia="Update llamadas set hora='"+str(aux)+"' where id_llamada ="+str(choice)
                            cursor.execute(sentencia)
                            connection.commit()
                            print("EDICIÓN REALIZADA")
                            if YesOrNo("Desea hacer otra operacion? Y/N\n")=="n":
                                break
                        
                        elif choice1==11:
                            break
                        
                        else:
                            print("Ingrese Opcion Valida")
                    except:
                        print("Ingrese Opcion Valida")  
                cursor.close()
                break
            else:
                print("Ingrese Opcion Valida")
        except:
                    
            print("Ingrese Opcion Valida")
   
            
#Funcion para hacer preguntas binarias
def YesOrNo(pregunta):
    while True:
        respuesta=input(pregunta).lower()
        if respuesta == "y" or respuesta=="n":
            if respuesta == "y":
                return "y"
            if respuesta=="n":
                return "n"
        else:
            print("Ingrese Opcion valida")
            
            
            
            
            
            
import psycopg2   
    
def Connect():
    global connection
    connection=psycopg2.connect(host="201.238.213.114",user="grupo5",password="0BMxCm",database="grupo5",port="54321") 

def Exit():
    connection.close()
#Main work area    
if __name__ == "__main__":  
    Connect()
    login=0
    InsertLlamada(login)
    Exit()

