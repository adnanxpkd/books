from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name
    
class Ebook(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()

    class Meta:
        db_table = 'ebook'
        ordering = ('title','author','description')

    def __str__(self):
        return f"{self.title} by {self.author}"

class AudioCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AudioAuthor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Audiobook(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(AudioAuthor,on_delete=models.CASCADE)
    category = models.ForeignKey(AudioCategory, on_delete=models.CASCADE)
    description = models.TextField()

    class Meta:
        db_table = 'audiobook'
        ordering = ('title','author','description')

    def __str__(self):
        return f"{self.title} by {self.author}"
