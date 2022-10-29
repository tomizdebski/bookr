from django.contrib import auth
from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text="Nazwa wydawnictwa")
    website = models.URLField(help_text="Witryna wydawnictwa")
    email = models.EmailField(help_text="Adres email wydawnictwa")

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=70, help_text="Tytuł ksiazki")
    publication_date = models.DateField(verbose_name="Data publikacji")
    isbn = models.CharField(max_length=20, verbose_name="Numer ISBN książki")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through="BookContributor")

    def __str__(self):
        return self.title

class Contributor(models.Model):
    first_names = models.CharField(max_length=50, help_text="Imie lub imiona tworcy")
    last_names = models.CharField(max_length=50, help_text="Nazwisko lub nazwiska współtwórcy")
    email = models.EmailField(help_text="Email współtwórcy")

    def __str__(self):
        return self.first_names


class BookContributor(models.Model):
    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role this contributor had in the book.",
                            choices=ContributionRole.choices, max_length=20)


class Review(models.Model):
    content = models.TextField(help_text="The Review text.")
    rating = models.IntegerField(help_text="The rating the reviewer has given.")
    date_created = models.DateTimeField(auto_now_add=True,
                                        help_text="The date and time the review was created.")
    date_edited = models.DateTimeField(null=True,
                                       help_text="The date and time the review was last edited.")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             help_text="The Book that this review is for.")
