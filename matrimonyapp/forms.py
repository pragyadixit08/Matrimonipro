from django import  forms

class RegisterForm(forms.Form):
    first_name =  forms.CharField(
        label='First name ',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter your first name'
            }
        )
    )
    last_name = forms.CharField(
        label='Last name ',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter your last name'
            }
        )
    )
    GENDER_CHOICE = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    gender = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=GENDER_CHOICE
    )
    username = forms.CharField(
        label='User name ',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter your user name'
            }
        )
    )
    password1 = forms.CharField(
        label='Password ',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter your password'
            }
        )
    )
    password2 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Re-enter your password'
            }
        )
    )
    email = forms.EmailField(
        label='Email-id',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter your email id'
            }
        )
    )
    mobile = forms.IntegerField(
        label='Mobile ',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter your mobile number'
            }
        )
    )
    dob = forms.CharField(
        label='DOB ',
        widget=forms.DateInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter your date of birth'
            }
        )
    )

class LoginForm(forms.Form):
    username = forms.CharField(
        label='User name ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your user name'
            }
        )
    )
    password1 = forms.CharField(
        label='Password ',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password'
            }
        )
    )

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':'Enter your name'
            }
        )
    )
    GENDER_CHOICE = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    gender = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=GENDER_CHOICE
    )
    email = forms.EmailField(
        label='Email-id',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email id'
            }
        )
    )
    mobile = forms.IntegerField(
        label='Mobile ',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your mobile number'
            }
        )
    )
    about = forms.CharField(
        label='About you',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Some thing about you....'
            }
        )
    )

class PasswordForm(forms.Form):
    username = forms.CharField(
        label='User name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your user name'
            }
        )
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your password'
            }
        )
    )
    password2 = forms.CharField(
        label='Re-type Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 're-enter your password'
            }
        )
    )