from django.db import models

# Create your models here.

# Basic Information
class profile(models.Model):
    pic = models.ImageField(upload_to='main-photo', blank=False, null=False)
    name = models.CharField(max_length=30, blank=False, null=False)
    mname = models.CharField(max_length=50, blank=True, null=True)
    lname = models.CharField(max_length=50, blank=True, null=True)
    designation = models.CharField(max_length=256, blank=True, null=True)
    age = models.PositiveIntegerField()
    country = models.CharField(max_length=50, null=False, blank=False)
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    email = models.EmailField(max_length=256)
    phone = models.CharField(max_length=25, null=True, blank=True)
    description = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name
# Basic Information End

#Education
class education(models.Model):
    eduFor = models.ForeignKey(profile, on_delete=models.CASCADE)
    eduTitle = models.CharField(max_length=50, blank=False, null=False)
    eduFrom = models.CharField(max_length=100, blank=False, null=False)
    eduYear = models.PositiveIntegerField(blank=False, null=False)
    eduDesc = models.CharField(max_length=256, blank=True, null=True)
    def __str__(self):
        return str(self.eduFor)
#Education End

#Skils
class skils(models.Model):
    skilFor = models.ForeignKey(profile, on_delete=models.CASCADE)
    skilTitle = models.CharField(max_length=50, null=False, blank=False)
    skilPer = models.IntegerField(null=False, blank=False, default=1)
    def __str__(self):
        return str(self.skilFor) + ' ' +self.skilTitle
#Skils End

# Knowledges
class knowledge(models.Model):
    knoFor = models.ForeignKey(profile, on_delete=models.CASCADE)
    knowledges = models.CharField(max_length=500, null=False, blank= False)
    def __str__(self):
        return str(self.knoFor)
# Knowledges End

#Experience
class experience(models.Model):
    expFor = models.ForeignKey(profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    compuny = models.CharField(max_length=100, null=False, blank=False)
    fromDate = models.CharField(max_length=50, null=False, blank=False)
    toDate = models.CharField(max_length=50, null=False, blank=False)
    desc = models.CharField(max_length=500, null=True, blank=True)
    def __str__(self):
        return str(self.expFor)
#Experience End

#Portfolio
class portfolio(models.Model):
    portFor = models.ForeignKey(profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    img = models.ImageField(upload_to='img/portfolio', null=False, blank=False)
    url = models.URLField(null=True, blank=True)
    date = models.DateField()
    desc = models.CharField(max_length=500, null=False, blank= False)
    technology = models.CharField(max_length=256, blank=True, null=True)
    def __str__(self):
        return str(self.portFor)
#Portfolio End

#Contact
class contact(models.Model):
    messageFor = models.ForeignKey(profile, on_delete=models.CASCADE)
    fullName = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    subject = models.CharField(max_length=100, null=False, blank=False)
    message = models.CharField(max_length=1000, null=False, blank=False)
#Contact End