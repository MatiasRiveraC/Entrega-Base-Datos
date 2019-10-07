
def Show_Campaigns_Tennant(Login):
    cursor=connection.cursor()
    sentencia="select id_campaign from tennants_campaigns where id_tennant = "+ str(Login) 
    cursor.execute(sentencia)
    rows=cursor.fetchall()
    print("\n"+"El tennant posee las siguientes campañas:\n")
    print("-----------------------")
    for campaign in rows:
        print(campaign[0])
    print("-----------------------")

def Agregar_Campaña(Login):
    pass






import psycopg2   
    
def Connect():
    global connection
    connection=psycopg2.connect(host="201.238.213.114",user="grupo5",password="0BMxCm",database="grupo5",port="54321") 

def Exit():
    connection.close()

 
if __name__ == "__main__":  
    login=0

    Exit()
