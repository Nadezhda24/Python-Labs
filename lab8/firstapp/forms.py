from django import forms
from .models import Teacher

class DateInput(forms.DateInput):
    input_type = 'date'

class PostForm(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = '__all__'
		widgets = {
            'my_date': DateInput()
        }
	record=forms.IntegerField(label='Your record')
	surname= forms.CharField(label='Your surname',max_length=25)    
	name = forms.CharField(label='Your name',max_length=25)
	secondName= forms.CharField(label='Your second_name',max_length=25)
	birthday= forms.DateField(label='Your birthday')
	telephone= forms.CharField(label='Your telephone',max_length=11)
	experience=forms.IntegerField(label='Your experience',max_value=70)
	genger_choices=[('M','Man'),('W','Woman')]
	gender= forms.ChoiceField(label='Your gender',choices=genger_choices)
	discipline= forms.CharField(label='Your discipline',max_length=25)
