from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Todo


class TodoCreationForm(ModelForm):
    class Meta:
        model = Todo
        fields = ("title", "complete")
        labels = {
            "title": _("Todo"),
            "complete": _("Complete?")
        }
        # help_texts = {
        #     "title": _("Todo"),
        #     "complete": _("Complete?")
        # }


class TodoChangeForm(ModelForm):
    class Meta:
        model = Todo
        fields = ("title", "complete")
        labels = {
            "title": _("Todo"),
            "complete": _("Complete?")
        }
        # help_texts = {
        #     "title": _("Todo"),
        #     "complete": _("Complete?")
        # }
