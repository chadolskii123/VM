from django.contrib.auth import get_user_model, authenticate, login, user_logged_in
from django import forms
from django.contrib import messages
#LoginForm, RegisterForm, UserDetailChangeForm

User = get_user_model()

class UserDetailChangeForm(forms.ModelForm):
    full_name = forms.CharField(required=None, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta :
        model = User
        fields = ('username',)


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta :
        model = User
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        print(kwargs)
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        request = self.request
        data = self.cleaned_data
        email = data.get("email")
        password = data.get("password")
        qs = User.objects.filter(email=email)
        
        user = authenticate(request, username=email, password=password)
        if user is None:
            messages.success(request, "Cannot login with you've written. Please check again.")
            raise forms.ValidationError("Invalid credentials")
        login(request, user)
        self.user = user
        user_logged_in.send(user.__class__, user=user, request=request)

        login(request, user)
        self.user = user
        user_logged_in.send(user.__class__, user=user, request=request)
        try:
            pass
        except:
            pass
        return data


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta :
        model = User
        fields = ('username', 'email')

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2 :
            raise forms.ValidationError("Passwords are not matched")
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = True
        if commit : 
            user.save()
        return user