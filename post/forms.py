# from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit, Layout
# from .models import Post

# class PetPost(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ["pet_name", "pet_description", "pet_picture"]

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.attrs = {"novalidate": ''}
#         self.helper.layout = Layout(
#             'pet_name',
#             'pet_description',
#             'pet_picture',
#             Submit('submit', 'Submit'))