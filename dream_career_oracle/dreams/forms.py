from django import forms


# class AddNewStep(forms.Form):
#     step_title = forms.CharField()
#     description = forms.CharField()
#     estimated_time = forms.CharField()
#     status = forms.ChoiceField("Pending", "In Progress", "Completed")

class EditDream(forms.Form):
    dreamtitle = forms.CharField()
    shortdescription = forms.ChoiceField()
    category = forms.ChoiceField()
    
    