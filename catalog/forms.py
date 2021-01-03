from django import forms
from catalog.models import AddBook, Author



class AddBooksForm(forms.ModelForm):
    """Form definition for AddBooks."""

    class Meta:
        """Meta definition for AddBooksform."""

        model = AddBook
        fields = "__all__"
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
        }


class AuthorForm(forms.ModelForm):
    """Form definition for Author."""
    class Meta:
        """Meta definition for Authorform."""
        model = Author
        fields = ('first_name', 'last_name', 'was_born', 'photo', 'book')
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'width':'20px'}),
            'was_born':forms.TextInput(attrs={'class':'form-control form-control-sm'}), 
            'book':forms.SelectMultiple(attrs={'multiple class':'form-control'})
        }