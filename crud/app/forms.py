from cProfile import label
from django import forms
from django import forms
from .models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields= ('fullname','mobile','emp_code','position')   #or '__all__'

    # change the name on the web page
        labels={
            'fullname':'FULL NAME',
            'emp_code':'EMP Code'
        }

    # removing the empty labeled field
    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__( *args, **kwargs)
        self.fields['position'].empty_label="select"
        self.fields['emp_code'].required=False
