from django import forms


class school_form(forms.Form):
    school_name = forms.CharField(label="院校名称", empty_value='')
    province = forms.CharField(label="省份", empty_value='')
