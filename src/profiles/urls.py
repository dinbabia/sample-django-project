from django.urls import path,include
from .views import ProfileListView, ProfileDetailView, ProfileCreateView, ProfileUpdateView, ProfileDeleteView

app_name = "profiles"
urlpatterns = [
    path('', ProfileListView.as_view(), name="profile-list"),
    path('<int:id>/', ProfileDetailView.as_view(), name="profile-detail"), 
    path('<int:id>/update', ProfileUpdateView.as_view(), name="profile-update"), 
    path('create/', ProfileCreateView.as_view(), name="profile-create"),
    path('<int:id>/delete', ProfileDeleteView.as_view(), name="profile-delete"), 
]
