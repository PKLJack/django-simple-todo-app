from django.urls import path

from .views import (
    todo_create_view,
    todo_delete_view,
    todo_detail_view,
    todo_edit_view,
    todo_list_view,
    todo_toggle_complete_view,
)

app_name = "todos"

urlpatterns = [
    path("", todo_list_view, name="list"),
    path("create/", todo_create_view, name="create"),
    path("<int:id>/", todo_detail_view, name="detail"),
    path("<int:id>/edit/", todo_edit_view, name="edit"),
    path("<int:id>/delete/", todo_delete_view, name="delete"),
    path("<int:id>/toggle_complete/", todo_toggle_complete_view, name="toggle"),
]
