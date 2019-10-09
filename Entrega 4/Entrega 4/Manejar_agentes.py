def Show_Agentes(Login):
    cursor=connection.cursor()
    sentencia="select id_agente from agente where id_tennant = "+ str(Login) 
    cursor.execute(sentencia)
    rows=cursor.fetchall()
    print("\n"+"El tennant posee las siguientes Agentes:\n")
    print("-----------------------")
    lista = []
    for agente in rows:
        print(agente[0])
        lista.append(str(agente[0]))
    print("-----------------------")
    cursor.close()
    return lista

def Agregar_Agente(Login):
    name = input("Nombre del agente: ")
    rut = input("RUT del Agente(12345678-9): ")
    lastName = input("Apellido del Agente(Bravo_Diaz): ")
    city = input("Ciudad del Agente: ")
    calle = input("Dirección del Agente(sin número de calle): ")
    num = input("Numero de la calle: ")
    phone = input("Número de teléfono del Agente(+56998765432)): ")
    idA = nextIDAgente()
    try:
        cursor=connection.cursor()
        sentencia="INSERT INTO agente VALUES("+ str(idA)+","+ str(Login) + ",'"+str(rut)+"', '"+ str(name)+"','"+ str(lastName)+"', '"+ str(city)+"','"+ str(calle)+"','" + str(num)+"','"+ str(phone)+"' )"
        cursor.execute(sentencia)
        connection.commit()
        cursor.close()
        print("Agente creado")
    except:
        print("ERROR creando Agente")
    





def Edit_Information(Login):
    lista = Show_Agentes(Login)
    while True:
        choice = input("Ingrese el Agente que desea editar: ")
        if choice in lista:
            break
        print("Ingrese un Agente válida")
    while True:
        cursor=connection.cursor()
        sentencia="select * from agente where id_agente = "+ str(choice) 
        cursor.execute(sentencia)
        rows=cursor.fetchall()
        cursor.close()
        for item in rows:
            print(item)
        print("Que desea editar?\n")
        print("1) RUT")
        print("2) Nombre")
        print("3) Apellido")
        print("4) Ciudad")
        print("5) Calle")
        print("6) Numero")
        print("7) Télefono")
        print("8) Exit")
        options = input("==> ")
        if options == "1":
            rut = input("RUT del Agente(12345678-9): ")
            try:
                cursor=connection.cursor()
                sentencia="UPDATE agente SET rut='"+str(rut)+"' where id_agente ="+str(choice)
                cursor.execute(sentencia)
                connection.commit()
                cursor.close()
                print("RUT editado!")
                print("")
            except:
                print("ERROR al editar RUT")
                print("")
                             
        elif options == "2":
            name = input("Nombre del agente: ")
            try:
                cursor=connection.cursor()
                sentencia="UPDATE agente SET nombre='"+str(name)+"' where id_agente ="+str(choice)
                cursor.execute(sentencia)
                connection.commit()
                cursor.close()
                print("Nombre editadao!")
                print("")
            except:
                print("ERROR al editar Nombre")
                print("")

        elif options == "3":
            lastName = input("Apellido del Agente(Bravo_Diaz): ")
            try:
                cursor=connection.cursor()
                sentencia="UPDATE agente SET apellido='"+str(lastName)+"' where id_agente ="+str(choice)
                cursor.execute(sentencia)
                connection.commit()
                cursor.close()
                print("Apellido editado!")
                print("")
            except:
                print("ERROR al editar Apellido")
                print("")
        elif options == "4":
            city = input("Ciudad del Agente: ")
            try:
                cursor=connection.cursor()
                sentencia="UPDATE agente SET ciudad='"+str(city)+"' where id_agente ="+str(choice)
                cursor.execute(sentencia)
                connection.commit()
                cursor.close()
                print("Ciudad editada!")
                print("")
            except:
                print("ERROR al editar Ciudad")
                print("")

        elif options == "5":
            calle = input("Dirección del Agente(sin número de calle): ")
            try:
                cursor=connection.cursor()
                sentencia="UPDATE agente SET calle='"+str(calle)+"' where id_agente ="+str(choice)
                cursor.execute(sentencia)
                connection.commit()
                cursor.close()
                print("Dirección editada!")
                print("")
            except:
                print("ERROR al editar Dirección")
                print("")
        elif options == "6":
            num = input("Numero de la calle: ")
            try:
                cursor=connection.cursor()
                sentencia="UPDATE agente SET num='"+str(num)+"' where id_agente ="+str(choice)
                cursor.execute(sentencia)
                connection.commit()
                cursor.close()
                print("Número editado!")
                print("")
            except:
                print("ERROR al editar Número")
                print("")

        elif options == "7":
            phone = input("Número de teléfono del Agente(+56998765432)): ")
            try:
                cursor=connection.cursor()
                sentencia="UPDATE agente SET telefono='"+str(phone)+"' where id_agente ="+str(choice)
                cursor.execute(sentencia)
                connection.commit()
                cursor.close()
                print("Teléfono editado!")
                print("")
            except:
                print("ERROR al editar Teléfono")
                print("")
        elif options == "8":
            break




def Eliminar_Agente(Login):
    lista = Show_Agentes(Login)
    while True:
        choice = input("Ingrese el Agente que desea eliminar: ")
        if choice in lista:
            break
        print("Ingrese un Agente válido")
    
    while True:
        print("Desea eliminar el Agente: "+choice+"?")
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
            sentencia="Delete from agente where id_agente ="+str(choice)+" and id_tennant="+str(Login)
            cursor.execute(sentencia)
            connection.commit()
            cursor.close()
            cursor=connection.cursor()
            sentencia="Delete from llamadas where id_agente ="+str(choice)
            cursor.execute(sentencia)
            connection.commit()
            cursor.close()
            print("Agente Eliminado")
        except:
            print("ERROR elimando Agente")



def nextIDAgente():
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM agente order by id_agente desc limit 1")
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
    Connect()
    login=0
    #Eliminar_Agente(login)
    #Agregar_Agente(login)
    #Edit_Information(login)
    Exit()
