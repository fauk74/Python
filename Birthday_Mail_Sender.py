import smtplib
import pandas as pd
import random
import datetime as dt
import json

friends=pd.read_csv("list_of_friends.csv")
# let's build a dictionary with name : month , day , mail
list=[]
diz={}
#print(friends)
#print(friends["Mail"])
#print(friends.columns)

dict_friends= friends.to_dict(orient="records")

with open("list_of_friends.json","w") as file:
    json.dump(dict_friends, file, indent=4)


#print(dict_friends[0]['Name'])

def check_friends(diz, data):
    """
    return a list of mails if the data matches with day and month

    """
    lista=[]
    for x in diz:
        mese=int(x['Month'])
        giorno=int(x['Day'])

        if mese == int(data.month) and giorno == int(data.day):
            lista.append( (x['Name'], x['Mail']))
    return (lista)


list_to_send= check_friends(dict_friends, dt.datetime.now())

print(list_to_send)

list_of_letters=["wishes1.txt","wishes2.txt","wishes3.txt"]


my_mail='renda.isabella2@gmail.com'
password='arianna10'

connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_mail, password=password)



for nome in list_to_send:
    model=random.choice(list_of_letters)

    with open(model) as file:
        msg=file.read()

    msg_new=msg.replace("[NAME]", nome[0])
    connection.sendmail(from_addr=my_mail, to_addrs=nome[1], msg=msg_new)
    print(nome[1], msg_new)

connection.close()
