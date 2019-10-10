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

#Funcion para mostrar las campañas disponibles para el tennat ademas de poder seleecionar 1 de ellas
def ShowCampaigns(Login):
    ListCampaign=[]
    cursor=connection.cursor()
    sentencia="select c.id_campaign, c.fecha_inicio, c.fecha_termino,c.nombre from tennants_campaigns t join campaign c on t.id_campaign = c.id_campaign where t.id_tennant ="+str(Login)
    cursor.execute(sentencia)
    rows=cursor.fetchall()
    if len(rows)!=0:
        for a in rows:
            print("Id_Campaign:",a[0])
            print("Nombre campaña:",a[3])
            print("Fecha inicio:",a[1])
            print("Fecha termino:",a[2])
            print("-------------------------------")
            ListCampaign.append(a[0])
    else:
        print("No hay campañas para este tennant")
    cursor.close()  
    return ListCampaign

#Funcion para elegir campaña y mostrar las tipificaciones
def ChooseCampaign(Login):
    ListCampaign=ShowCampaigns(Login)
    if len(ListCampaign)==0:
        return (False,-1)
    else:
        while True:
            choice=input("Seleccione un ID_campaña\n")
            try:
                choice=int(choice)
                if choice in ListCampaign:
                    Showtipification(Login,choice)
                    return (True,choice)
                else:
                    print("Ingrese opcion valida")
            except:
                print("Ingrese opcion Valida")

#Funcion para mostrar las tipificaciones
def Showtipification(Login):
    cursor=connection.cursor()
    sentencia="select t.id_pregunta, t.tipo_dato,t.pregunta_asociada from (tipificaciones_campaign tic join tipificacion t on tic.id_pregunta = t.id_pregunta) join tennants_campaigns tec on tec.id_campaign = tic.id_campaign where tic.id_campaign="+str(Login)
    cursor.execute(sentencia)
    rows=cursor.fetchall()
    if len(rows)!=0:
        for a in rows:
            print("Id_Pregunta:",a[0])
            print("Pregunta asociada:",a[2])
            print("Tipo de respuesta:",a[1])
            print("-------------------------------")
    else:
        print("No hay tipifiaciones para esta campaña")
    cursor.close()  

#Funcion para agregar tipifiaciones
def AddTipification(Login,Choice):
    cursor=connection.cursor()
    Id=nextIDPregunta()
    Question = input("Ingrese la pregunta que quiere crear\n")
    Type=ChooseType()
    sentencia="insert into tipificacion values ("+str(Id)+",'"+str(Type)+"','"+str(Question)+"')"
    cursor.execute(sentencia)
    connection.commit()
    sentencia="insert into tipificaciones_campaign values ("+str(Login)+","+str(Id)+")"
    cursor.execute(sentencia)
    connection.commit()
    print("Pregunta creada con exito")
    
#Funcion para agregar un tipificacion en una llamada, esto se hace al asociar una campaña a una llamada
def AddCampaignToCall(Login,Choice):
    ListAvailableCall=ListCall(Login,Choice)
    if len(ListAvailableCall)==0:
        return
    else:
        while True:
            choice1=input("Seleccione un Id llamada\n")
            try:
                choice1=int(choice1)
                if choice1 in ListAvailableCall:
                    cursor=connection.cursor()
                    sentencia="Update llamadas set id_campaign="+str(Choice)+" where id_llamada ="+str(choice1)
                    cursor.execute(sentencia)
                    connection.commit()
                    print("EDICIÓN REALIZADA")
                    break
                else:
                    print("Ingrese opcion valida")
            except:
                print("Ingrese opcion Valida")

#Funcion que muestra todas las llamadas del tennant dentro de cierto rango de fechas, ademas de devolver una lista de las que exiten
def ListCall(Login,Choice):
    ListAvailableCall=[]
    cursor=connection.cursor()
    sentencia="select fecha_inicio, fecha_termino from campaign where id_campaign="+str(Choice)
    cursor.execute(sentencia)
    rows=cursor.fetchone()
    FechaInicio=rows[0]
    FechaTermino=rows[1]
    sentencia="select id_llamada from (llamadas l join agente a on l.id_agente=a.id_agente) join tennant t on a.id_tennant = t.id_tennant where t.id_tennant ="+str(Login)+" and '"+str(FechaInicio)+"' <l.fecha_llamada and '"+str(FechaTermino)+"'> l.fecha_llamada"
    cursor.execute(sentencia)
    rows=cursor.fetchall()
    if len(rows)!=0:
        print("Llamadas disponibles para editar:")
        for a in rows:
            print("Id Llamada:",a[0])
            ListAvailableCall.append(a[0])
    else:
        print("No hay llamadas a las cuales le puedas asociar esta campaña")
    cursor.close()  
    return ListAvailableCall





#Funcion para eliminar una tipificacion de un campaña
def KillTipification(Login,Choice):
    ListTipificacione=CantidadTipificaciones(Login)
    while True:
        choice=input("Ingrese Id_Pregunta \n")
        try:
            choice=int(choice)
            if choice in ListTipificacione:
                sure=YesOrNo("Estas seguro que quieres eliminar esta pregunta? Y/N \n")
                if sure=="y":
                    cursor=connection.cursor()
                    sentencia="delete from tipificaciones_campaign where id_pregunta="+str(choice)
                    cursor.execute(sentencia)
                    connection.commit()
                    sentencia="delete from tipificacion where id_pregunta="+str(choice)
                    cursor.execute(sentencia)
                    connection.commit()
                    cursor.close()
                    print("Pregunta Eliminada")
                    break
                else:
                    sure1=YesOrNo("Desea borrar otra pregunta? Y/N \n")
                    if sure1=="n": 
                        break
            else:
                print("Ingrese Opcion Valida")
        except:
            print("Ingrese Opcion Valida")  
            
#Funcion que crear una lista de las tipificaciones existentes. Esta funcion para crear una lista la cual se usa para comprobar si es que un id pertencese a una pregunta real
def CantidadTipificaciones(Login):
    cursor=connection.cursor()
    ListTipificacione=[]
    sentencia="select t.id_pregunta from (tipificaciones_campaign tic join tipificacion t on tic.id_pregunta = t.id_pregunta) join tennants_campaigns tec on tec.id_campaign = tic.id_campaign where tic.id_campaign="+str(Login)
    cursor.execute(sentencia)
    rows=cursor.fetchall()
    for a in rows:
        ListTipificacione.append(a[0])
    cursor.close()
    return ListTipificacione

#Funcion para editar tipificacion
def EditTipification(Login,Choice):
    ListTipificacione=CantidadTipificaciones(Login)
    while True:
        choice=input("Ingrese Id_Pregunta \n")
        try:
            choice=int(choice)
            if choice in ListTipificacione:
                cursor=connection.cursor()
                while True:
                    choice1=input("Ingrese que opcion que quiere editar\n1) Sentencia de la Pregunta\n2) Tipo de respuesta\n3) Salir\n")
                    try:
                        choice1=int(choice1)
                        if choice1==1:
                            aux=input("Ingrese la nueva pregunta\n")
                            sentencia="Update tipificacion set pregunta_asociada='"+str(aux)+"' where id_pregunta ="+str(choice)
                            cursor.execute(sentencia)
                            connection.commit()
                            print("EDICIÓN REALIZADA")
                            if YesOrNo("Desea hacer otra operacion? Y/N\n")=="n":
                                break
                        elif choice1 == 2:
                            aux=ChooseType()
                            sentencia="Update tipificacion set tipo_dato='"+str(aux)+"' where id_pregunta ="+str(choice)
                            cursor.execute(sentencia)
                            connection.commit()
                            print("EDICIÓN REALIZADA")
                            if YesOrNo("Desea hacer otra operacion? Y/N\n")=="n":
                                break
                        elif choice1== 3:
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

#Funcion para editar asociacion ... por ahora nuestro modelo no calza con esta consulta
# Asi q voy a escribirlo asi nomas pero no se si lo implementemos
def EditAssociation(Login,Choice):
    print("Not yet implemented because of logic reasons")

#Funcion que calcula el siguiente ID para insertar
def nextIDPregunta():
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM tipificacion order by id_pregunta desc limit 1")
    rows=cursor.fetchone()
    nextIDLlamada=rows[0]+1
    cursor.close()
    return nextIDLlamada

#Funcion para elegir el tipo de respuesta a la pregunta
def ChooseType():
    while True:
        answ=input("Seleccione el tipo de respuesta a su pregunta\n1)string\n2)int\n3)bool\n")
        try:
            answ=int(answ)
            if answ ==1:
                return "string"
            elif answ==2:
                return "int"
            elif answ == 3:
                return "bool"
            else:
                print("Ingrese Opcion Valida")
        except:
            print("Ingrese Opcion Valida")
















import psycopg2   
    
def Connect():
    global connection
    connection=psycopg2.connect(host="201.238.213.114",user="grupo5",password="0BMxCm",database="grupo5",port="54321") 

def Exit():
    connection.close()

 
if __name__ == "__main__":  
    Connect()
    login=0
    AddCampaignToCall(login,0)
    Exit()
