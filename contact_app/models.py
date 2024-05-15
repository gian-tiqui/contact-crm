from django.db import models

class Contact(models.Model):
  cid = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=50)
  middle_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  phone = models.CharField(max_length=30)
  email = models.EmailField(max_length=40)
  contact_of = models.CharField(max_length=40)

  def __str__(self) -> str:
    return (self.last_name)


class User(models.Model):
  uid = models.AutoField(primary_key=True)
  email = models.EmailField(max_length=40)
  password = models.CharField(max_length=30)
