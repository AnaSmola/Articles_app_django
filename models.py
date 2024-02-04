from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from taggit.managers import TaggableManager

User = get_user_model()

STATUS_CHOICES = (('draft','Draft'),('published','Published'))


class Category(models.Model):
    """Categories of articles
    """
    title = models.CharField(verbose_name="Title", max_length=100)

    class Meta:
        ordering = ('title',)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('new_by_category',  args=[self.id])


class News(models.Model):
    """Class of articles
    """
    user = models.ForeignKey(
        User,
        verbose_name="Author",
        on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(
        Category,
        verbose_name="Category",
        on_delete=models.CASCADE,
        null=True)
    status = models.CharField(choices=STATUS_CHOICES, default='draft', max_length=10, verbose_name='Status')
    title = models.CharField(verbose_name="Title", max_length=100)
    content = models.TextField(verbose_name="Content", blank=False)
    picture = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True,  verbose_name="Picture")
    tags = TaggableManager(verbose_name="Tagged")
    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('new_single',  args=[self.id])


class Comments(models.Model):

    """Comments to articles
    """

    new = models.ForeignKey(
         News,
         verbose_name="Article",
         on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, verbose_name="Email")
    text = models.TextField(verbose_name="Text")
    published = models.DateTimeField(verbose_name="Published", auto_now_add=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ("published",)

    def __str__(self):
        return f"Comment by: {self.name}"


class Adds(models.Model):

    """Advertisements
    """
    name = models.CharField(max_length=50, verbose_name="Name")
    email = models.EmailField(max_length=50, verbose_name="Email")
    text = models.TextField(verbose_name="Text", max_length=255)
    phone = models.CharField(max_length=12, verbose_name="Telephone")
    published = models.DateTimeField(verbose_name="Published", auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Add"
        verbose_name_plural = "Adds"
        ordering = ("published",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('add_single', args=[self.id])

