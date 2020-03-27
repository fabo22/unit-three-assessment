from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm

# Create your views here.
def home(request):
    widget = Widget.objects.all()    
    widget_form = WidgetForm()
    form = WidgetForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'home.html', {
        'widget': widget, 'widget_form': widget_form
  })

def delete(request, widget_id):
    widget = Widget.objects.get(pk=widget_id)
    widget.delete()
    return redirect('home')