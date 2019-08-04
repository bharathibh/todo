from django.shortcuts import render

from totoapp.forms import TodoForm
from totoapp.models import Item
from totoapp.forms import TodoForm

from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# Create your views here.

from django.views.generic.edit import FormView

class TodoView(FormView):
    template_name = 'todoapp/todo.html'
    form_class = TodoForm
    success_url = '/'

    def form_valid(self, form):
        form.save(commit=True)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_valid(form)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todos"] =  Item.objects.filter(is_deleted=False)
        return context
    
    def post(self, request, *args, **kwargs):
        if "taskDelete" in request.POST and "checkedbox" in request.POST:
            
            checkedlist = request.POST["checkedbox"]
            if isinstance(checkedlist, str):
                checkedlist = [checkedlist]
            for todo_id in checkedlist:
                todo = Item.objects.get(id=int(todo_id))
                todo.is_deleted = True
                todo.save()
        return super().post(request, *args, **kwargs)
    

class TodoDetailView(DetailView):
    model = Item
    template_name = "todoapp/todo_details.html"	

class TodoUpdate(UpdateView):
    model = Item
    form_class = TodoForm
    template_name = "todoapp/todo_edit.html"
    # fields = ["title",  "description", "status", "expired_at",]
    success_url = reverse_lazy('todo_list')
    
    def get_initial(self):
        initial = super(TodoUpdate, self).get_initial()
        item = self.get_object()

        initial['expired_at'] = item.expired_at
        return initial


    def get_object(self, *args, **kwargs):
        item = get_object_or_404(Item, pk=self.kwargs['pk'])
        return item

