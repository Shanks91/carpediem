from django import forms
from .models import Ngo, Happening, Gallery, HapComments


class NgoForm(forms.ModelForm):

    class Meta:
        model = Ngo
        exclude = ('moderator',)


class HappeningForm(forms.ModelForm):

    class Meta:
        model = Happening
        exclude = ('author',)


class GalleryForm(forms.ModelForm):

    class Meta:
        model = Gallery
        exclude = ('owner',)


class HapCommentsForm(forms.ModelForm):

    class Meta:
        model = HapComments
        exclude = ('author', 'comment_on')
