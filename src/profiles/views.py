from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)


from .models import Profiles
from .forms import ProfileModelForm


class ProfileListView(ListView):
    # if template_name is to be changed or override:
    # template_name = 'profiles/profile_list.html'
    queryset = Profiles.objects.all()

class ProfileDetailView(DetailView):
    # if template_name is to be changed or override:
    # template_name = 'profiles/profile_list.html'
    # queryset = Profiles.objects.all()

    def get_object(self):
        _id = self.kwargs.get('id')
        return get_object_or_404(Profiles, id=_id)

class ProfileDeleteView(DeleteView):
    # if template_name is to be changed or override:
    # template_name = 'profiles/profile_list.html'
    # queryset = Profiles.objects.all()

    def get_object(self):
        _id = self.kwargs.get('id')
        return get_object_or_404(Profiles, id=_id)

    def get_success_url(self):
        return reverse("profiles:profile-list")

class ProfileCreateView(CreateView):
    form_class = ProfileModelForm
    template_name = 'profiles/profiles_create.html'
    queryset = Profiles.objects.all()
    # success_url = "/" # override default url when done filling up form
    def form_valid(self, form):
        return super().form_valid(form)

class ProfileUpdateView(UpdateView):
    form_class = ProfileModelForm
    # template_name = 'profiles/profiles_create.html'
    queryset = Profiles.objects.all()

    def get_object(self):
            _id = self.kwargs.get('id')
            return get_object_or_404(Profiles, id=_id)



