from pyrogram import Client

api_id = 16526653
api_hash = "918872691e0a8ea8335cce787546eb3d"
tg = Client("84922511526", api_id=api_id, api_hash=api_hash)#app.send_message('@viktortanchik','hi')

tg.start()
#tg.send_message('@viktortanchik','ты гей?')



contacts =[]  # создаём список контактов

def zbor_contact():

    len_contact= input('skolko kotntaktov?')
    for b in range (int(len_contact)):
        contact = input ('vvedite contact')
        contacts.append(contact)

zbor_contact() # Вызываем функцию


for c in contacts:
    mess='добрый день \nв наличии есть: \nпшеничная 10\n ячневая 10\n'
    tg.send_message(c,mess)
    print(c)
