from django.shortcuts import render

from django.db.models import Count
from django.db.models.functions import TruncMonth



from datetime import date, timedelta
from datetime import datetime
from itertools import chain

# https://kaiching.org/pydoing/py/python-library-datetime.html

from .models import Note
from .models import Wk
from .models import Work
from .models import Work2


def index(request):
    list = Note.objects.all()
    context = {'list': list}
    return render(request, 'note/index.html', context)

def ww(request):
    list = Wk.objects.all()
    context = {'list': list}
    return render(request, 'note/ww.html', context)

def ww2(request):
    list = Wk.objects.all()
    context = {'list': list}
    return render(request, 'note/ww2.html', context)


#表格 open quiz
def work(request):
    list = Work.objects.all()
    context = {'list': list}
    return render(request, 'note/work.html', context)

"""
    list1 = Work.objects.values('place', 'date1__year', 'date1__month').annotate(
        num_dates=Count('date1__month', distinct = True) , num_worker=Count('worker', distinct = True), worktimes=Count('id')).order_by('place')
    
    temp_p = Work.objects.order_by('place').values('place').distinct()
    dis_p = temp_p.values_list('place', flat=True).order_by('place')

    dis_m = {7,8,9}

    print("DEBUG ... ")
    for i in dis_p:
        
        for j in dis_m
    
            try x = d.filter(place=i, date1__month=j)


"""

#妹妹的實驗室：這個寫法可以應付多個不限定月份
def work3(request):

    #輸入想要的年份即可 Generate 整年的數據
    year = 2019
    list0={}    
    dis_p = Work.objects.values_list('place', flat=True).distinct().order_by('place')
    num_p = dis_p.count()
    dis_m = Work.objects.order_by('date1__month').values('date1__month').distinct()
    num_m = dis_m.count()
    
    for i in range(num_p):
        #現在只可支援連續的月份
        for j in range(num_m):

            #目前的寫法如果 place 超過 99 筆會有錯誤，到時候改成 *1000就可以了
            list0[i+100*j]={'place':dis_p[i], 'date1__year':year ,'date1__month':dis_m[j]['date1__month']}
            
    
    list0 = list0.values()

    list1 = Work.objects.values('place', 'date1__year', 'date1__month').annotate(
        num_dates=Count('date1__month', distinct = True) , num_worker=Count('worker', distinct = True), worktimes=Count('id')).order_by('place')
    
    firstdate = Work.objects.values('date1').order_by('date1').first()
    lastdate = Work.objects.values('date1').order_by('date1').last()

    for x in list0:

        list2 = list1.filter(place=x['place'],date1__month=x['date1__month'],date1__year=year)

        x['New_num_dates']=x['New_num_worker']=x['New_worktimes']=0
        

        if list2:
            x['New_num_dates']=list2[0]['num_dates']
            x['New_num_worker']=list2[0]['num_worker']
            x['New_worktimes']=list2[0]['worktimes']

    context = {'list': list0, 'dis_m':dis_m, 'year':year, 'firstdate':firstdate, 'lastdate':lastdate}
    return render(request, 'note/work3.html', context)




def init_ww(request):
    def getList():
        return Wk.objects.order_by('yr','num')
    def getCnt():
        return Wk.objects.count()
        
    # https://docs.djangoproject.com/en/2.2/intro/tutorial02/
    # list = Wk.objects.order_by('yr','num')
    list = getList()
    
    for x in list:
        x.delete()
 
    k1 = getCnt()
    
    d1='2018-12-31'
    date1 = datetime.strptime(d1, "%Y-%m-%d")
    date2 = date1 + timedelta(days=6) 
   
    for num in range(1,53):
        # print(num) # to ensure num is 1,2,3 ..., 52
        date2 = date1 + timedelta(days=6)
        
        x =Wk(yr=2019,num=num,date1=date1,date2=date2)
        x.save()
        
        date1 = date2 + timedelta(days=1)
        
    k2 = getCnt()
    
    user = request.user

    key={'k1':k1,'k2':k2}
    list = getList()
    context = {'user': user,'key': key,'list':list }
    return render(request, 'note/ww.html', context)



#成功版本
def work2(request):

    #不能解決算 m 的方式，因為他會是個<QuerySet [(7,), (8,), (9,)]>
    list_month = Work.objects.values_list('date1__month').distinct()
    for z in list_month: 
        z[0]
    print(list_month)

    list0 = Work.objects.values('place').annotate(
    num_dates=Count('date1', distinct = True) , num_worker=Count('worker', distinct = True), worktimes=Count('id'))



    for x in list0:
        for i in {7,8,9}:
            listi = Work.objects.filter(place=x['place'],date1__year=2019,date1__month=i).values('place').annotate(
            num_dates=Count('date1', distinct = True) , num_worker=Count('worker', distinct = True), worktimes=Count('id')).order_by('place')

            x[str(i)+'num_dates']=x[str(i)+'num_worker']=x[str(i)+'worktimes']=0

            #如果list1有值的话，就运行缩排那些指令。       
            if listi:
                x[str(i)+'num_dates']=listi[0]['num_dates']
                x[str(i)+'num_worker']=listi[0]['num_worker']
                x[str(i)+'worktimes']=listi[0]['worktimes']

    print(list0)
    list_keys = list0[0].keys()

    context = {'list': list0, 'month':list_month, 'keys':list_keys}
    return render(request, 'note/work2.html', context)

#迴圈版本

"""

def work2(request):

    list0 = Work.objects.values('place').annotate(
    num_dates=Count('date1', distinct = True) , num_worker=Count('worker', distinct = True), worktimes=Count('id'))

    list_month = {7,8,9}

    for x in list0:

        for i in list_month:
            listi = Work.objects.filter(place=x['place'],date1__year=2019,date1__month=i).values('place').annotate(
            num_dates=Count('date1', distinct = True) , num_worker=Count('worker', distinct = True), worktimes=Count('id'))

            x[str(i)+'num_dates']=x[str(i)+'num_worker']=x[str(i)+'worktimes']=0

       
            if listi:
                x[str(i)+'num_dates']=listi[0]['num_dates']
                x[str(i)+'num_worker']=listi[0]['num_worker']
                x[str(i)+'worktimes']=listi[0]['worktimes']

    list_keys = list0[0].keys()

    context = {'list': list0, 'month':list_month, 'keys':list_keys}
    return render(request, 'note/work2.html', context)
    """