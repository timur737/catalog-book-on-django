import pytest
from catalog.models import AddBook, Author
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.mark.django_db
class TestModels:

    def test_add_book(self):
        img = SimpleUploadedFile(name='GqG8xnLu23A.jpg', \
             content=open('/home/timur/Projects/catalog/library-book-on-django/catalog/testing_image/GqG8xnLu23A.jpg', 'rb').read(), \
                 content_type='image/jpeg')
        book = AddBook.objects.create(title='Palach', description='Something else', image=img)
        book.save()
        assert book.title == 'Palach'
        assert book.description == 'Something else'
        AddBook.objects.filter(pk=book.id).delete()

    def test_add_author(self):
        photo = SimpleUploadedFile(name='GqG8xnLu23A.jpg', \
             content=open('/home/timur/Projects/catalog/library-book-on-django/catalog/testing_image/GqG8xnLu23A.jpg', 'rb').read(), \
                 content_type='image/jpeg')
        author = Author.objects.create(first_name='Lev', last_name='Tolstoy', was_born='2001-02-05')
        author.save()
        assert author.first_name == 'Lev'
        assert author.last_name == 'Tolstoy'
        assert author.was_born == '2001-02-05'
        Author.objects.filter(pk=author.id).delete()
        