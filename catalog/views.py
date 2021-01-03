from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import TemplateView, View, DetailView
from catalog.models import AddBook, Author
from catalog.forms import AddBooksForm, AuthorForm
from django.db.models import Q


def base(request):
    return redirect(reverse('catalog:index'))


class IndexView(TemplateView):
    def get(self, request):
        books = AddBook.objects.all()
        return render(request, 'catalog/index.html', {'books':books})


class Authors(TemplateView):
    def get(self, request):
        author = Author.objects.all()
        return render(request, 'catalog/author_index.html', {'author':author})


class AddAuthor(View):
    def get(self, request):
        form = AuthorForm()
        return render(request, 'catalog/author.html', {'form':form})
        
    def post(self, request):
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            if 'photo' in request.FILES:
                form.image = request.FILES['photo']
            form.save()
            return redirect(reverse('catalog:author'))
        else:
            print(form.errors)
        return render(request, 'catalog/author.html', {'form':form})

class AddBooks(View):
    def get(self, request):
        form = AddBooksForm()
        return render(request, 'catalog/addbook.html', {'form':form})

    def post(self, request):
        bound_form = AddBooksForm(request.POST, request.FILES)
        if bound_form.is_valid():
            if 'image' in request.FILES:
                bound_form.image = request.FILES['image']
            bound_form.save()
            return redirect(reverse('catalog:index'))
        else:
            print(bound_form.errors)
        return render(request, 'catalog/addbook.html', {'form':bound_form})


class BookDetail(View):
    def get(self, request, pk):
        book = get_object_or_404(AddBook, pk=pk)
        return render(request, 'catalog/book.html', {'book':book})


def edit(request, pk):
    book = get_object_or_404(AddBook, pk=pk)
    form = AddBooksForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect(reverse('catalog:index'))
    return render(request, 'catalog/edit.html', {'form':form})

def delete(request, pk):
    book = get_object_or_404(AddBook, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect(reverse('catalog:index'))
    return render(request, 'catalog/confirm_delete.html', {'object':book})
def search(request):
    search_query = request.GET.get('search', '')
    if search_query == '':
        print('Not found')
    if search_query:
        books = AddBook.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))
        author = Author.objects.filter(Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query))
    else:
        books = AddBook.objects.all()
        author = Author.objects.all()
    return render(request, 'catalog/index.html', {
        'books':books,
        'author':author
        })




