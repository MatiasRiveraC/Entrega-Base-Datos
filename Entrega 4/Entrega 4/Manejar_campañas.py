
def Show_Campaigns_Tennant(Login):
    cursor=connection.cursor()
    sentencia="select id_campaign from tennants_campaigns where id_tennant = "+ str(Login) 
    cursor.execute(sentencia)
    rows=cursor.fetchall()
    print("\n"+"El tennant posee las siguientes campañas:\n")
    print("-----------------------")
    lista = []
    for campaign in rows:
        print(campaign[0])
        lista.append(str(campaign[0]))
    print("-----------------------")
    cursor.close()
    return lista
    
def Agregar_Campaña(Login):
    name = input("Nombre de la campaña: ")
    initDate = input("Fecha Inicio(2019-01-01): ")
    endDate = input("Fecha Término(2019-02-01): ")
    idC = nextIDCampaign()
    try:
        cursor=connection.cursor()
        sentencia="INSERT INTO campaign VALUES("+ str(idC)+",'"+ str(initDate) + "','"+str(endDate)+"', '"+ str(name)+"')"
        cursor.execute(sentencia)
        connection.commit()
        cursor.close()
        cursor=connection.cursor()
        sentencia="INSERT INTO tennants_campaigns VALUES("+ str(Login)+","+ str(idC) + ")" 
        cursor.execute(sentencia)
        connection.commit()
        cursor.close()
        print("Campaña creada")
    except:
        print("ERROR creando campaña")
    
def Eliminar_campaña(Login):
    lista = Show_Campaigns_Tennant(Login)
    while True:
        choice = input("Ingrese la campaña que desea eliminar: ")
        if choice in lista:
            break
        print("Ingrese una campaña válida")
    
    while True:
        print("Desea eliminar la campaña "+choice+"?")
        warning = input("Y/N: ")
        if warning.lower() == "y":
            warning = True
            break
        elif warning.lower() == "n":
            warning = False
            break
    if warning:
        try:
            cursor=connection.cursor()
            sentencia="Delete from tennants_campaigns where id_campaign ="+str(choice)+" and id_tennant="+str(Login)
            cursor.execute(sentencia)
            connection.commit()
            cursor.close()
            cursor=connection.cursor()
            sentencia="Delete from campaign where id_campaign ="+str(choice)
            cursor.execute(sentencia)
            connection.commit()
            cursor.close()
            print("Campaña Eliminada")
        except:
            print("ERROR elimando campaña")
            
def Editar_Campaña(Login):
    lista = Show_Campaigns_Tennant(Login)
    while True:
        choice = input("Ingrese la campaña que desea editar: ")
        if choice in lista:
            break
        print("Ingrese una campaña válida")
    while True:
        cursor=connection.cursor()
        sentencia="select * from campaign where id_campaign = "+ str(choice) 
        cursor.execute(sentencia)
        rows=cursor.fetchall()
        cursor.close()
        for item in rows:
            print(item)
        print("Que desea editar?\n")
        print("1) Fecha Inicio")
        print("2) Fecha Término")
        print("3) Nombre")
        print("4) Exit")
        options = input("==> ")
        if options == "1":
            initDate = input("Fecha Inicio(2019-01-01): ")
            try:
                cursor=connection.cursor()
                sentencia="UPDATE campaign SET Fecha_Inicio='"+str(initDate)+"' where id_campaign ="+str(choice) 
                cursor.execute(sentencia)
                connection.commit()
                cursor.close()
                print("Campaña editada!")
                print("")
            except:
                print("ERROR al editar Fecha de Inicio")
                print("")
                             
        elif options == "2":
            endDate = input("Fecha Término(2019-02-01): ")
            try:
                cursor=connection.cursor()
                sentencia="UPDATE campaign SET Fecha_Termino='"+str(endDate)+"' where id_campaign ="+str(choice) 
                cursor.execute(sentencia)
                connection.commit()
                cursor.close()
                print("Campaña editada!")
                print("")
            except:
                print("ERROR al editar Fecha de Inicio")
                print("")

        elif options == "3":
            name = input("Nombre: ")
            try:
                cursor=connection.cursor()
                sentencia="UPDATE campaign SET Nombre='"+str(name)+"'where id_campaign ="+str(choice) 
                cursor.execute(sentencia)
                connection.commit()
                cursor.close()
                print("Campaña editada!")
                print("")
            except:
                print("ERROR al editar Fecha de Inicio")
                print("")
        
        elif options == "4":
            break
    
    
    



def nextIDCampaign():
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM campaign order by id_campaign desc limit 1")
    rows=cursor.fetchone()
    nextIDCampaign=rows[0]+1
    cursor.close()
    return nextIDCampaign



import psycopg2   
    
def Connect():
    global connection
    connection=psycopg2.connect(host="201.238.213.114",user="grupo5",password="0BMxCm",database="grupo5",port="54321") 

def Exit():
    connection.close()

 
if __name__ == "__main__":  
    login=10
    Connect()
    Eliminar_campaña(login)

    Exit()
