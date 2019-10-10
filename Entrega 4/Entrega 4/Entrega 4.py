import psycopg2
import Ver_llamadas as v
import Manejar_campañas as m
import Manejar_supervisores as ms
import Evaluar_llamadas as e
import Manejar_agentes as ma

conn = psycopg2.connect(database="grupo5",user = "grupo5",host ="201.238.213.114", port ="54321", password ="0BMxCm")

cur = conn.cursor()

cur.execute("SELECT id_tennant,nombre FROM tennant")
rows = cur.fetchall()

cur.close()
conn.close()

tennants  = {}

for row in rows:
    print(row[0],row[1])
    tennants[row[0]] = row[1]




Main_Choices = {1:"Ver_llamadas()",2:"Evaluar_llamadas()",
                3:"Manejar_campañas()",4:"Manejar_tipificaciones()",
                5:"Manejar_agentes()",6:"Manejar_supervisores()",
                7:"Manejar_tennants()",8:"Exit  "}

def Ver_llamadas():
    def Ver_llamadas():
        v.ShowCallInfo(Login)
        
    def Agregar_llamada():
        v.InsertLlamada(Login)
        
    def Editar_llamada():
        v.EditCall(Login)
        
    def Eliminar_llamada():
        v.KillCall(Login)
    
    Ver = {1:"Ver_llamadas()",2:"Agregar_llamada()",
           3:"Editar_llamada()",4:"Eliminar_llamada()",5:"Exit  "}
    v.Connect()
    v.ShowCall(Login)
    while True:
        for key in Ver:
            print(key, Ver[key][:-2])
        print("\n")
        choice = input()
        try:
            if choice=="5":
                v.Exit()
                break
            eval(Ver[int(choice)][:])
            print("\n")
            
        except:
            print("Ingrese opción válida")
            print("\n")
        

    
def Evaluar_llamadas():
    def Agregar_calificacion():
        e.AgregarCalificacion(Login)
        
    def Editar_calificacion():
        e.EditarCalificacion(Login)
        
    def Eliminar_calificacion():
        e.EliminarCalificacion(Login)
        
    
    Ver = {1:"Agregar_calificacion()",2:"Editar_calificacion()",
           3:"Eliminar_calificacion()",4:"Exit  "}
    e.Connect()
    e.Mostrarllamadas(Login)
    while True:
        for key in Ver:
            print(key, Ver[key][:-2])
        print("\n")
        choice = input()
        try:
            if choice=="4":
                e.Exit()
                break
            eval(Ver[int(choice)][:])
            print("\n")
            
        except:
            print("Ingrese opción válida")
            print("\n")
    
def Manejar_campañas():
    def Agregar_campaña():
        m.Agregar_Campaña(Login)
        
    def Eliminar_campaña():
        m.Eliminar_campaña(Login)
        
    def Editar_campaña():
        m.Editar_Campaña(Login)
        
    
    Ver = {1:"Agregar_campaña()",2:"Eliminar_campaña()",
           3:"Editar_campaña()",4:"Exit  "}
    m.Connect()
    m.Show_Campaigns_Tennant(Login)
    while True:
        for key in Ver:
            print(key, Ver[key][:-2])
        print("\n")
        choice = input()
        try:
            if choice=="4":
                m.Exit()
                break
            eval(Ver[int(choice)][:])
            print("\n")
            
        except:
            print("Ingrese opción válida")
            print("\n")

def Manejar_tipificaciones():
    def Agregar_tipificacion():
        print("Función: Agregar_tipificacion")
        
    def Asociar_tipificacion():
        print("Función: Asociar_tipificacion")
        
    def Eliminar_tipificacion():
        print("Función: Eliminar_tipificacion")

    def Editar_tipificacion():
        print("Función: Editar_tipificacion")
        
    def Editar_asociacion():
        print("Función: Editar_asociacion")        
    
    Ver = {1:"Agregar_tipificacion()",2:"Asociar_tipificacion()",
           3:"Eliminar_tipificacion()",4:"Editar_tipificacion()",
           5:"Editar_asociacion()",6:"Exit  "}
    while True:
        for key in Ver:
            print(key, Ver[key][:-2])
        print("\n")
        choice = input()
        try:
            if choice=="6":
                break
            eval(Ver[int(choice)][:])
            print("\n")
            
        except:
            print("Ingrese opción válida")
            print("\n")


def Manejar_agentes():
    def Agregar_agente():
        ma.Agregar_Agente(Login)

    def Editar_informacion():
        ma.Edit_Information(Login)
        
    def Eliminar_agente():
        ma.Eliminar_Agente(Login)
        
    Manejar = {1:"Agregar_agente()",2:"Editar_informacion()",
               3:"Eliminar_agente()",4:"Exit  "}
    ma.Connect()
    ma.Show_Agentes(Login)
    while True:
        for key in Manejar:
            print(key, Manejar[key][:-2])
        choice = input()
        try:
            if choice == "4":
                ma.Exit()
                break
            eval(Manejar[int(choice)][:])
            print("\n")
        except:
            print("Ingrese una opción válida")
            print("\n")
            


def Manejar_supervisores():
    def Agregar_supervisor():
        ms.AgregarSupervisor(Login)

    def Editar_informacion():
        ms.EditarInformacion(Login)
        
    def Eliminar_supervisor():
        ms.EliminarSupervisor(Login)
        
    Manejar = {1:"Agregar_supervisor()",2:"Editar_informacion()",
               3:"Eliminar_supervisor()",4:"Exit  "}
    ms.Connect()
    ms.Mostrarsupervisor(Login)
    while True:
        for key in Manejar:
            print(key, Manejar[key][:-2])
        choice = input()
        try:
            if choice == "4":
                ms.Exit()
                break
            eval(Manejar[int(choice)][:])
            print("\n")
        except:
            print("Ingrese una opción válida")
            print("\n")
            
    
def Manejar_tennants():
    def Agregar_tennant():
        print("Función: Agregar_tennant")

    def Editar_informacion():
        print("Función: Editar_informacion")
        
    def Eliminar_tennant():
        print("Función: Eliminar_tennant")
        
    Manejar = {1:"Agregar_tennant()",2:"Editar_informacion()",
               3:"Eliminar_tennant()",4:"Exit  "}
    while True:
        for key in Manejar:
            print(key, Manejar[key][:-2])
        choice = input()
        try:
            if choice == "4":
                break
            eval(Manejar[int(choice)][:])
            print("\n")
        except:
            print("Ingrese una opción válida")
            print("\n")


#############################################  LOGIN
while True:
    choice = input("Ingrese un tennant: ")
    try:
        print(tennants[int(choice)])
        Login = int(choice)
        print("\n")
        break
    except:
        print("Ingrese opción válida")
        print("\n")

########################################### MAIN LOOP
while True:
    print("---------------------------------")
    print("Current Login session: "+ tennants[Login])
    print("---------------------------------")
    print("\n")
    for key in Main_Choices:
        print(key, Main_Choices[key][:-2])
    print("\n")
    choice = input("Ingrese una opción: ")
    try:
        if choice=="8":
            break
        eval(Main_Choices[int(choice)][:])
        print("\n")
        

    except:
        print("Ingrese opción válida")
        print("\n")
print("Adios!")



