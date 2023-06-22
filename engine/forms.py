from django import forms
from engine.models import Page
from codemirror2.widgets import CodeMirrorEditor

class PageForm(forms.ModelForm):
    override_css = forms.CharField(required=False, widget=CodeMirrorEditor(options={'mode': 'css', 'theme': 'icecoder'}))
    class meta:
        model = Page
