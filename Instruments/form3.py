from django import forms

from Instruments.models import Slobodni_Aerofoni, Register


class RegisterForm(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super(RegisterForm,self).__int__(*args, **kwargs)
        for filed in self.visible_fields():
            print(filed)
            filed.field.widget.attrs["class"] = "form-control"


    class Meta:
        model = Register
        exclude = ("user",)


