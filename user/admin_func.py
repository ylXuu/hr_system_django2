import datetime
import pymysql

def admin_find(id,password):
    db = pymysql.connect(host='localhost',user='root',password='xyl1278157445',port=3306,db='hr')
    cursor = db.cursor()

    sql = "select name from user_administrator where account_id = \'{id_value}\' and password = \'{password_value}\';".format(id_value=id,password_value=password)
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

def find_attend_existed():
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    time = datetime.datetime.now()
    s1 = (str)(time.year) + '_' + (str)(time.month) + '_' + (str)(time.day)

    sql = "select TABLE_NAME from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA = 'hr' and TABLE_NAME = 'attendence_" + s1 + "';"
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        return True
    else:
        return False

def create_attend():
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    time = datetime.datetime.now()
    s1 = (str)(time.year) + '_' + (str)(time.month) + '_' + (str)(time.day)

    sql = "create table attendence_" + s1 + " (id varchar(10) not null primary key,am_in_time datetime,am_off_time datetime,pm_in_time datetime,pm_off_time datetime);"
    cursor.execute(sql)

    sql1 = "select id from worker_in;"
    cursor.execute(sql1)
    form = cursor.fetchall()
    for i in form:
        sql2 = "insert into attendence_" + s1 + "(id,am_in_time,am_off_time,pm_in_time,pm_off_time) values (\'{id_value}\',null,null,null,null);".format(id_value=i[0])
        cursor.execute(sql2)

    db.commit()
    s2 = (str)(time.year) + '-' + (str)(time.month) + '-' + (str)(time.day)
    return s2


def search_attend(s):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    time = datetime.datetime.now()
    s1 = (str)(time.year) + '_' + (str)(time.month) + '_' + (str)(time.day)

    sql = "select * from attendence_" + s1 + " where " + s + " is not null;"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def search_not_attend(s):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    time = datetime.datetime.now()
    s1 = (str)(time.year) + '_' + (str)(time.month) + '_' + (str)(time.day)

    sql = "select * from attendence_" + s1 + " where " + s + " is null;"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def all_history_attend_table():
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "select table_name from information_schema.tables where table_schema = 'hr' and table_name like '%attendence_%';"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def add_train(train_id,train_name,start_time,end_time,introduction):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "insert into train_course(train_id,train_name,start_time,end_time,introduction) values (\'{id_value}\',\'{name_value}\',\'{start_value}\',\'{end_value}\',\'{intro_value}\')".format(id_value=train_id,name_value=train_name,start_value=start_time,end_value=end_time,intro_value=introduction)
    cursor.execute(sql)
    db.commit()


def getAllWorkerIn():
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "select * from worker_in;"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def getAllWorkerOut():
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "select * from worker_out;"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def getAllSalary():
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "select * from salary;"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def getAllAward():
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "select * from award"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def getAllPerformance():
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "select * from performance;"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def getAllTrainWorker(train_id):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "select id from train_worker where train_id = \'{id_value}\';".format(id_value=train_id)
    cursor.execute(sql)
    worker = cursor.fetchall()
    return worker

def deleteTrainWorker(train_id,id):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "delete from train_worker where train_id = \'{train_id_value}\' and id = \'{id_value}\'".format(train_id_value=train_id,id_value=id)
    cursor.execute(sql)
    db.commit()


def deleteAttend(table_name):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    #sql = "drop table \'{table_value}\';".format(table_value=table_name)
    sql = "drop table " + table_name + ";"

    cursor.execute(sql)
    db.commit()

def search_history_attend(s,table_name):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "select * from " + table_name + " where " + s + " is not null;"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def search_history_not_attend(s,table_name):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "select * from " + table_name + " where " + s + " is null;"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def addWorkerIn(id,name,sex,age,email,telephone,entry_time,department,duties):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "insert into worker_in(id,password,name,sex,age,email,telephone,entry_time,department,duties) values (\'{id_value}\','88888888',\'{name_value}\',\'{sex_value}\',\'{age_value}\',\'{email_value}\',\'{telephone_value}\',\'{entry_time_value}\',\'{department_value}\',\'{duties_value}\');".format(id_value=id,name_value=name,sex_value=sex,age_value=age,email_value=email,telephone_value=telephone,entry_time_value=entry_time,department_value=department,duties_value=duties)

    cursor.execute(sql)

    sql2 = "insert into salary(id,amount) values (\'{id_value}\',0);".format(id_value=id)
    cursor.execute(sql2)
    db.commit()


def edit_worker_in(id,name,sex,age,email,telephone,entry_time,department,duties):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = 'update worker_in set id = \'{id_value}\', name = \'{name_value}\', sex = \'{sex_value}\', age = \'{age_value}\', email = \'{email_value}\', telephone = \'{telephone_value}\', entry_time = \'{entry_time_value}\' , department = \'{department_value}\', duties = \'{duties_value}\' where id = \'{id_value}\''.format(id_value=id,name_value=name,sex_value=sex,age_value=age,email_value=email,telephone_value=telephone,entry_time_value=entry_time,department_value=department,duties_value=duties)
    cursor.execute(sql)
    db.commit()



def quit_worker_in(id,quit_reason):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "select id,name,sex,age,email,telephone,entry_time from worker_in where id = \'{id_value}\'".format(id_value=id)
    cursor.execute(sql)
    worker = cursor.fetchall()
    time = datetime.datetime.now().strftime('%Y-%m-%d')
    for i in worker:
        sql1 = "insert into worker_out(id,name,sex,age,email,telephone,entry_time,quit_time,quit_reason) values (\'{id_value}\',\'{name_value}\',\'{sex_value}\',\'{age_value}\',\'{email_value}\',\'{telephone_value}\',\'{entry_time_value}\',\'{quit_time_value}\',\'{quit_reason_value}\')".format(id_value=id,name_value=i[1],sex_value=i[2],age_value=i[3],email_value=i[4],telephone_value=i[5],entry_time_value=i[6],quit_time_value=time,quit_reason_value=quit_reason)
        cursor.execute(sql1)

    sql2 = "delete from worker_in where id = \'{id_value}\';".format(id_value=id)
    cursor.execute(sql2)

    sql3 = "delete from salary where id = \'{id_value}\';".format(id_value=id)
    cursor.execute(sql3)
    db.commit()


def initial_password(id):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "update worker_in set password = '88888888' where id = \'{id_value}\';".format(id_value=id)
    cursor.execute(sql)
    db.commit()

def delete_worker_out(id):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "delete from worker_out where id = \'{id_value}\';".format(id_value=id)
    cursor.execute(sql)
    db.commit()

def searchById(id):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "select * from worker_in where id = \'{id_value}\';".format(id_value=id)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def searchByName(name):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "select * from worker_in where name = \'{name_value}\';".format(name_value=name)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def searchByDepartment(department):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "select * from worker_in where department = \'{department_value}\';".format(department_value=department)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def getName(id):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "select name from worker_in where id = \'{id_value}\';".format(id_value=id)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def modifySalary(id,new):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "update salary set amount = \'{amount_value}\' where id = \'{id_value}\';".format(amount_value=new,id_value=id)
    cursor.execute(sql)
    db.commit()

def addAward(id,name,amount,type,date,remarks):
    db = pymysql.connect(host='localhost', user='root', password='xyl1278157445', port=3306, db='hr')
    cursor = db.cursor()

    sql = "insert into award(id,name,amount,type,date,remarks) values (\'{id_value}\',\'{name_value}\',\'{amount_value}\',\'{type_value}\',\'{date_value}\',\'{remarks_value}\');".format(id_value=id,name_value=name,amount_value=amount,type_value=type,date_value=date,remarks_value=remarks)
    cursor.execute(sql)
    db.commit()