from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.base import View
from django.http import JsonResponse

from .forms import ToDoForm


from .models import ToDo

class ToDoView(ListView):
    """ main view
    """
    model = ToDo
    queryset = ToDo.objects.all()
    template_name = 'main/main.html'

    # def get(self, request):
    #     data = {
    #     }
    #     return render(request, self.template, data)

class Check(View):
    """ main view
    """
    model = ToDo
    template = 'main/main.html'

    def post(self, request):
        todo =  request.POST.get('ToDo')
        status =  get_status(request.POST.get('status'))

        obj = ToDo.objects.get(ToDo=todo)
        obj.status = status
        obj.save()

        # print(todo, status)
        data = {
            'todo': todo,
            'status': status,
        }
        return JsonResponse(data, safe=False)

def get_status(status):
    ''' Geting status from a request POST format
    '''
    if status == 'true':
        return True
    else:
        return False


class Remove(View):
    """ main view
    """
    model = ToDo
    template = 'main/main.html'

    def post(self, request):
        try:
            obj = ToDo.objects.get(ToDo=request.POST.get('ToDo'))
            obj.delete()
            success = True
        except:
            success = False

        data = {
            'success': success
        }
        return JsonResponse(data, safe=False)


class Add(View):
    """ main view
    """
    model = ToDo
    template = 'main/main.html'

    def post(self, request):
        # todo =  request.POST.get('ToDo')
        try:
            form = ToDoForm(request.POST)
            if form.is_valid():
                form.save()
        except:
            pass
        return redirect('/')