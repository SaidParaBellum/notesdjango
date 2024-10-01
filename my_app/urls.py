from django.urls import path
from my_app.views import IndexView, NoteView, NotesCreateView, NotesUpdateView, NotesDeleteView, MakeNoteDoneView
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('notes/', NoteView.as_view(), name='notes'),
    path('create', NotesCreateView.as_view(), name='create'),
    path('update/<int:pk>/', NotesUpdateView.as_view(), name='update'),
    path('delete/<int:id>/', NotesDeleteView.as_view(), name='delete'),
    path('make_done/<int:pk>/', MakeNoteDoneView.as_view(), name='make_done'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),


]