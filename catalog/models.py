from django.db import models
import os


class AddBook(models.Model):
    """Model definition for AddBook."""
    class Meta:
        """Meta definition for AddBook."""
        verbose_name = 'AddBook'
        verbose_name_plural = 'AddBooks'
        
    title = models.CharField(max_length=240)
    description = models.TextField()
    image = models.ImageField(upload_to='user_book/', blank=True)
    file_book = models.FileField(upload_to='file_book', null=True)
    
    def __str__(self):
        """Unicode representation of AddBook."""
        return self.title

    def delete(self):
        self.image.delete()
        super(AddBook, self).delete()


class Author(models.Model):
    """Model definition for Author."""
    class Meta:
        """Meta definition for Author.""" 
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=80)
    was_born = models.DateField()
    photo = models.ImageField(upload_to='author_book/', blank=True)
    book = models.ManyToManyField(AddBook)
    
    def __str__(self):
        """Unicode representation of Author."""
        return f'{self.first_name} {self.last_name}'

    def delete(self):
        self.image.delete()
        super(Author, self).delete()
