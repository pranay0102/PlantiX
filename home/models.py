from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content=models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message From '+self.name+' - '+self.email

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)
#     phone_number = models.CharField(max_length=12, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#     profile_image = models.ImageField(default='default-avatar.png', upload_to='users/', null=True, blank=True)

#     def __str__(self):
#         return '%s %s' % (self.user.first_name, self.user.last_name)


# class Profile(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     bio = models.TextField()
#     profile_pic = models.ImageField(null=True, blank=True, upload_to="media/static/images/")
#     facebook_url= models.CharField(max_length=255, null= True, blank=True)
#     Instagram_url= models.CharField(max_length=255, null= True, blank=True)
#     Twitter_url= models.CharField(max_length=255, null= True, blank=True)

    
#     def __str__(self):
#         return str(self.user)
