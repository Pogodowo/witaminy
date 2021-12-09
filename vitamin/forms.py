from django import forms

class VitAForm (forms.Form):
    my_choices = (('1', 'g liq.'), ('2', 'j.m.'), ('3', 'op'), ('4', 'krople'), ('5', 'ml'), ('5', 'g'))
    producenci = (('1', 'Medana 50000j.m./ml'), ('2', 'Hasco 4500j.m./ml'))
    jednostka = forms.ChoiceField(choices=my_choices)
    producent = forms.ChoiceField(choices=producenci)
    ilosc = forms.DecimalField(max_digits=6, decimal_places=3)


class VitEForm(forms.Form):
    my_choices = (('1', 'g liq.'), ('2', 'j.m.'), ('3', 'op'), ('4', 'krople'), ('5', 'ml'), ('5', 'g'))
    jednostka = forms.ChoiceField(choices=my_choices)
    ilosc = forms.DecimalField(max_digits=6, decimal_places=3)

class HydrokortyzonForm (forms.Form):
    ilosc = forms.DecimalField(max_digits=6, decimal_places=3)


