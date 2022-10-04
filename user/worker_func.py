import pymysql
import datetime
import hashlib

def hash_code(s,salt='hrsys'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()

def find(id,password):
    db = pymysql.connect(host='localhost',user='root',password='xyl1278157445',port=3306,db='hr')
    cursor = db.cursor()

    sql = "select name from worker_in where id = \'{id_value}\' and password = \'{password_value}\';".format(id_value=id,password_value=password)
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

def getWorker(id):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "select * from worker_in where id = \'{id_value}\';".format(id_value=id)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def view_today_attend(id):#查看该员工今日签到情况
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    time = datetime.datetime.now()
    s = (str)(time.year) + '_' + (str)(time.month) + '_' + (str)(time.day)

    sql = "select * from attendence_" + s + " where id = \'{id_value}\';".format(id_value=id)
    cursor.execute(sql)
    result = cursor.fetchall()
    data = {'am_in':None,'am_off':None,'pm_in':None,'pm_off':None}
    if result[0][1]: #am_in不为空
        data['am_in'] = (str)(result[0][1].hour) + ':' + (str)(result[0][1].minute) + ':' + (str)(result[0][1].second)
    if result[0][2]:
        data['am_off'] = (str)(result[0][2].hour) + ':' + (str)(result[0][2].minute) + ':' + (str)(result[0][2].second)
    if result[0][3]:
        data['pm_in'] = (str)(result[0][3].hour) + ':' + (str)(result[0][3].minute) + ':' + (str)(result[0][3].second)
    if result[0][4]:
        data['pm_off'] = (str)(result[0][4].hour) + ':' + (str)(result[0][4].minute) + ':' + (str)(result[0][4].second)

    return data

def attend_am_in(id):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    time = datetime.datetime.now()
    s1 = (str)(time.year) + '_' + (str)(time.month) + '_' + (str)(time.day)
    s2 = (str)(time.year) + '-' + (str)(time.month) + '-' + (str)(time.day) + ' ' + (str)(time.hour) + ':' + (str)(time.minute) + ':' + (str)(time.second)

    sql = "update attendence_" + s1 + " set am_in_time = \'{datetime_value}\' where id = \'{id_value}\';".format(datetime_value=s2,id_value=id)
    cursor.execute(sql)
    db.commit()

def attend_am_off(id):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    time = datetime.datetime.now()
    s1 = (str)(time.year) + '_' + (str)(time.month) + '_' + (str)(time.day)
    s2 = (str)(time.year) + '-' + (str)(time.month) + '-' + (str)(time.day) + ' ' + (str)(time.hour) + ':' + (str)(
        time.minute) + ':' + (str)(time.second)

    sql = "update attendence_" + s1 + " set am_off_time = \'{datetime_value}\' where id = \'{id_value}\';".format(datetime_value=s2,id_value=id)
    cursor.execute(sql)
    db.commit()


def attend_pm_in(id):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    time = datetime.datetime.now()
    s1 = (str)(time.year) + '_' + (str)(time.month) + '_' + (str)(time.day)
    s2 = (str)(time.year) + '-' + (str)(time.month) + '-' + (str)(time.day) + ' ' + (str)(time.hour) + ':' + (str)(
        time.minute) + ':' + (str)(time.second)

    sql = "update attendence_" + s1 + " set pm_in_time = \'{datetime_value}\' where id = \'{id_value}\';".format(datetime_value=s2,id_value=id)
    cursor.execute(sql)
    db.commit()


def attend_pm_off(id):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    time = datetime.datetime.now()
    s1 = (str)(time.year) + '_' + (str)(time.month) + '_' + (str)(time.day)
    s2 = (str)(time.year) + '-' + (str)(time.month) + '-' + (str)(time.day) + ' ' + (str)(time.hour) + ':' + (str)(
        time.minute) + ':' + (str)(time.second)

    sql = "update attendence_" + s1 + " set pm_off_time = \'{datetime_value}\' where id = \'{id_value}\';".format(datetime_value=s2,id_value=id)
    cursor.execute(sql)
    db.commit()


def getWorkerTrain(id):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "select * from train_worker natural join train_course where id = \'{id_value}\';".format(id_value=id)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def getAllTrain():
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "select * from train_course;"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def sign_up_train(train_id,id):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql1 = "select * from train_worker where train_id = \'{train_id_value}\' and id = \'{id_value}\';".format(train_id_value=train_id,id_value=id)
    cursor.execute(sql1)
    temp = cursor.fetchall()
    for i in temp:
        if i[0]:
            return 0 #已存在

    sql = "insert into train_worker(train_id,id) values (\'{train_id_value}\',\'{id_value}\');".format(train_id_value=train_id,id_value=id)
    cursor.execute(sql)
    db.commit()
    return 1


def search_salary(id):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "select * from salary where id = \'{id_value}\';".format(id_value=id)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def search_award(id):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "select * from award where id = \'{id_value}\';".format(id_value=id)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def search_ssf(id):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "select * from ssf where id = \'{id_value}\';".format(id_value=id)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def performance_all(id):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "select * from performance where id = \'{id_value}\';".format(id_value=id)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def modifyPassword(id,newPassword):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "update worker_in set password = \'{password_value}\' where id = \'{id_value}\';".format(password_value=newPassword[0:20],id_value=id)
    cursor.execute(sql)
    db.commit()