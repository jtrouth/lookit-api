from django.conf.urls import url

from web import views

urlpatterns = [
    url(r'^signup/?$', views.ParticipantSignupView.as_view(), name='participant-signup'),
    url(r'^demographic_data/?$', views.DemographicDataCreateView.as_view(), name='demographic-data-create'),
    url(r'^studies/?$', views.StudiesListView.as_view(), name='studies-list'),
    url(r'', views.HomeView.as_view(), name='home'),
]