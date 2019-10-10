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

def Showtipification(Login,choice):
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





















import psycopg2   
    
def Connect():
    global connection
    connection=psycopg2.connect(host="201.238.213.114",user="grupo5",password="0BMxCm",database="grupo5",port="54321") 

def Exit():
    connection.close()

 
if __name__ == "__main__":  
    Connect()
    login=0
    ChooseCampaign(login)
    Exit()
