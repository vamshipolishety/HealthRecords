from django.urls import include, path
from .views import IndexView
app_name = 'HospitalRecords'

urlpatterns = [
    path(r'',IndexView.as_view(), name='base'),
]