from django.forms import ModelForm
from .models import KhoiDong1Question


class KhoiDong1QuestionForm(ModelForm):
    """
    The form to create a new Khoi Dong question
    """

    class Meta:
        model = KhoiDong1Question
        fields = "__all__"
