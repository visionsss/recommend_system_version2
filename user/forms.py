from django import forms
from django.core.exceptions import ValidationError
from . import models


class RegisterForm(forms.Form):
    # 校验两次密码是否相同等
    def clean(self):
        username = self.cleaned_data.get('username')
        user = models.User.objects.filter(username=username).first()
        if user:
            raise ValidationError('用户名已存在')
        pwd = self.cleaned_data.get('password1')
        re_pwd = self.cleaned_data.get('password2')
        if pwd == re_pwd:
            return self.cleaned_data
        else:
            raise ValidationError('两次密码不一致')

    username = forms.CharField(label="用户名", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "请输入用户名小于30个字符"}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class LoginForm(forms.Form):
    # 校验账号密码
    def clean(self):
        username = self.cleaned_data.get('username')
        user = models.User.objects.filter(username=username).first()
        if not user:
            raise ValidationError('该用户名尚未注册')
        else:
            if user.password != self.cleaned_data.get('password'):
                raise ValidationError('密码输入错误')
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class StudentInfoForm(forms.Form):
    sex_gender = (
        ('male', "男"),
        ('female', "女"),
    )
    province_gender = (
        ('GuangDong', '广东'),
    )
    subject_gender = (
        ('science', '理科'),
        ('art', '文科'),
    )
    sex = forms.ChoiceField(label='性别', choices=sex_gender)
    province = forms.ChoiceField(label='省份', choices=province_gender)
    subject = forms.ChoiceField(label='科别', choices=subject_gender)
    score = forms.IntegerField(label='高考分数', max_value=800, min_value=0, widget=forms.NumberInput)
