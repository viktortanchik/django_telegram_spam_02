import time
from pyrogram import Client, filters
import asyncio
###########################################
import datetime as dt

from scheduler import Scheduler
#from scheduler.asyncio import Scheduler

from scheduler.trigger import Monday, Tuesday
import time
from threading import Thread


#############################################


# async def main():
#     async with Client("6283834705843", api_id, api_hash) as app:
#         await app.send_message("674868256", "Greetings from **Pyrogram**!")
#

#asyncio.run(main())

'''
def handle_uploaded_file(f):
    with open('/home/viktor/PycharmProjects/Spam_TG_Django/django_telegram_spam/media/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
handle_uploaded_file(request.FILES['file'])



'''



def tel():
    api_id = 13729328
    api_hash = "9344d5d46317f096d8bde457e1a9bf53"
    app = Client("6283834705843", api_id=api_id, api_hash=api_hash)
    app.connect()
    #time.sleep(2)
    #app.send_message("674868256", str(text))
    app.send_message("674868256", 'TEST')



async def telega_text(text,phon,username):
    api_id = 16526653
    api_hash = "918872691e0a8ea8335cce787546eb3d"
    phone='84922511526'
    #84922511526
    if phon=='0':
        phone='6285776362281'

    if phon=='1':
        phone='84922511526'

    if phon=='2':
        phone='6285298448807'
    print(f'phon>>>{phon}   phone>>{phone}')

    app = Client(phone, api_id=api_id, api_hash=api_hash)
    try:
        await app.start()
        #await app.send_melsssage("674868256", str(text))
        print('SEND_TEXT')
        await app.send_message(username, str(text))
        await app.stop()
    except KeyError as er:
        print("Error>> ", er)
        # async with Client("6283834705843", api_id, api_hash) as app:
    #     await app.send_message("674868256", str(text))


async def telega_img(text,phon,username,img_name):
    api_id = 16526653
    api_hash = "918872691e0a8ea8335cce787546eb3d"
    phone='84922511526'
    #84922511526
    if phon=='0':
        phone='6285776362281'

    if phon=='1':
        phone='84922511526'

    if phon=='2':
        phone='6285298448807'
    print(f'phon>>>{phon}   phone>>{phone}')

    try:
        app = Client(phone, api_id=api_id, api_hash=api_hash)
        await app.start()
        #await app.send_melsssage("674868256", str(text))
        #await app.send_message(username, str(text))
        print(f'img_name--->{img_name}')
        await app.send_photo(chat_id=username,photo=img_name,caption=text)
        await app.stop()
    except KeyError as er:
        print("Error>> ", er)
        # async with Client("6283834705843", api_id, api_hash) as app:
    #     await app.send_message("674868256", str(text))


def foo_img(text_test,phon,username,img_name):
    asyncio.run(telega_img(text_test,phon,username,img_name))


async def main_Scheduler_img(tepm_date,text,phon,username,img_name):
    schedule = Scheduler()
    # loop = asyncio.get_running_loop()
    # schedule = Scheduler(loop=loop)

    flag = True
    temp_data = {'text_test': text,
                 'phon': phon,
                 'username': username,
                 'img_name':img_name
                 }
    j1 = schedule.once(dt.datetime.strptime(tepm_date, '%Y-%m-%d %H:%M'), foo_img, kwargs=temp_data)
    # asyncio.run(main())

    while flag:
        schedule.exec_jobs()
        print(schedule)
        print(f'j1>>>{j1.attempts}')
        print(dt.datetime)
        if j1.attempts == 1:
            flag = False
        time.sleep(10)

    print('END')

def start_Scheduler_img(tepm_date,text,phon,username,img_name):
    asyncio.run(main_Scheduler_img(tepm_date,text,phon,username,img_name))
############################################################################################
def foo_text(text_test,phon,username):
    asyncio.run(telega_text(text_test,phon,username))


async def main_Scheduler_text(tepm_date,text,phon,username):
    schedule = Scheduler()
    # loop = asyncio.get_running_loop()
    # schedule = Scheduler(loop=loop)

    flag = True
    temp_data = {'text_test': text,
                 'phon': phon,
                 'username': username
                 }
    j1 = schedule.once(dt.datetime.strptime(tepm_date, '%Y-%m-%d %H:%M'), foo_text, kwargs=temp_data)
    # asyncio.run(main())

    while flag:
        schedule.exec_jobs()
        print(schedule)
        print(f'j1>>>{j1.attempts}')
        print(dt.datetime)
        if j1.attempts == 1:
            flag = False
        time.sleep(10)

    print('END')

def start_Scheduler_text(tepm_date,text,phon,username,img_name):
    asyncio.run(main_Scheduler_text(tepm_date,text,phon,username,img_name))

#telega('TEST')

#asyncio.run(telega('TEST'))
