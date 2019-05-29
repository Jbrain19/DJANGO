from django.views import generic
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import Page, UserFileUpload # Imports information from models.py for Page and UserFileUpload
from .forms import UploadFileForm # Imports information from forms.py for UserFileUpload

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class IndexView(generic.ListView):
    template_name = 'wiki/index.html'
    context_object_name = 'pages'

    def get_queryset(self):
        return Page.objects.all()

class DetailView(generic.DetailView):
    model = Page
    template_name = 'wiki/detail.html'

def view_page(request, pk):
    try:
        page = Page.objects.get(pk=pk)
        return render(request, "wiki/detail.html",{"page":page})
    except Page.DoesNotExist:
        return render (request, "wiki/create_page.html", {"page_name": pk}) 

@login_required(login_url='wiki:login') # Makes sure a login (if not already) is required before continuining
def edit_page(request, pk):
    try:
        page = Page.objects.get(pk=pk)
        content = page.content
    except Page.DoesNotExist:
        content=''
    return render(request,'wiki/edit_page.html',
                    {  
                        'page_name':pk,
                        'content': content
                    })

@login_required(login_url='wiki:login') # Makes sure a login (if not already) is required before continuining. Will display login page when user trys to save eddited content
def save_page(request, pk):
    content = request.POST["content"] 
    try: 
            page = Page.objects.get(pk=pk)
            page.content = content
    except Page.DoesNotExist:
        page =  Page(title=pk, content=content)
    page.save()
    return redirect ('wiki:detail', pk=pk) # Makes sure that if task fails it will redirect to the content page (detail)

@login_required(login_url='wiki:login') # Makes sure a login (if not already) is required before continuining
def upload_file(request):
    context = {}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadFileForm()
    context['form'] = form
    context['files'] = UserFileUpload.objects.all().order_by('upload')
    return render(request, 'wiki/upload.html', context)

