from django.urls import reverse, resolve
from catalog import views


class TestUrls:
    
    def test_index(self):
        path = reverse('catalog:index')
        assert resolve(path).app_name == 'catalog'

    def test_detail(self):
        path = reverse('catalog:book_detail', kwargs={'pk': 6})
        assert resolve(path).view_name == 'catalog:book_detail'

    def test_add_book(self):
        path = reverse('catalog:addbook_url')
        assert resolve(path).url_name == 'addbook_url'
    
    def test_add_author(self):
        path = reverse('catalog:author_url')
        assert resolve(path).route == 'addauthor/'

    def test_edit(self):
        path = reverse('catalog:edit', kwargs={'pk': 6})
        assert resolve(path).func == views.edit
