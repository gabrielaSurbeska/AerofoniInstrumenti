from django import forms

from Instruments.models import Duvacki_Instrumenti


class Duvacki_Instrumenti(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super(Duvacki_Instrumenti,self).__int__(*args, **kwargs)
        for filed in self.visible_fields():
            print(filed)
            filed.field.widget.attrs["class"] = "form-control"


    class Meta:
        model = Duvacki_Instrumenti
        exclude = ("user",)


