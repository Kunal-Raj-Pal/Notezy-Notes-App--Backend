from django.urls import path
from .views import *

urlpatterns = [
    path("notes",notes, name="notes"),
    path("notes/add",add_notes, name="add_notes"),
    path("notes/edit/<id>",edit_notes, name="edit_note"),
    path("notes/delete/<id>",delete, name="delete"),
]
