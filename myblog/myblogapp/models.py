from django.db import models
# user blog article comment tag
# Create your models here.
class user(models.Model):
	userid = models.CharField(max_length=30)
	realname = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	nickname = models.CharField(max_length=30)
	state = models.CharField(max_length=10)	
	photo = models.FileField(blank=True,null = True,upload_to = './upload/')
	mail = models.EmailField(blank=True,null = True)
	website = models.URLField(blank=True,null = True)
	birth = models.DateField(blank=True,null = True)
	sex = models.IntegerField(blank=True,max_length=100)
	phone = models.CharField(blank=True,null = True,max_length=100)


	def __unicode__(self):
		return self.realname

class blog(models.Model):
	blogid = models.CharField(max_length=30,blank=True)
	useby = models.ForeignKey("user", related_name="useBy")
	name = models.CharField(max_length=50)
	birth = models.DateField()
	words = models.CharField(max_length=100,blank=True,null = True)
	state = models.CharField(max_length=10)
	def __unicode__(self):
		return self.name

class article(models.Model):
	articleid = models.CharField(max_length=30,blank=True,null = True)
	writer = models.ForeignKey("user", related_name="wirteBy")
	blogname = models.ForeignKey("blog", related_name="fromBlog")
	state = models.CharField(max_length=10)

	createtime = models.DateField()
	modiftime = models.DateField()
	title = models.CharField(max_length=50)
	content = models.CharField(max_length=10000)
	def __unicode__(self):
		return self.title

class comment(models.Model):
	byarticle = models.ForeignKey("article", related_name="markFromArticle")
	byuser = models.ForeignKey("user", related_name="markByUser")
	state = models.CharField(max_length=10)

	supercomment = models.ForeignKey("comment", related_name="father",blank=True,null = True)
	subcomment = models.ForeignKey("comment", related_name="son",blank=True,null = True)
	rootcomment = models.ForeignKey("comment", related_name="grandpa",blank=True,null = True)
	time = models.DateField()
	content = models.CharField(max_length=1000)
	def __unicode__(self):
		return self.content

class tag(models.Model):
	name = models.CharField(max_length=20)
	articles = models.ManyToManyField("article")
	def __unicode__(self):
		return self.name