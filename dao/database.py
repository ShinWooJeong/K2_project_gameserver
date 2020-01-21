#-*- coding:utf-8 -*-
import jsonify
import pymysql

def getConnection():
    return pymysql.connect(
        host='',
        port=3306,
        user='',
        password='',
        db='',
        charset=''
    )

def CheckLogin(_id,_pw):
    conn = getConnection()
    cursor = conn.cursor()
    sql = "SELECT * FROM `TBLuser` WHERE `id` = '%s' AND `pw` = '%s';" %(_id,_pw)
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result)>0:
        return result
    else:
        return 'n'

def CheckRegister(_id,_pw,_name):

    data = {
        "id" : True,
        "pw" : True,
        "name" : True
    }

    conn = getConnection()
    cursor = conn.cursor()
    sql = "SELECT * FROM `TBLuser` WHERE `id` = '%s'" %(_id)
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result)>0:
        data["id"] = False
    sql = "SELECT * FROM `TBLuser` WHERE `nickname` = '%s'" %(_name)
    cursor.execute(sql)
    result = cursor.fetchall()
    if len(result)>0:
        data["name"] = False

    if data["id"] == True and data["pw"] == True and data["name"] == True:
        sql = "INSERT INTO `TBLuser` (`id`,`pw`,`nickname`) VALUES('%s','%s','%s')" %(_id,_pw,_name)
        cursor.execute(sql)
        conn.commit()
        conn.close()
    return data

##이부분##
def GetDictionaryInfo(tablename):
    conn = getConnection()
    cursor = conn.cursor()
    sql = "SELECT * FROM `%s`" %(tablename)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

#불확실
def GetInputKeyTBLInfo(tablename,key_name,key):
    conn = getConnection()
    cursor = conn.cursor()
    sql = "SELECT * FROM `%s` WHERE `%s` = %d" %(tablename,key_name,key)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

#불확실
def UpdateTBL(tablename,update_key_name,update_key,user_key):
    conn = getConnection()
    cursor = conn.cursor()
    sql = "UPDATE `%s` SET `%s` = %d WHERE `user_key` = %d" %(tablename,update_key_name,update_key,user_key)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return 'success'

def UpdateSkinTBL(skin_key,skin_name,character_key):
    conn = getConnection()
    cursor = conn.cursor()
    sql = "UPDATE `TBLcharacter` SET `skin_key` = %d, `skin` = '%s' WHERE `character_key` = %d" %(skin_key,skin_name,character_key)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return 'success'