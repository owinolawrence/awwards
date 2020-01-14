from django.db import models

# Create your models here.

class Project(models.Model):
    title =models.CharField(max_length =30)
    project_image=models.ImageField(default = 'default.jpg', upload_to="Pictures")
    description=models.TextField()
    project_url=models.TextField()

    def __str__(self):
        return self.caption


    @classmethod
    def search_by_title(cls,search_term):
        award = cls.object
