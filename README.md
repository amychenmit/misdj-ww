# ww課程開始 #
課程：https://github.com/twoutlook/misdj-ww-steps

# 10/12 #
## Homework
- What is a bash script? 
    - 如何可以更節省，目前發現有三種方式可以叫出 script. 10/13 可以用 ./go.sh 跑 go 三步驟！
- What's the different between 'Git clone' and 'download zip file directly'?
- 理解的是 def init_ww(request) 是怎麼做到的，關掉後才能正常刪減東西，打開後又全部更新好了！
- 可以讀 SHELL 了 https://docs.djangoproject.com/en/2.2/intro/tutorial02/

## Open book quiz
- Table

![image](https://github.com/amychenmit/misdj-ww/blob/master/H1.png)



# Challenge Action Reminder

- 進階：每個值之間應該是 ManyToMany 的關係，這樣才可以反查


Challange
# By 週會用到
Departure_Date.objects.filter(date_from__year__gte=year,
                              date_from__month__gte=month,
                              date_to__year__lte=year,
                              date_to__month__lte=month)

Alternative method using .extra:

where = '%(year)s >= YEAR(date_from) AND %(month)s >= MONTH(date_from) \
        AND %(year)s <= YEAR(date_to) AND %(month)s <= MONTH(date_to)' % \
        {'year': year, 'month': month}
Departure_Date.objects.extra(where=[where])

https://stackoverflow.com/questions/14077799/django-filter-by-specified-month-and-year-in-date-range


#如果不丟零進去呢？

def work2(request):

    #整個季度

    list0 = Work.objects.values('place').annotate(
        num_dates=Count('date1', distinct = True) , num_worker=Count('worker', distinct = True), worktimes=Count('id'))
    
    
    print("DEBUG ... ")
    for x in list0:

        print("x in list0 ... ")
        print(x)

        #整個季度分成七月、八月、九月

        list1 = Work.objects.filter(place=x['place'],date1__year=2019,date1__month=7).values('place').annotate(
        num_dates=Count('date1', distinct = True) , num_worker=Count('worker', distinct = True), worktimes=Count('id'))

        list2 = Work.objects.filter(place=x['place'],date1__year=2019,date1__month=8).values('place').annotate(
        num_dates=Count('date1', distinct = True) , num_worker=Count('worker', distinct = True), worktimes=Count('id'))

        list3 = Work.objects.filter(place=x['place'],date1__year=2019,date1__month=9).values('place').annotate(
        num_dates=Count('date1', distinct = True) , num_worker=Count('worker', distinct = True), worktimes=Count('id'))

        #增加七月、八月、九月的三個值為 0 

        #這個 if 令我百思不解，把list1[0]['xx']的值取代掉 0 的值（如果有的話） 
        if list1:
            x['m1num_dates']=list1[0]['num_dates']
            x['m1num_worker']=list1[0]['num_worker']
            x['m1worktimes']=list1[0]['worktimes']

        if list2:
            x['m2num_dates']=list2[0]['num_dates']
            x['m2num_worker']=list2[0]['num_worker']
            x['m2worktimes']=list2[0]['worktimes']

        if list3:
            x['m3num_dates']=list3[0]['num_dates']
            x['m3num_worker']=list3[0]['num_worker']
            x['m3worktimes']=list3[0]['worktimes']
    
        print("final x")
        print(x)
    context = {'list': list0 }
    return render(request, 'note/work2.html', context)


#這裡就有許多可以優化的, 通常就是把重覆的寫成 , def xx(yy):

#爸爸的7月

def work2(request):

    list1 = Work.objects.values('place').annotate(
        num_dates=Count('date1', distinct = True) , num_worker=Count('worker', distinct = True), worktimes=Count('id'))
    
    print("DEBUG ... ")
    for x in list1:
        list2 = Work.objects.filter(place=x['place'],date1__year=2019,date1__month=7).values('place').annotate(
        num_dates=Count('date1', distinct = True) , num_worker=Count('worker', distinct = True), worktimes=Count('id'))

        x['m1num_dates']=x['m1num_worker']=x['m1worktimes']=0
        if list2:
            x['m1num_dates']=list2[0]['num_dates']
            x['m1num_worker']=list2[0]['num_worker']
            x['m1worktimes']=list2[0]['worktimes']

    print(x)

    context = {'list': list1 }
    return render(request, 'note/work2.html', context)"""


#爸爸的7月延伸，硬寫8、9月
"""
def work2(request):

    #整個季度

    list0 = Work.objects.values('place').annotate(
        num_dates=Count('date1', distinct = True) , num_worker=Count('worker', distinct = True), worktimes=Count('id'))
    
    
    print("DEBUG ... ")
    for x in list0:

        print("x in list0 ... ")
        print(x)

        #整個季度分成七月、八月、九月

        list1 = Work.objects.filter(place=x['place'],date1__year=2019,date1__month=7).values('place').annotate(
        num_dates=Count('date1', distinct = True) , num_worker=Count('worker', distinct = True), worktimes=Count('id'))

        list2 = Work.objects.filter(place=x['place'],date1__year=2019,date1__month=8).values('place').annotate(
        num_dates=Count('date1', distinct = True) , num_worker=Count('worker', distinct = True), worktimes=Count('id'))

        list3 = Work.objects.filter(place=x['place'],date1__year=2019,date1__month=9).values('place').annotate(
        num_dates=Count('date1', distinct = True) , num_worker=Count('worker', distinct = True), worktimes=Count('id'))

        #增加七月、八月、九月的三個值為 0 
        x['m1num_dates']=x['m1num_worker']=x['m1worktimes']=0
        x['m2num_dates']=x['m2num_worker']=x['m2worktimes']=0
        x['m3num_dates']=x['m3num_worker']=x['m3worktimes']=0

        print("x add 0 ... ")
        print(x)

        #這個 if 令我百思不解，把list1[0]['xx']的值取代掉 0 的值（如果有的話） 
        if list1:
            x['m1num_dates']=list1[0]['num_dates']
            x['m1num_worker']=list1[0]['num_worker']
            x['m1worktimes']=list1[0]['worktimes']

        if list2:
            x['m2num_dates']=list2[0]['num_dates']
            x['m2num_worker']=list2[0]['num_worker']
            x['m2worktimes']=list2[0]['worktimes']

        if list3:
            x['m3num_dates']=list3[0]['num_dates']
            x['m3num_worker']=list3[0]['num_worker']
            x['m3worktimes']=list3[0]['worktimes']
    
        print("final x")
        print(x)
    context = {'list': list0 }
    return render(request, 'note/work2.html', context)"""


#妹妹的實驗室

"""def work2(request):

    list1 = Work.objects.values('place', 'date1__year', 'date1__month').annotate(
        num_dates=Count('date1__month', distinct = True) , num_worker=Count('worker', distinct = True), worktimes=Count('id')).order_by('place')
    
    print("DEBUG ... ")
    for x in list1:
        print(x)
    
    context = {'list': list1 }
    return render(request, 'note/work2.html', context)"""

#妹妹的實驗室2

"""def work2(request):

    list1 = Work.objects.values('place', 'date1__year', 'date1__month').annotate(
        num_dates=Count('date1__month', distinct = True) , num_worker=Count('worker', distinct = True), worktimes=Count('id')).order_by('place')
    
    temp_p = Work.objects.order_by('place').values('place').distinct()
    dis_p = temp_p.values_list('place', flat=True).order_by('place')

    dis_m = {7,8,9}

    print("DEBUG ... ")
    for i in dis_p:
        
        for j in dis_m
    
            try x = d.filter(place=i, date1__month=j)

            e


    context = {'list': list1 }
    return render(request, 'note/work2.html', context)"""



    # 'dict_test':dict_test,'e1':e1,'d':d,'b':b,'a':a, 'dis_p':dis_p, 'dis_t':dis_t

    
"""    #括號能幹嘛啦
    def getCnt():
        return Work.objects.count()

    #變成def dis_list = Work.objects.order_by('place').values('place','thing').distinct()




    list = Work.objects.order_by('place').values()

    

    #以下是測試資料區



    a = Work.objects.values('place','date1')
    #   .annotate(num_dates=Count('date1', distinct = True))
    #    .annotate(num_worker=Count('worker', distinct = True))
    #    .annotate(worktimes=Count('id'))

         

     
    #10/18 最新進度
    #分月份：七、八、九月
    d = Work.objects.values('place', 'date1__year', 'date1__month').annotate(num_dates=Count('date1__month', distinct = True) , num_worker=Count('worker', distinct = True), worktimes=Count('id')).order_by('place')

    #想要把他依照place分成多個子群
    dis_p = Work.objects.order_by('place').values('place').distinct()
    dis_t = dis_p.values_list('place', flat=True).order_by('place')
    e1 = [d.filter(place='3園'),d.filter(place='17園'),d.filter(place='112園')]
  
    #要找表達空集合的方式{}
    dict_test = {}
    for i in dis_t:
        dict_test[i] = d.filter(place=i)
    print(dict_test)
        #{} = d.filter(place= i )
        #結果子集合變成一個值



    #a = Work.objects.values('date1','place','thing').annotate(Count('worker'))
    #c = dis_list.filter(place='112園').count()
    #c = dis_list.values('place')
    #測試 loop 的效果
    #for x in dis_list:
    #    d = filter(place='x.place').count()"""