from django import forms

class SearchForm(forms.Form): #Note that it is not inheriting from forms.ModelForm
    text = forms.CharField()
    count = forms.IntegerField()




    #All my attributes here