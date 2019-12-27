from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from django.urls import reverse

PROJECTS_TYPES = (
    ("draft", "Draft"),
    ("public", "Public"),
    ("private", "Private")
)


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    content = RichTextField(verbose_name="Content", default="", extra_plugins=['uploadimage'])
    author = models.CharField(max_length=30, verbose_name="Author")
    type = models.CharField(max_length=20, choices=PROJECTS_TYPES, verbose_name="Type")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    slug = AutoSlugField(populate_from='name', unique=True, unique_with='id')
    project_image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})


class File(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=50, verbose_name="File name")
    file = models.FileField(verbose_name="File", upload_to='uploads/')

    def __str__(self):
        return self.file_name
