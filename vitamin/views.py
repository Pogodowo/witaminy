from django.shortcuts import render
from django.http import JsonResponse,response
from django.core import serializers
import sys
from .models import Skladnik
from .forms import VitAForm,VitEForm,HydrokortyzonForm
from .models import roboczareceptura
from .algorytmy import Przeliczanie

forms={'witamina A':VitAForm,'witamina E':VitEForm,'Hydrokortyzon': HydrokortyzonForm}
data={'witamina A':[['jednostka_z_recepty','opakowania','gramy','jednostki'],'ilosc_na_recepcie',['producent','Hasco 4500j.m./ml','Medana 50000j.m./ml'],],'witamina E':['opakowania','gramy','jednostki',['producent','Hasco 0,3g/ml']],'Hydrokortyzon':['gramy','aa'],}
def home (request):
    skladniki = roboczareceptura.objects.all()
    t = []
    for i in skladniki:
        t.append(i.skladnik)
    datax = serializers.serialize("python", roboczareceptura.objects.all())


    print('datax', datax)
    sys.stdout.flush()
    return render(request,'home.html',{'tabela2':datax})

def formJson (request,skl):

    form=forms[skl]
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
                print('i', i)
                sys.stdout.flush()
                print('a',a)
                sys.stdout.flush()
                #ostatniskl.update(**{i: a})
                to_updade[i]=a
            else:
                print('i0', i[0])
                sys.stdout.flush()
                a = request.POST.get(str(i[0]))
                print('a', a)
                sys.stdout.flush()
                to_updade[i[0]] = a



        to_updade=Przeliczanie(dodanySkladnik,to_updade)

        for key, value in to_updade.items():
            setattr(ostatniskl, key, value)
        print('ostatniskl.jednostka_z_recepty', ostatniskl.jednostka_z_recepty)
        sys.stdout.flush()
        ostatniskl.save()



        return JsonResponse({'tabela':to_updade})
    return JsonResponse({'nie dodano skladnika': False, }, safe=False)


def aktualizujTabela (request):
    datax = serializers.serialize("python", roboczareceptura.objects.all())
    return JsonResponse({'tabela_zbiorcza':datax})