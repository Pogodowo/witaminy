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
    return render(request,'home.html',{'tabela2':datax})

def formJson (request,skl):
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
                sys.stdout.flush()
                to_updade[i]=a
            else:
                a = request.POST.get(str(i[0]))
                to_updade[i[0]] = a

        to_updade=Przeliczanie(dodanySkladnik,to_updade)
        for key, value in to_updade.items():
            setattr(ostatniskl, key, value)
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
    all=roboczareceptura.objects.all()
    last=roboczareceptura.objects.last()
    if len(all)>1 and roboczareceptura.objects.last().aa=='off' and roboczareceptura.objects.last().gramy!=""  and roboczareceptura.objects.all().order_by('-pk')[1].gramy=="":
       last.aa ="on"
       last.save()
    print('roboczareceptura.objects.last().aa',roboczareceptura.objects.last().aa)
    if roboczareceptura.objects.last().aa=='on':
        for el in roboczareceptura.objects.all().order_by('-pk'):#order_by('-pk')
            if el.pk<l and el.gramy != "":
                break
            else:
                el.gramy = g
                el.obey=l
                el.save()

    ####################################################
    ########### kasowanie ilości g po usunięciu skłądnika z aa#########################
    for el in roboczareceptura.objects.all():

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


def delSkl (request, id):
    deletedElement=roboczareceptura.objects.filter(pk=id)
    response=serializers.serialize("python", deletedElement)
    deletedElement.delete()
    print('response', response)
    sys.stdout.flush()
    return JsonResponse({'response':response})