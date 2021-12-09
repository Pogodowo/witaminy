data={'witamina A':[['jednostka_z_recepty','opakowania','gramy','jednostki'],'ilosc_na_recepcie',['producent','Hasco 4500j.m./ml','Medana 50000j.m./ml'],],'witamina E':['opakowania','gramy','jednostki',['producent','Hasco 0,3g/ml']],'Hydrokortyzon':['gramy'],}

def Przeliczanie (dodanySkladnik,to_update):
    if dodanySkladnik=='witamina A':
        if to_update['jednostka_z_recepty']=='gramy':
            if to_update['producent']=='Hasco 4500j.m./ml':
                to_update['mililitry']=str(float(to_update['ilosc_na_recepcie'])*1.14)
                to_update['opakowania'] = str(float(to_update['ilosc_na_recepcie']) /10)
                to_update['jednostki'] = str(float(to_update['ilosc_na_recepcie']) * 45000)
                to_update['krople'] = str(float(to_update['mililitry']) * 28)
                to_update['gramy'] = to_update['ilosc_na_recepcie']
            elif to_update['producent']=='Medana 50000j.m./ml':
                to_update['mililitry']=str(int(to_update['ilosc_na_recepcie'])*1.08)
                to_update['opakowania'] = str(int(to_update['ilosc_na_recepcie']) /10)
                to_update['jednostki'] = str(int(to_update['ilosc_na_recepcie']) * 50000)
                to_update['krople'] = str(float(to_update['mililitry']) * 30)
                to_update['gramy'] = to_update['ilosc_na_recepcie']
        elif to_update['jednostka_z_recepty']=='jednostki':
            if to_update['producent']=='Hasco 4500j.m./ml':
                to_update['mililitry']=str(int(to_update['ilosc_na_recepcie'])/45000)
                to_update['opakowania'] = str(int(to_update['ilosc_na_recepcie']) /10)
                to_update['jednostki'] = str(int(to_update['ilosc_na_recepcie']) * 45000)
                to_update['krople'] = str(int(to_update['mililitry']) * 28)
            elif to_update['producent']=='Medana 50000j.m./ml':
                to_update['mililitry']=str(int(to_update['ilosc_na_recepcie'])*1.08)
                to_update['opakowania'] = str(int(to_update['ilosc_na_recepcie']) /10)
                to_update['jednostki'] = str(int(to_update['ilosc_na_recepcie']) * 50000)
                to_update['krople'] = str(int(to_update['mililitry']) * 30)
        elif to_update['jednostka_z_recepty']=='opakowania':
            if to_update['producent']=='Hasco 4500j.m./ml':
                to_update['mililitry']=str(int(to_update['ilosc_na_recepcie'])*1.14)
                to_update['opakowania'] = str(int(to_update['ilosc_na_recepcie']) /10)
                to_update['jednostki'] = str(int(to_update['ilosc_na_recepcie']) * 45000)
                to_update['krople'] = str(float(to_update['mililitry']) * 28)
            elif to_update['producent']=='Medana 50000j.m./ml':
                to_update['mililitry']=str(int(to_update['ilosc_na_recepcie'])*1.08)
                to_update['opakowania'] = str(int(to_update['ilosc_na_recepcie']) /10)
                to_update['jednostki'] = str(int(to_update['ilosc_na_recepcie']) * 50000)
                to_update['krople'] = str(int(to_update['mililitry']) * 30)

    return to_update




dodanySkladnik='witamina A'
to_update={'jednostka_z_recepty': 'gramy', 'ilosc_na_recepcie': '99', 'producent': 'Hasco 4500j.'}