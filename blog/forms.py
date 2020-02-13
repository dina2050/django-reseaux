from django.forms import inlineformset_factory
from django.contrib.auth.models import User
from .models import Profil
from dal import autocomplete
from django import forms
from leaflet.forms.widgets import LeafletWidget
ProfilFormSet = inlineformset_factory(User, Profil,
                                   exclude = (),
                                    can_delete = False,
                                    extra = 1,
                                    max_num = 1,
                                    widgets = {'geom': LeafletWidget()}
)


class SearchForm(forms.Form):
    search_form = forms.ModelChoiceField(
        queryset=Profil.objects.all(),
        widget=autocomplete.ModelSelect2(url='profil-autocomplete', attrs={'data-html':True})
    ) 