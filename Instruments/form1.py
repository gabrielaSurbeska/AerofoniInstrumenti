from django import forms

from Instruments.models import Slobodni_Aerofoni


class Slobodni_AerofoniForm(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super(Slobodni_AerofoniForm,self).__int__(*args, **kwargs)
        for filed in self.visible_fields():
            print(filed)
            filed.field.widget.attrs["class"] = "form-control"


    class Meta:
        model = Slobodni_Aerofoni
        exclude = ("user",)


