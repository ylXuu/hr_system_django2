from django.shortcuts import render,redirect
from user.worker_func import find,view_today_attend,attend_am_in,attend_pm_in,attend_pm_off,attend_am_off,getWorker,getWorkerTrain,getAllTrain,search_award,search_salary,performance_all,sign_up_train,modifyPassword
from user.admin_func import admin_find,create_attend,search_not_attend,search_attend,all_history_attend_table,add_train,getAllWorkerIn,getAllWorkerOut,getAllAward,getAllSalary,getAllPerformance,getAllTrainWorker,deleteTrainWorker,find_attend_existed,deleteAttend,search_history_attend,search_history_not_attend,addWorkerIn,edit_worker_in,quit_worker_in,initial_password,searchByDepartment,searchById,searchByName,getName,modifySalary,addAward
import datetime

# Create your views here.
def login(request):
    if request.session.get('is_login',None):
        return redirect('/worker_index/')
    return render(request,'login.html',{'error':False})

def logout(request):
    if not request.session.get('is_login',None):
        return redirect('/worker_index/')
    request.session.flush()
    return redirect('/worker_index/')

def worker_index(request):
    if request.session.get('is_login',None):
        return render(request,'worker_index.html')
    if request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']
        name = find(id,password)
        if name:
            name = str(name)
            request.session['is_login'] = True
            request.session['user_id'] = id
            request.session['user_name'] = name[2:-3]
            return render(request,'worker_index.html',{'name':name})
        else:
            return render(request,'login.html',{"error":True})
    else:
        return render(request,'login.html',{"error":False})

def worker_attend(request):
    id = request.session.get('user_id')
    list = view_today_attend(id)
    return render(request,'worker_attend.html',{"form":list})

def am_in(request):
    time = datetime.datetime.now()
    if time.hour < 9 and time.hour >= 8: #可以签到
        id = request.session.get('user_id')
        attend_am_in(id)
        return render(request, 'attend_success.html')
    else:
        return render(request,'attend_error.html')

def am_off(request):
    time = datetime.datetime.now()
    if time.hour >= 11 and time.hour <= 12: #可以签到
        id = request.session.get('user_id')
        attend_am_off(id)
        return render(request, 'attend_success.html')
    else:
        return render(request,'attend_error.html')

def pm_in(request):
    time = datetime.datetime.now()
    if time.hour >= 13 and time.hour < 14: #可以签到
        id = request.session.get('user_id')
        attend_pm_in(id)
        return render(request, 'attend_success.html')
    else:
        return render(request,'attend_error.html')

def pm_off(request):
    time = datetime.datetime.now()
    if time.hour >= 18: #可以签到
        id = request.session.get('user_id')
        attend_pm_off(id)
        return render(request, 'attend_success.html')
    else:
        return render(request,'attend_error.html')



#--------员工界面：培训-----------------

def worker_train(request):
    id = request.session.get('user_id')
    form = getWorkerTrain(id)
    list1 = []#正在进行
    list2 = []#未开始
    list3 = []#已结束
    time_now = datetime.datetime.now().strftime('%Y-%m-%d')
    now = datetime.datetime.strptime(str(time_now),'%Y-%m-%d')#现在的时间：年-月-日
    for i in form:
        start = datetime.datetime.strptime(str(i[3]),'%Y-%m-%d')#开始时间
        end = datetime.datetime.strptime(str(i[4]),'%Y-%m-%d')#结束时间
        if now <= end and now >= start: #正在进行
            data = {'train_id': i[0], 'train_name': i[2], 'start_time': i[3], 'end_time': i[4], 'introduction': i[5]}
            list1.append(data)
        elif now < start: #未开始
            data = {'train_id': i[0], 'train_name': i[2], 'start_time': i[3], 'end_time': i[4], 'introduction': i[5]}
            list2.append(data)
        elif now > end:
            data = {'train_id': i[0], 'train_name': i[2], 'start_time': i[3], 'end_time': i[4], 'introduction': i[5]}
            list3.append(data)

    return render(request,'worker_train.html',{'form1':list1,'form2':list2,'form3':list3})

def worker_all_train(request):
    form = getAllTrain()
    list1 = []
    list2 = []
    list3 = []
    time_now = datetime.datetime.now().strftime('%Y-%m-%d')
    now = datetime.datetime.strptime(str(time_now), '%Y-%m-%d')
    for i in form:
        start = datetime.datetime.strptime(str(i[2]), '%Y-%m-%d')
        end = datetime.datetime.strptime(str(i[3]), '%Y-%m-%d')
        if now <= end and now >= start: #正在进行
            data = {'train_id': i[0], 'train_name': i[1], 'start_time': i[2], 'end_time': i[3], 'introduction': i[4]}
            list1.append(data)
        elif now < start: #未开始
            data = {'train_id': i[0], 'train_name': i[1], 'start_time': i[2], 'end_time': i[3], 'introduction': i[4]}
            list2.append(data)
        elif now > end: #已结束
            data = {'train_id': i[0], 'train_name': i[1], 'start_time': i[2], 'end_time': i[3], 'introduction': i[4]}
            list3.append(data)

    return render(request,'worker_all_train.html',{'form1':list1,'form2':list2,'form3':list3})


def sign_up(request,train_id):
    id = request.session.get('user_id')
    b = sign_up_train(train_id,id)
    if b == 0:
        return render(request,'sign_up_0.html')
    else:
        return render(request, 'sign_up_1.html')

#--------------------------------------



#-------------员工界面：工资与奖金----------

def worker_salary_award(request):
    id = request.session.get('user_id')
    salary = search_salary(id)
    form1 = []
    for i in salary:
        data = {'amount':i[1]}
        form1.append(data)

    award = search_award(id)
    form3 = []
    for i in award:
        data = {'amount':i[2],'type':i[3],'date':i[4],'remarks':i[5]}
        form3.append(data)

    return render(request,'worker_salary_award.html',{'form1':form1,'form3':form3})

#----------------------------------------


#----------------员工界面：绩效------------

def worker_performance(request):
    id = request.session.get('user_id')
    form = performance_all(id)
    list = []
    for i in form:
        data = {'date':i[2],'achievement':i[3],'capacity':i[4],'attitude':i[5],'score':i[6]}
        list.append(data)
    return render(request,'worker_performance.html',{'form':list})

def worker_performance_plan(request):
    return render(request,'worker_performance_plan.html')

#----------------------------------------------------------#

#-----------------员工：账号安全------------------------------

def worker_account_safe(request):
    return render(request,'worker_account_safe.html')

def worker_modify_password(request):
    if request.method == 'POST':
        password = request.POST['password']
        id = request.session.get('user_id')
        modifyPassword(id,password)
        return redirect('/worker_index/')
    else:
        return render(request,'worker_account_safe.html')


def admin_login(request):
    if request.session.get('is_login',None):
        return redirect('/admin_index/')
    return render(request,'admin_login.html',{'error':False})

def admin_index(request):
    if request.session.get('is_login',None):
        return render(request,'admin_index.html')
    if request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']
        name = admin_find(id,password)
        if name:
            name = str(name)
            request.session['is_login'] = True
            request.session['user_id'] = id
            request.session['user_name'] = name[2:-3]
            return render(request,'admin_index.html',{'name':name})
        else:
            return render(request,'admin_login.html',{"error":True})
    else:
        return render(request,'admin_login.html',{"error":False})




#-------------管理员界面：考勤----------------

def admin_create_attend(request):
    b = find_attend_existed()
    if b == True:
        return render(request,'admin_create_attend_1.html')
    else:
        return render(request, 'admin_create_attend.html')


def create_table(request):
    create_attend()
    return redirect('/admin_create_attend/')

def admin_today_attend(request):
    form11 = search_attend('am_in_time')
    list11 = []
    for i in form11:
        worker = getWorker(i[0])
        data = {'id':worker[0][0],'name':worker[0][2],'datetime':i[1]}
        list11.append(data)

    form12 = search_not_attend('am_in_time')
    list12 = []
    for i in form12:
        worker = getWorker(i[0])
        data = {'id':worker[0][0],'name':worker[0][2],'datetime':i[1]}
        list12.append(data)

    form21 = search_attend('am_off_time')
    list21 = []
    for i in form21:
        worker = getWorker(i[0])
        data = {'id':worker[0][0],'name':worker[0][2],'datetime':i[2]}
        list21.append(data)

    form22 = search_not_attend('am_off_time')
    list22 = []
    for i in form22:
        worker = getWorker(i[0])
        data = {'id':worker[0][0],'name':worker[0][2],'datetime':i[2]}
        list22.append(data)

    form31 = search_attend('pm_in_time')
    list31 = []
    for i in form31:
        worker = getWorker(i[0])
        data = {'id':worker[0][0],'name':worker[0][2],'datetime':i[3]}
        list31.append(data)

    form32 = search_not_attend('pm_in_time')
    list32 = []
    for i in form32:
        worker = getWorker(i[0])
        data = {'id':worker[0][0],'name':worker[0][2],'datetime':i[3]}
        list32.append(data)

    form41 = search_attend('pm_off_time')
    list41 = []
    for i in form41:
        worker = getWorker(i[0])
        data = {'id':worker[0][0],'name':worker[0][2],'datetime':i[4]}
        list41.append(data)

    form42 = search_not_attend('pm_off_time')
    list42 = []
    for i in form42:
        worker = getWorker(i[0])
        data = {'id':worker[0][0],'name':worker[0][2],'datetime':i[4]}
        list42.append(data)

    return render(request,'admin_today_attend.html',{'form_am_in':list11,'form_am_not_in':list12,'form_am_off':list21,'form_am_not_off':list22,'form_pm_in':list31,'form_pm_not_in':list32,'form_pm_off':list41,'form_pm_not_off':list42})


def admin_history_attend(request):
    form = all_history_attend_table()
    list = []
    for i in form:
        data = {'table_name':i[0]}
        list.append(data)
    return render(request,'admin_history_attend.html',{'form':list})

def admin_view_history(request,table_name):
    form11 = search_history_attend('am_in_time',table_name)
    list11 = []
    for i in form11:
        worker = getWorker(i[0])
        data = {'id':worker[0][0],'name':worker[0][2],'datetime':i[1]}
        list11.append(data)

    form12 = search_history_not_attend('am_in_time',table_name)
    list12 = []
    for i in form12:
        worker = getWorker(i[0])
        data = {'id':worker[0][0],'name':worker[0][2],'datetime':i[1]}
        list12.append(data)

    form21 = search_history_attend('am_off_time',table_name)
    list21 = []
    for i in form21:
        worker = getWorker(i[0])
        data = {'id':worker[0][0],'name':worker[0][2],'datetime':i[2]}
        list21.append(data)

    form22 = search_history_not_attend('am_off_time',table_name)
    list22 = []
    for i in form22:
        worker = getWorker(i[0])
        data = {'id':worker[0][0],'name':worker[0][2],'datetime':i[2]}
        list22.append(data)

    form31 = search_history_attend('pm_in_time',table_name)
    list31 = []
    for i in form31:
        worker = getWorker(i[0])
        data = {'id':worker[0][0],'name':worker[0][2],'datetime':i[3]}
        list31.append(data)

    form32 = search_history_not_attend('pm_in_time',table_name)
    list32 = []
    for i in form32:
        worker = getWorker(i[0])
        data = {'id':worker[0][0],'name':worker[0][2],'datetime':i[3]}
        list32.append(data)

    form41 = search_history_attend('pm_off_time',table_name)
    list41 = []
    for i in form41:
        worker = getWorker(i[0])
        data = {'id':worker[0][0],'name':worker[0][2],'datetime':i[4]}
        list41.append(data)

    form42 = search_history_not_attend('pm_off_time',table_name)
    list42 = []
    for i in form42:
        worker = getWorker(i[0])
        data = {'id':worker[0][0],'name':worker[0][2],'datetime':i[4]}
        list42.append(data)

    return render(request,'admin_view_history.html',{'form_am_in':list11,'form_am_not_in':list12,'form_am_off':list21,'form_am_not_off':list22,'form_pm_in':list31,'form_pm_not_in':list32,'form_pm_off':list41,'form_pm_not_off':list42})


def admin_delete_history(request,table_name):
    deleteAttend(table_name)
    return redirect('/admin_history_attend/')

#-------管理员界面：培训---------------------

def admin_train(request):
    form = getAllTrain()
    list = []
    for i in form:
        data = {'train_id':i[0],'train_name':i[1],'start_time':i[2],'end_time':i[3],'introduction':i[4]}
        list.append(data)
    return render(request,'admin_train.html',{'form':list})

def admin_create_train(request):
    if request.method == 'POST':
        train_id = request.POST['train_id']
        train_name = request.POST['train_name']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        introduction = request.POST['introduction']
        add_train(train_id,train_name,start_time,end_time,introduction)
        return render(request,'admin_create_train.html')
    else:
        return render(request,'admin_create_train.html')

def admin_view_train_worker(request,train_id):
    form = getAllTrainWorker(train_id)
    list = []
    for i in form:
        worker = getWorker(i[0])
        for j in worker:
            data = {'id':j[0],'name':j[2],'department':j[8],'duties':j[9]}
            list.append(data)

    return render(request,'admin_view_train_worker.html',{'form':list,'train_id':train_id})

def delete_train_worker(request,train_id,id):
    deleteTrainWorker(train_id,id)
    return redirect('/admin_train/')

#----------------------------------------



#------------管理员界面：员工管理---------------

def admin_worker_in(request):
    form = getAllWorkerIn()
    list = []
    for i in form:
        data = {'id': i[0], 'name': i[2], 'sex': i[3], 'age': i[4], 'email': i[5], 'telephone': i[6], 'entry_time': i[7], 'department': i[8], 'duties': i[9]}
        list.append(data)
    return render(request,'admin_worker_in.html',{'form':list})

def admin_worker_out(request):
    form = getAllWorkerOut()
    list = []
    for i in form:
        data = {'id': i[0], 'name': i[1], 'sex': i[2], 'age': i[3], 'email': i[4], 'telephone': i[5], 'entry_time': i[6], 'quit_time': i[7], 'quit_reason': i[8]}
        list.append(data)
    return render(request,'admin_worker_out.html',{'form':list})


def admin_add_worker(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        sex = request.POST['sex']
        age = request.POST['age']
        email = request.POST['email']
        telephone = request.POST['telephone']
        entry_time = request.POST['entry_time']
        department = request.POST['department']
        duties = request.POST['duties']
        addWorkerIn(id,name,sex,age,email,telephone,entry_time,department,duties)
        return render(request,'create_worker_1.html')
    else:
        return render(request,'add_new_worker.html')


def admin_edit_worker(request,id):
    worker = getWorker(id)
    list = []
    for i in worker:
        data = {'id': i[0], 'name': i[2], 'sex': i[3], 'age': i[4], 'email': i[5], 'telephone': i[6],
                'entry_time': i[7],
                'department': i[8], 'duties': i[9]}
        list.append(data)
    return render(request, 'edit_worker_in.html', {'form': list})

def admin_do_edit(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        sex = request.POST['sex']
        age = request.POST['age']
        email = request.POST['email']
        telephone = request.POST['telephone'];
        entry_time = request.POST['entry_time'];
        department = request.POST['department']
        duties = request.POST['duties']
        entry_time_1 = entry_time.replace('年','-')
        entry_time_2 = entry_time_1.replace('月','-')
        entry_time_3 = entry_time_2.replace('日','-')
        edit_worker_in(id,name,sex,age,email,telephone,entry_time_3,department,duties)
        return redirect('/admin_worker_in/')
    else:
        return render(request,'edit_worker_in.html')


def admin_quit_worker(request,id):
    worker = getWorker(id)
    list = []
    for i in worker:
        data = {'id': i[0], 'name': i[2], 'sex': i[3], 'age': i[4], 'email': i[5], 'telephone': i[6],
                'entry_time': i[7],
                'department': i[8], 'duties': i[9]}
        list.append(data)
    return render(request,'quit_worker_confirm.html',{'form':list})

def admin_do_quit(request):
    if request.method == 'POST':
        quit_reason = request.POST['quit_reason']
        id = request.POST['id']
        quit_worker_in(id,quit_reason)
        return redirect('/admin_worker_in/')
    else:
        return render(request, 'quit_worker_confirm.html')

def admin_initial_password(request,id):
    initial_password(id)
    return redirect('/admin_worker_in/')




def search_by_id(request):
    return render(request,'search_by_id.html')

def search_by_id_out(request):
    if request.method == 'POST':
        id = request.POST['id']
        worker = searchById(id)
        list = []
        for i in worker:
            data = {'id': i[0], 'name': i[2], 'sex': i[3], 'age': i[4], 'email': i[5], 'telephone': i[6],
                    'entry_time': i[7],
                    'department': i[8], 'duties': i[9]}
            list.append(data)
        return render(request,'search_out.html',{'form':list})
    else:
        return render(request,'search_by_id.html')

def search_by_name(request):
    return render(request,'search_by_name.html')

def search_by_name_out(request):
    if request.method == 'POST':
        name = request.POST['name']
        worker = searchByName(name)
        list = []
        for i in worker:
            data = {'id': i[0], 'name': i[2], 'sex': i[3], 'age': i[4], 'email': i[5], 'telephone': i[6],
                    'entry_time': i[7],
                    'department': i[8], 'duties': i[9]}
            list.append(data)
        return render(request,'search_out.html',{'form':list})
    else:
        return render(request,'search_by_name.html')

def search_by_department(request):
    return render(request,'search_by_department.html')

def search_by_department_out(request):
    if request.method == 'POST':
        department = request.POST['department']
        worker = searchByDepartment(department)
        list = []
        for i in worker:
            data = {'id': i[0], 'name': i[2], 'sex': i[3], 'age': i[4], 'email': i[5], 'telephone': i[6],
                    'entry_time': i[7],
                    'department': i[8], 'duties': i[9]}
            list.append(data)
        return render(request,'search_out.html',{'form':list})
    else:
        return render(request,'search_by_department.html')

#-----------------------------------------------

def admin_recruit(request):
    pass


#--------------管理员界面：工资奖金-------------------

def admin_salary(request):
    form1 = getAllSalary()
    list1 = []
    for i in form1:
        name = getName(i[0])
        for j in name:
            data = {'id': i[0], 'name': j[0], 'amount': i[1]}
            list1.append(data)

    return render(request,'admin_salary.html',{'form':list1})

def admin_award(request):
    form = getAllAward()
    list = []
    for i in form:
        data = {'id': i[0], 'name': i[1], 'amount': i[2],'type':i[3],'date':i[4],'remarks':i[5]}
        list.append(data)
    return render(request, 'admin_award.html', {'form': list})


def admin_modify_salary(request,id,amount):
    return render(request,'admin_modify_salary.html',{'id':id,'amount':amount})

def admin_do_modify(request):
    if request.method == 'POST':
        id = request.POST['id']
        amount = request.POST['amount']
        modifySalary(id,amount)
        return redirect('/admin_salary/')
    else:
        return render(request,'admin_modify_salary.html')

def admin_add_award(request):
    worker = getAllWorkerIn()
    list = []
    for i in worker:
        data = {'id': i[0]}
        list.append(data)
    return render(request,'admin_add_award.html',{'form':list})

def admin_do_add(request):
    if request.method == 'POST':
        id = request.POST['id']
        amount = request.POST['amount']
        type = request.POST['type']
        date = request.POST['date']
        remarks = request.POST['remarks']
        name = str(getName(id))

        addAward(id,name[3:-5],amount,type,date,remarks)
        return redirect('/admin_award/')
    else:
        worker = getAllWorkerIn()
        list = []
        for i in worker:
            data = {'id': i[0]}
            list.append(data)
        return render(request,'admin_add_award.html',{'form':list})


#-----------------------------------------------

def admin_performance(request):
    form = getAllPerformance()
    list = []
    for i in form:
        data = {'id':i[0],'name':i[1],'date':i[2],'achievement':i[3],'capacity':i[4],'attitude':i[5],'score':i[6]}
        list.append(data)
    return render(request,'admin_performance.html',{'form':list})

def admin_assessment(request):
    form = getAllWorkerIn()
    list = []
    for i in form:
        data = {'id':i[0],'name':i[2],'department':i[8],'duties':i[9]}
        list.append(data)
    return render(request,'admin_assessment.html',{'form':list})