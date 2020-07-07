from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/' ,views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('meUp/<int:user_id>/', views.MUserView.as_view(), name='me'),
    path('update/<int:id>', views.UserPartialUpdateView.as_view({'get': 'detail'}), name='user_update')
    
]