from django.shortcuts import render
from django.http import JsonResponse,response
from django.core import serializers
import sys
from .models import Skladnik
from .forms import VitAForm,VitEForm,HydrokortyzonForm
from .models import roboczareceptura
from .algorytmy import Przeliczanie

forms={'witamina A':VitAForm,'witamina E':VitEForm,'Hydrokortyzon': HydrokortyzonForm}
data={'witamina A':[['jednostka_z_recepty','opakowania','gramy','jednostki'],'ilosc_na_recepcie',['producent','Hasco 4500j.m./ml','Medana 50000j.m./ml'],],'witamina E':['opakowania','gramy','jednostki',['producent','Hasco 0,3g/ml']],'Hydrokortyzon':['gramy','aa'],'Metronidazol':['gramy','aa'],}
def home (request):
    skladniki = roboczareceptura.objects.all()
    t = []
    for i in skladniki:
        t.append(i.skladnik)
    datax = serializers.serialize("python", roboczareceptura.objects.all())


    #print('datax', datax)
    #sys.stdout.flush()
    return render(request,'home.html',{'tabela2':datax})

def formJson (request,skl):

    #form=forms[skl]
    datadict=data[skl]

    context={ 'datadict':datadict}
    return JsonResponse(context)


def dodajsklJson (request):
    if request.is_ajax():
        dodanySkladnik=request.POST.get("skladnik")

        roboczareceptura.objects.create(skladnik=dodanySkladnik,)
        ostatniskl = roboczareceptura.objects.last()
        to_updade={'skladnik' :ostatniskl.skladnik}

        for i in data[dodanySkladnik]:
            if type(i)!=list:
                a=request.POST.get(str(i))
                #print('i', i)
                sys.stdout.flush()
                #print('a',a)
                #sys.stdout.flush()
                #ostatniskl.update(**{i: a})
                to_updade[i]=a
            else:
                #print('i0', i[0])
                #sys.stdout.flush()
                a = request.POST.get(str(i[0]))
                #print('a', a)
                #sys.stdout.flush()
                to_updade[i[0]] = a



        to_updade=Przeliczanie(dodanySkladnik,to_updade)

        for key, value in to_updade.items():
            setattr(ostatniskl, key, value)
        #print('ostatniskl.jednostka_z_recepty', ostatniskl.jednostka_z_recepty)
        #sys.stdout.flush()
        ostatniskl.save()



        return JsonResponse({'tabela':to_updade})
    return JsonResponse({'nie dodano skladnika': False, }, safe=False)


def aktualizujTabela (request):
    #########uwzględniaie aa################################
    print('roboczareceptura.objects.last()', roboczareceptura.objects.last(),roboczareceptura.objects.last().aa)
    sys.stdout.flush()
    g=roboczareceptura.objects.last().gramy
    l=roboczareceptura.objects.last().pk
    print('g', g)
    sys.stdout.flush()
    #auto aa
    print('roboczareceptura.objects.all().order_by("-pk")[1]', roboczareceptura.objects.all().order_by('-pk')[1].pk)
    sys.stdout.flush()
    print(roboczareceptura.objects.last().aa=='off', roboczareceptura.objects.last().gramy!="",roboczareceptura.objects.all().order_by('-pk')[1].gramy=="")
    sys.stdout.flush()
    print('roboczareceptura.objects.last()', roboczareceptura.objects.last())
    sys.stdout.flush()
    last=roboczareceptura.objects.last()
    # last.aa = 'on'
    # last.save()
    if roboczareceptura.objects.last().aa=='off' and roboczareceptura.objects.last().gramy!=""  and roboczareceptura.objects.all().order_by('-pk')[1].gramy=="":
       last.aa ="on"
       last.save()

    print('roboczareceptura.objects.last().aa',roboczareceptura.objects.last().aa)
    if roboczareceptura.objects.last().aa=='on':
        for el in roboczareceptura.objects.all().order_by('-pk'):#order_by('-pk')
            #print('el.gramy',el.gramy,el.pk)
            #sys.stdout.flush()
            if el.pk<l and el.gramy != "":
                break
            # if el:
            #     print('el', el)
            #     sys.stdout.flush()
            else:
                el.gramy = g
                el.obey=l
                el.save()
    #print('el.gramy', roboczareceptura.objects.last(), roboczareceptura.objects.last().pk)
    #sys.stdout.flush()
    ####################################################
    ########### kasowanie ilości g po usunięciu skłądnika z aa#########################
    for el in roboczareceptura.objects.all():
        print('roboczareceptura.objects.filter(pk=el.obey).exists()',roboczareceptura.objects.filter(pk=el.obey).exists())
        sys.stdout.flush()
        if roboczareceptura.objects.filter(pk=el.obey).exists():
            pass
        else:
            if el.obey!=None:
                el.gramy=''
                el.obey= None
                el.save()
    ########################################################################################
    datax = serializers.serialize("python", roboczareceptura.objects.all())
    return JsonResponse({'tabela_zbiorcza':datax})