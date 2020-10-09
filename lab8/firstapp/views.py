from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from .models import Teacher
from .forms import PostForm


def view(request):
	
	list = Teacher.objects.order_by('record')
	context ={
		"title": "Main",
		"list": list,
	}
	return render(request, "index.html",context)
 

def products(request):
    a=Teacher.objects.get_or_create(request.POST)
    context={
    	"teach": a,
    }
    return render(request, "temp.html",context)
 
def users(request):

	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			a=form.save()
			a.save()
			return redirect('/')
	else:
		form = PostForm()

	return render(request, "lab7.html", {'form': form })


def delete(request, record):
	try:
		Teachers = Teacher.objects.get(record=record)
		Teachers.delete()
		return redirect('/')
	except Person.DoesNotExist:
		return HttpResponseNotFound("<h2>Person not found</h2>")