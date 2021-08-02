from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon import functions, types
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError,UserIdInvalidError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import csv
import traceback
import time
import random
import re
from datetime import datetime
import tkinter as tk
from sqlalchemy import create_engine
engine = create_engine('sqlite:///database.db', echo=True)
connection = engine.connect()
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey,insert,update,delete,select,and_
metadata = MetaData()

acc = Table('acc',metadata,
            Column('name_acc',String),
            Column('api_id',String),
            Column('api_hash',String),
            Column('phone',String,primary_key=True))


Data = Table('data',metadata,Column('username',String),
                Column('user_id',String,primary_key=True),
                Column('access_hash',String),
                Column('name',String),
                Column('groups',String),
                Column('group_id',String))
buff = Table('buff',metadata,Column('user_id',String),Column('group_buffed_id',String))
def get_key():

    now = datetime.now()

    now = str(now).split(" ")
    key1 = "".join(now[0].split("-"))
    key2 = "".join(("".join(now[1].split(":")).split(".")))
    key = key2 + key1
    return key

def get_acc(phone):
    query = select([acc]).where(acc.columns.phone==phone)
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()
    ResultProxy.close()
    return ResultSet

def create_acc(api_id,api_hash,phone):
    name_acc= "acc"+str(get_key())
    if len(get_acc(phone)) == 0:
        new_acc = insert(acc).values(name_acc=name_acc,api_id=api_id, api_hash=api_hash, phone=phone)
        ResultProxy = connection.execute(new_acc)
        ResultProxy.close()
        return True
    return False



def author_acc(phone):
    acc = get_acc(phone)
    if len(acc) == 0:
        return False, False
    client = TelegramClient(acc[0][3], acc[0][1], acc[0][2])
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the code: '))
    return "Oke"


def check_acc(phone):
    acc = get_acc(phone)
    if len(acc) == 0:
        return False,False
    client = TelegramClient(acc[0][3],acc[0][1],acc[0][2])
    client.connect()
    if not client.is_user_authorized():
        return False,False
    return client,acc

def auto_join_group_with_username(client,name):
    result = client(functions.channels.JoinChannelRequest(
        channel=name
    ))
    return result.stringify()


def get_group_user(phone):
    last_date = None
    chunk_size = 200
    chats = []
    client,acc = check_acc(phone)
    if acc == False:
        return False
    groups = []

    result = client(GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=0
    ))
    chats.extend(result.chats)

    for chat in chats:
        try:
            if chat.megagroup == True:  # CONDITION TO ONLY LIST MEGA GROUPS.
                groups.append(chat)
        except:
            continue
    return client,groups

def get_all_user_from_groupID(client,group):
    query = delete(Data).where(Data.columns.group_id == group.id)
    ResultProxy = connection.execute(query)
    ResultProxy.close()
    all_user = []
    all_user = client.get_participants(group, aggressive=True)
    for user in all_user:
        if user.username:
            username = user.username
        else:
            username = ""
        if user.first_name:
            first_name = user.first_name
        else:
            first_name = ""
        if user.last_name:
            last_name = user.last_name
        else:
            last_name = ""
        name = (first_name + ' ' + last_name).strip()
        new_user = insert(Data).values(username=username,user_id=user.id,access_hash=user.access_hash,name=name,groups=group.title,group_id=group.id)
        ResultProxy = connection.execute(new_user)
        ResultProxy.close()
    return group.title


def add_users_to_group_by_Username(client,group_id_nguon,group_buff):
    query = select([Data]).where(Data.columns.group_id == group_id_nguon)
    ResultProxy = connection.execute(query)
    List_user = ResultProxy.fetchall()
    ResultProxy.close()
    if len(List_user) == 0:
        return "Không Tìm Thấy User"
    error_count = 0
    target_group_entity = InputPeerChannel(group_buff.id, group_buff.access_hash)
    for user in List_user:
        if user[0] == "":
            continue

        query = select([buff]).where(and_(buff.columns.user_id == user[1], buff.columns.group_buffed_id == group_buff.id))
        ResultProxy = connection.execute(query)
        user_buffed = ResultProxy.fetchall()
        ResultProxy.close()
        print(len(user_buffed))
        if len(user_buffed) != 0:
            continue
        try:
            user_to_add = client.get_input_entity(user[0])
            client(InviteToChannelRequest(target_group_entity, [user_to_add]))
            query = insert(buff).values(user_id=user[1], group_buffed_id=group_buff.id)
            ResultProxy = connection.execute(query)
            ResultProxy.close()
            print("Waiting 20 Seconds...")
            time.sleep(5)
        except UserPrivacyRestrictedError:
            query = insert(buff).values(user_id=user[1], group_buffed_id=group_buff.id)
            ResultProxy = connection.execute(query)
            ResultProxy.close()
            print("The user's privacy settings do not allow you to do this. Skipping.")
        except PeerFloodError:
            print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
        except:
                traceback.print_exc()
                print("Unexpected Error")
                error_count += 1
                if error_count > 100:
                    print("Loi qua nhieu")
                    return False
                continue

def add_users_to_group_by_Id(client,group_id_nguon,group_buff):
    query = select([Data]).where(Data.columns.group_id==group_id_nguon)
    ResultProxy = connection.execute(query)
    List_user = ResultProxy.fetchall()
    ResultProxy.close()
    if len(List_user) == 0:
        return "Không Tìm Thấy User"
    error_count = 0
    target_group_entity = InputPeerChannel(group_buff.id, group_buff.access_hash)
    for user in List_user:
        try:
            query = select([buff]).where(and_(buff.columns.user_id==user[1],buff.columns.group_buffed_id==group_buff.id))
            ResultProxy = connection.execute(query)
            user_buffed = ResultProxy.fetchall()
            print(user_buffed)
            ResultProxy.close()
            if len(user_buffed) != 0:
                continue
            user_to_add = InputPeerUser(int(user[1]), int(user[2]))
            client(InviteToChannelRequest(target_group_entity, [user_to_add]))
            query = insert(buff).values(user_id=user[1],group_buffed_id=group_buff.id)
            ResultProxy = connection.execute(query)
            ResultProxy.close()
            time.sleep(5)
        # try:
        #     target_group_entity = InputPeerChannel(group_buff.id, group_buff.access_hash)
        except UserPrivacyRestrictedError:
            query = insert(buff).values(user_id=user[1], group_buffed_id=group_buff.id)
            ResultProxy = connection.execute(query)
            ResultProxy.close()
            print("The user's privacy settings do not allow you to do this. Skipping.")
        except PeerFloodError:
            print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
        except:
                traceback.print_exc()
                print("Unexpected Error")
                error_count += 1
                if error_count > 100:
                    print("Loi qua nhieu")
                    exit(0)
                continue
        # except UserPrivacyRestrictedError:
        #     print("The user's privacy settings do not allow you to do this. Skipping.")
        # except:
        #         traceback.print_exc()
        #         print("Unexpected Error")
        #         error_count += 1
        #         if error_count > 100:
        #             print("Loi qua nhieu")
        #             exit(0)


def get_user(group_id):
    query = select([Data]).where(Data.columns.group_id == group_id)
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()
    ResultProxy.close()
    return ResultSet

if __name__ == '__main__':
    metadata.create_all(engine)
    query = select([acc])
    result = connection.execute(query)
    list_sdt = result.fetchall()
    result.close()
    for sdt in list_sdt:
        client, list_group = get_group_user(sdt[3])
        for group in list_group:
            if group.username == 'thongtinhangngay':
                check = add_users_to_group_by_Username(client,1420585883,group)
                if check == False:
                    continue
    # print(get_acc("+84877507820"))
    # print(get_acc("+84923131168"))
    # print(get_user('1420585883'))
    # client,list_group = get_group_user('+84706370139')
    # print(get_all_user_from_groupID(client,list_group[0]))

    # client, list_group = get_group_user('+84947425294')
    # print(list_group[0])
    # for i in list_group:
    #     print(i[3])
    print(add_users_to_group_by_Username(client,1420585883,list_group[0]))
    # print(create_acc('7776562','b1c5fdf74712aab590a8ed67cb257822','+84589354107'))
    # print(create_acc('7184095','88df02001d0ae1defdbd34f4a4108d12','+84784906948'))
    # print(author_acc('+84784906948'))

    # client,acc= check_acc('+84877507820')
    # print(get_group_user('+84877507820'))

# api_id = 7112836# YOUR API_ID
# api_hash = '36df55da53e23816ede094a4d527bc0c'  # YOUR API_HASH
# phone = '+84923131168'# YOUR PHONE NUMBER, INCLUDING COUNTRY CODE
# client = TelegramClient(phone, api_id, api_hash)
#
# client.connect()
# if not client.is_user_authorized():
#     client.send_code_request(phone)
#     client.sign_in(phone, input('Enter the code: '))
#
#
# def add_users_to_group():
#     input_file = 'test.csv'
#     users = []
#     with open(input_file, encoding='UTF-8') as f:
#         rows = csv.reader(f, delimiter=",", lineterminator="\n")
#         next(rows, None)
#         for row in rows:
#             user = {}
#             user['username'] = row[0]
#             try:
#                 user['id'] = int(row[1])
#                 user['access_hash'] = int(row[2])
#             except IndexError:
#                 print('users without id or access_hash')
#             users.append(user)
#
#     # random.shuffle(users)
#     chats = []
#     last_date = None
#     chunk_size = 10
#     groups = []
#
#     result = client(GetDialogsRequest(
#         offset_date=last_date,
#         offset_id=0,
#         offset_peer=InputPeerEmpty(),
#         limit=chunk_size,
#         hash=0
#     ))
#     chats.extend(result.chats)
#
#     for chat in chats:
#         try:
#             if chat.megagroup == True:  # CONDITION TO ONLY LIST MEGA GROUPS.
#                 groups.append(chat)
#         except:
#             continue
#
#     print('Choose a group to add members:')
#     i = 0
#     for group in groups:
#         print(str(i) + '- ' + group.title)
#         i += 1
#
#     g_index = input("Enter a Number: ")
#     target_group = groups[int(g_index)]
#     print('\n\nGrupo elegido:\t' + groups[int(g_index)].title)
#
#     target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)
#
#     mode = int(input("Enter 1 to add by username or 2 to add by ID: "))
#
#     error_count = 0
#
#     for user in users:
#         try:
#             print("Adding {}".format(user['username']))
#             if mode == 1:
#                 if user['username'] == "":
#                     continue
#                 user_to_add = client.get_input_entity(user['username'])
#             elif mode == 2:
#                 user_to_add = InputPeerUser(user['id'], user['access_hash'])
#             else:
#                 sys.exit("Invalid Mode Selected. Please Try Again.")
#             client(InviteToChannelRequest(target_group_entity, [user_to_add]))
#             print("Waiting 20 Seconds...")
#             time.sleep(20)
#         except PeerFloodError:
#             print("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
#         except UserPrivacyRestrictedError:
#             print("The user's privacy settings do not allow you to do this. Skipping.")
#         except:
#             traceback.print_exc()
#             print("Unexpected Error")
#             error_count += 1
#             if error_count > 1000:
#                 sys.exit('too many errors')
#             continue
#
#
# def list_users_in_group():
#     chats = []
#     last_date = None
#     chunk_size = 200
#     groups = []
#
#     result = client(GetDialogsRequest(
#         offset_date=last_date,
#         offset_id=0,
#         offset_peer=InputPeerEmpty(),
#         limit=chunk_size,
#         hash=0
#     ))
#     chats.extend(result.chats)
#
#     for chat in chats:
#         try:
#             print(chat)
#             groups.append(chat)
#             # if chat.megagroup== True:
#         except:
#             continue
#
#     print('Choose a group to scrape members from:')
#     i = 0
#     for g in groups:
#         print(str(i) + '- ' + g.title)
#         i += 1
#
#     g_index = input("Enter a Number: ")
#     target_group = groups[int(g_index)]
#
#     print('\n\nGrupo elegido:\t' + groups[int(g_index)].title)
#
#     print('Fetching Members...')
#     all_participants = []
#     all_participants = client.get_participants(target_group, aggressive=True)
#
#     print('Saving In file...')
#     with open("members-" + re.sub("-+", "-", re.sub("[^a-zA-Z]", "-", str.lower(target_group.title))) + ".csv", "w",
#               encoding='UTF-8') as f:
#         writer = csv.writer(f, delimiter=",", lineterminator="\n")
#         writer.writerow(['username', 'user id', 'access hash', 'name', 'group', 'group id'])
#         for user in all_participants:
#             if user.username:
#                 username = user.username
#             else:
#                 username = ""
#             if user.first_name:
#                 first_name = user.first_name
#             else:
#                 first_name = ""
#             if user.last_name:
#                 last_name = user.last_name
#             else:
#                 last_name = ""
#             name = (first_name + ' ' + last_name).strip()
#             writer.writerow([username, user.id, user.access_hash, name, target_group.title, target_group.id])
#     print('Members scraped successfully.')
#
#
# def printCSV():
#     input_file = 'test.csv'
#     users = []
#     with open(input_file, encoding='UTF-8') as f:
#         rows = csv.reader(f, delimiter=",", lineterminator="\n")
#         next(rows, None)
#         for row in rows:
#             user = {}
#             user['username'] = row[0]
#             user['id'] = int(row[1])
#             user['access_hash'] = int(row[2])
#             users.append(user)
#             print(row)
#             print(user)
#     sys.exit('FINITO')
#
#
# # print('Fetching Members...')
# # all_participants = []
# # all_participants = client.get_participants(target_group, aggressive=True)
# print('What do you want to do:')
# mode = int(input(
#     "Enter \n1-List users in a group\n2-Add users from CSV to Group (CSV must be passed as a parameter to the script\n3-Show CSV\n\nYour option:  "))
#
# if mode == 1:
#     list_users_in_group()
# elif mode == 2:
#     add_users_to_group()
# elif mode == 3:
#     printCSV()