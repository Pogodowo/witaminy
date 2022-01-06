from django.db import models

class Skladnik (models.Model):
    nazwa=models.CharField( max_length=30)

class Parametry (models.Model):
    my_choices = (('1', 'g liq.'), ('2','j.m.' ),('3', 'op'),('4', 'krople'),('5', 'ml'),('5', 'g'))
    producenci=(('1','Medana 50000j.m./ml'),('2','Hasco 4500j.m./ml'))
    skladnik=models.ForeignKey(Skladnik, on_delete=models.CASCADE)
    jednostka = models.TextField(choices=my_choices)
    producent = models.TextField(choices=producenci)
    ilosc= models.DecimalField(max_digits=6, decimal_places=3,blank=True)
    ilegramliq=models.DecimalField(max_digits=6, decimal_places=3,blank=True)
    ilejm = models.DecimalField(max_digits=6, decimal_places=3,blank=True)
    ilegram = models.DecimalField(max_digits=6, decimal_places=3,blank=True)
    ilekropli = models.DecimalField(max_digits=6, decimal_places=3,blank=True)
    ileml=models.DecimalField(max_digits=6, decimal_places=3,blank=True)
    ileop=models.DecimalField(max_digits=6, decimal_places=3,blank=True)

class ElementyFormularzaSkladnika (models.Model):
    my_choiceswit = (('1', 'g liq.'), ('2', 'j.m.'), ('3', 'op'), ('4', 'krople'), ('5', 'ml'), ('5', 'g'))
    producenci = (('1', 'Medana 50000j.m./ml'), ('2', 'Hasco 4500j.m./ml'))
    skladnik = models.ForeignKey(Skladnik, on_delete=models.CASCADE)
    jednostkawit = models.TextField(choices=my_choiceswit)
    ilosc = models.DecimalField(max_digits=6, decimal_places=3, blank=True)



class Skladnikrecepty (models.Model):
    nazwas = models.CharField(max_length=30)
    ilegramliqs = models.DecimalField(max_digits=6, decimal_places=3, blank=True)
    ilejms = models.DecimalField(max_digits=6, decimal_places=3, blank=True)
    ilegrams = models.DecimalField(max_digits=6, decimal_places=3, blank=True)
    ilekroplis = models.DecimalField(max_digits=6, decimal_places=3, blank=True)
    ilemls = models.DecimalField(max_digits=6, decimal_places=3, blank=True)
    ileops = models.DecimalField(max_digits=6, decimal_places=3, blank=True)

class roboczareceptura (models.Model):
    producenci = (('1', 'Hasco 4500j.m./ml'), ('2', 'Medana 50000j.m./ml'),('3', 'Hasco 0,3g/ml'))
    skladnik=models.CharField(max_length=40)
    jednostka_z_recepty=models.CharField(max_length=40,blank=True, null=True)
    ilosc_na_recepcie=models.CharField(max_length=40,blank=True, null=True)
    gramy=models.CharField(max_length=40,default='0')
    mililitry = models.CharField(max_length=40, default='0')
    krople = models.CharField(max_length=40, default='0')
    opakowania = models.CharField(max_length=40, default='0')
    jednostki = models.CharField(max_length=40, default='0')
    sztuki = models.CharField(max_length=40, default='0')
    tabletki= models.CharField(max_length=40, default='0')
    czesci = models.CharField(max_length=40, default='0')
    producent = models.TextField(choices=producenci,blank=True, null=True)
    aa=models.CharField(max_length=20,default='off')
    obey=models.IntegerField(null=True)
    sumg=models.IntegerField(default=0)
    aa_ad=models.CharField(max_length=20,default='off')
    aa_ad_gramy=models.CharField(max_length=40,default='')

    def __str__(self):
        return   (self.skladnik)






