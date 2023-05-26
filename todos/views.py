from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TodoChangeForm, TodoCreationForm
from .models import Todo


def todo_list_view(request: HttpRequest) -> HttpResponse:
    """ """
    qs = Todo.objects.all()
    qs = qs.order_by("-create_at")
    return render(request, "todos/todos_list.html", {"object_list": qs})


def todo_detail_view(request: HttpRequest, id: int) -> HttpResponse:
    """ """
    todo = get_object_or_404(Todo, pk=id)
    return render(request, "todos/todos_detail.html", {"object": todo})


def todo_delete_view(request: HttpRequest, id: int) -> HttpResponse:
    """ """
    if request.method == "POST":
        # todo = Todo.objects.get(id=id)
        todo = get_object_or_404(Todo, pk=id)
        todo.delete()
    return redirect("todos:list")


def todo_toggle_complete_view(request: HttpRequest, id: int) -> HttpResponse:
    """ """
    if request.method == "POST":
        todo = get_object_or_404(Todo, pk=id)
        todo.complete = not todo.complete
        todo.save()
    return redirect("todos:list")


def todo_create_view(request: HttpRequest) -> HttpResponse:
    """ """
    if request.method == "POST":
        form = TodoCreationForm(request.POST)
        if form.is_valid():
            Todo.objects.create(
                title=form.cleaned_data["title"], complete=form.cleaned_data["complete"]
            )
            return redirect("todos:list")
    else:  # GET, ...
        form = TodoCreationForm()
        context = {
            "form": form,
        }
        return render(request, "todos/todos_edit.html", context)


def todo_edit_view(request: HttpRequest, id: int) -> HttpResponse:
    """ """
    todo = get_object_or_404(Todo, pk=id)

    if request.method == "POST":
        form = TodoChangeForm(request.POST)
        if form.is_valid():
            todo.title = form.cleaned_data["title"]
            todo.complete = form.cleaned_data["complete"]
            todo.save()
            return redirect("todos:list")
    else:  # GET, ...
        form = TodoChangeForm(instance=todo)
        context = {
            "form": form,
            "object": todo,
        }
        return render(request, "todos/todos_edit.html", context)
