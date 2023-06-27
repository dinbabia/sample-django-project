from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title       = forms.CharField(label='Titleee')
    class Meta:
        model = Product
        fields = ["title", "description", "price", "summary"]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "THE" not in title:
            raise forms.ValidationError("'THE' should be included in the title.")
        return title

class RawProductForm(forms.Form):
    title       = forms.CharField(label='Titleee')
    description = forms.CharField(
                        required=False, 
                        widget=forms.Textarea(
                                      attrs = {
                                        "class" : "sample-class center-blue",
                                        "id"    : "sample-id title",
                                        "rows"  : 15,
                                        "columns" : 20,
                                        "placeholder" : "Enter description here"
                                      }
                                  ))
    price       = forms.DecimalField(initial=50.0)
