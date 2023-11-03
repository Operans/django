from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic

# Create your views here.
class BookView(generic.ListView):
    template_name = 'book.html'
    queryset = models.Book.objects.all()

class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'

    def get_object(self, **kwargs):
       book = self.kwargs.get('id')
       return get_object_or_404(models.Book, id=book)

class CreateBookPostView(generic.CreateView):
    template_name = 'create_book.html'
    form_class = forms.BookForm
    queryset = models.Book.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBookPostView, self).form_valid(form=form)


class UpdateLangPostView(generic.UpdateView):
    template_name = 'update.html'
    form_class = forms.BookForm
    success_url = '/'

    def get_object(self, **kwargs):
        lang = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=lang)

    def form_valid(self, form):
        return super(UpdateLangPostView, self).form_valid(form=form)

class BookDropView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/'

    def get_object(self, **kwargs):
        lang_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=lang_id)

def createBookReview(request):
    method = request.method
    if method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Коммент успешно добавлен</h1>')

    else:
        form = forms.ReviewForm()

    return render(request, 'createReview.html', {'form': form})

class SearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'lang'
    paginate_by = 5

    def get_queryset(self):
        return models.ProgramLang.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

def createBookReview(requset):
    method = requset.method
    if method == 'POST':
        form = forms.ReviewForm(requset.POST, requset.FILES)
        if form.is_valid():
            form.save()

            return HttpResponse('<h1>Success</h1>')
    else:
        form = forms.ReviewForm()

    return render(requset, 'createReview.html', {'form' : form})

class SearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book'
    paginate_by = 5

    def get_queryset(self):
        return models.Book.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context