from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Value, F
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic.list import ListView


from .models import Announcment
from .forms import SearchForm, AnnouncmentForm
# Create your views here.

def search(request):
    if request.method == 'GET':
        get_data = request.GET
        form = SearchForm(get_data)
        if form.is_valid():
            q = form.cleaned_data['q']
            announcments = Announcment.objects.filter(name__icontains=q).annotate(url_name=Value('announcment_detail'), obj_name=F('title'))
            object_list = list(announcments) 
            context = {'object_list': object_list}
            return render(request, 'board/search_list.html', context)


def announcment_list(request):
    announcment = Announcment.objects.all()
    paginator = Paginator(announcment, 1, orphans=1)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {"object_list": page.object_list, "page_obj": page}
    return render(request, "board/announcment_list.html", context)


class AnnouncmentCreate(CreateView):
    model = Announcment
    success_url = reverse_lazy('product_list')
    form_class = AnnouncmentForm


class AnnouncmentDelete(DeleteView):
    model = Announcment
    success_url = reverse_lazy('announcment_list')
    template_name = 'board/announcment_form.html'


class AnnouncmentUpdate(UpdateView):
    model = Announcment
    fields = '__all__'
    success_url = reverse_lazy('announcment_list')


class AnnouncmentList(ListView):
    model = Announcment
    paginate_by = 2
    paginate_orphans = 1

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Bce announcment')
        return super().dispatch(request, *args, **kwargs)


class AnnouncmentDetail(DetailView):
    model = Announcment
    context_object_name = 'announcment'
