#Funcion para mostrar la cantidad de llemadas realizadas y recibidas por un tennant dado
def GraphRealizada(Login):
    ListTrue=[]
    ListFalse=[]
    cursor=connection.cursor()
    sentencia="select t.nombre ,count(case l.realizada when true then 1 else null end) realizadas,count(case l.realizada when false then 1 else null end) recibidas  from (llamadas l join agente a on l.id_agente=a.id_agente)join tennant t on t.id_tennant=a.id_tennant where t.id_tennant="+str(Login)+"group by t.nombre"
    cursor.execute(sentencia)
    rows=cursor.fetchall()
    for row in rows:
        name=row[0]
        ListTrue.append(int(row[1]))
        ListFalse.append(int(row[2]))
        
    width = 0.35  # the width of the bars
    
    fig, ax = plt.subplots()
    ax.bar(0, ListTrue, width, label='Realizada')
    ax.bar(1, ListFalse, width, label='Recibida')
    
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Frecuencia')
    ax.set_title('Llamadas realizadas/recibidas de '+str(name))
    ax.get_xaxis().set_ticks([])
    ax.legend(loc='upper center')
    
    fig.tight_layout()
    
    plt.show()

#Funcion para mostrar la cantidad de aprobaciones segun nota de un tennant
def GraphNotas(Login):
    List7=[]
    List6=[]
    List5=[]
    List4=[]
    List3=[]
    List2=[]
    List1=[]
    
    ListLabel=[7,6,5,4,3,2,1]
    cursor=connection.cursor()
    sentencia="select t.nombre, count(case ss.aprovado=7 when true then 1 else null end) Nota_7, count(case ss.aprovado=6 when true then 1 else null end) Nota_6, count(case ss.aprovado=5 when true then 1 else null end) Nota_5,count(case ss.aprovado=4 when true then 1 else null end) Nota_4, count(case ss.aprovado=3 when true then 1 else null end) Nota_3,count(case ss.aprovado=2 when true then 1 else null end) Nota_2, count(case ss.aprovado=1 when true then 1 else null end) Nota_1 from(supervision ss join supervisor s on ss.id_supervisor=s.id_supervisor) join tennant t on s.id_tennant=t.id_tennant  where t.id_tennant ="+str(Login)+" group by t.nombre"
    cursor.execute(sentencia)
    rows=cursor.fetchall()
    for row in rows:
        name=row[0]
        List7.append(int(row[1]))
        List6.append(int(row[2]))
        List5.append(int(row[3]))
        List4.append(int(row[4]))
        List3.append(int(row[5]))
        List2.append(int(row[6]))
        List1.append(int(row[7]))
        
    x = np.arange(len(ListLabel))  # the label locations
    width = 0.35  # the width of the bars
    
    fig, ax = plt.subplots()
    ax.bar(0, List7, width)
    ax.bar(1, List6, width)
    ax.bar(2, List5, width)
    ax.bar(3, List4, width)
    ax.bar(4, List3, width)
    ax.bar(5, List2, width)
    ax.bar(6, List1, width)
    
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Frecuencia')
    ax.set_title('Llamadas evaluadas de '+name)
    ax.set_xticks(x)
    ax.set_xticklabels(ListLabel)
    
    fig.tight_layout()
    
    plt.show()

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

#Mostrar la cantidad de llamadas por agente dado un agente y un rango de fechas
def GraphLlamadasPorAgente(Login):
    
    choiceAgente= ChoosedAgent(Login)
    minFecha=input("Ingrese el menor valor de su rango de fechas Ej: 2017-01-05 \n")
    maxFecha=input("Ingrese el mayor valor de su rango de fechas Ej: 2017-01-05 \n")
    ListCont=[]
    ListLabel=[]
    cursor=connection.cursor()
    sentencia="select l.fecha_llamada, count(*) from (llamadas l join agente a on l.id_agente=a.id_agente)join tennant t on t.id_tennant=a.id_tennant where t.id_tennant="+str(Login)+" and l.id_agente="+str(choiceAgente)+" and l.fecha_llamada>'"+str(minFecha)+"'and l.fecha_llamada<'"+str(maxFecha)+"' group by l.fecha_llamada"
    cursor.execute(sentencia)
    rows=cursor.fetchall()
    if len(rows)!=0:
        for row in rows:
            ListLabel.append(row[0])
            ListCont.append(row[1])
            
        x = np.arange(len(ListLabel))
        fig, ax = plt.subplots()
        plt.bar(x, ListCont)
        plt.title("Llamadas por fecha del agente "+str(choiceAgente))
        plt.ylabel("Frecuencia")
        plt.xticks(x,ListLabel,rotation='vertical')
        plt.show()
    else:
        print("No hay datos de este agente para las fechas dadas")


#Mostrar todas las llamadas supervisadas por dia de un tennant
def GraphRendimientoSupervisor(Login):
    ListCont=[]
    ListLabel=[]
    cursor=connection.cursor()
    sentencia="select l.fecha_llamada, count(case l.id_supervisor=null when true then null else 1 end) from (llamadas l join agente a on l.id_agente=a.id_agente) join tennant t on a.id_tennant=t.id_tennant where t.id_tennant="+str(Login)+" group by l.fecha_llamada order by l.fecha_llamada"
    cursor.execute(sentencia)
    rows=cursor.fetchall()
    if len(rows)!=0:
        for row in rows:
            ListLabel.append(row[0])
            ListCont.append(row[1])
            
        sentencia="select * from tennant where id_tennant="+str(Login)
        cursor.execute(sentencia)
        rows=cursor.fetchone()
        name=rows[1]
        x = np.arange(len(ListLabel))
        fig, ax = plt.subplots()
        fig.set_figwidth(14)
        plt.bar(x, ListCont)
        plt.title("Cantida de llamadas supervisadas de "+str(name))
        plt.ylabel("Frecuencia")
        plt.xticks(x,ListLabel,rotation='vertical')
        plt.tight_layout()
        plt.show()
    else:
        print("No hay datos de este agente para las fechas dadas")

import psycopg2
import matplotlib.pyplot as plt
import numpy as np
    
def Connect():
    global connection
    connection=psycopg2.connect(host="201.238.213.114",user="grupo5",password="0BMxCm",database="grupo5",port="54321") 

def Exit():
    connection.close()

 
if __name__ == "__main__":  
    Connect()
    login=0
    GraphRealizada(login)
    #GraphNotas(login)
    #GraphLlamadasPorAgente(login)
    #GraphRendimientoSupervisor(login)
    Exit()
