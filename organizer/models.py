from django.db import models

# Create your models here.


class Tag(models.Model):
	name = models.CharField(max_length=31)
	slug = models.SlugField()

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name



class Startup(models.Model):
	name = models.CharField(
		max_length=31,
		db_index=True
		)
	slug = models.SlugField(
		max_length=31,
		unique=True,
		help_text='A label for URL config.')
	description = models.TextField()
	founded_date = models.DateField('date founded')
	contact = models.EmailField()
	website = models.URLField(max_length=255)
	tags = models.ManyToManyField(Tag)

	class Meta:
		ordering = ['name']
		get_latest_by = 'founded_date'

	def __str__(self):
		return self.name

class NewsLink(models.Model):
	name = models.CharField(max_length=63)
	pub_date = models.DateField()
	link = models.URLField()
	startup = models.ForeignKey(Startup, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'News Article'
		ordering = ['-pub_date']
		get_latest_by = 'pub_date'

	def __str__(self):
		return f"{self.startup} {self.name}"