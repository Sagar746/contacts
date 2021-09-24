from django.db import models

# Create your models here.

LABEL_CHOICE=(
	('home','Home'),
	('work','Work')
)

class Contact(models.Model):
	first_name=models.CharField(max_length=200)
	last_name=models.CharField(max_length=200)
	address=models.CharField(max_length=200)
	label=models.CharField(max_length=10,choices=LABEL_CHOICE,default='home')

	def __str__(self):
		return self.first_name


class Email(models.Model):
	email=models.EmailField(max_length=200,null=True)
	contacts=models.ForeignKey(Contact,on_delete=models.CASCADE,null=True,related_name='emails')

	def __str__(self):
		return self.email

