# -*-coding:utf-8-*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from settings import *
from myblogapp.models import *
# from hellocjsAPP.models import Programmer

import datetime
def article_edit(request, offset) :
	try :
		offset = int(offset)
	except ValueError:
		raise Http404()
	art = article.objects.get(id=offset)
	if request.method == 'POST':
		if request.session.test_cookie_worked():
			request.session.delete_test_cookie()
			# edit article here
			if "user_id" in request.session:
				user_id = request.session["user_id"]
				u = user.objects.get(id=user_id)

				
				art_id = request.POST.get("art_id", '')
				title = request.POST.get("title", '')
				content = request.POST.get("content", '')
				modiftime = datetime.datetime.now()
				state = request.POST.get("state", '')

				art = article.objects.get(id=art_id)
				# check if writer's article
				if art and u and art.writer == u:
					# has the access to edit article
					if title != '' and content != '':
						# can modefied
						art.title = title
						art.content = content
						art.state = state
						art.modiftime = modiftime
						art.save()
						return HttpResponseRedirect("/" + art.id)
				else:
					return render_to_response("warning.html", {warnings:"You have no access to delete this article"},context_instance=RequestContext(request))

			# not done here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


	request.session.set_test_cookie()
	# art: article
	return render_to_response("article_edit.html",locals(),context_instance=RequestContext(request))


def articles_show(request) :
	canedit = False
	if "user_id" in request.session:
		canedit = True
		user_id = request.session["user_id"]
		u = user.objects.get(id=user_id)
		articles = article.objects.filter(writer=u,state="exist")
		return render_to_response("articles.html",locals(),context_instance=RequestContext(request))
	return HttpResponseRedirect("/")

def article_search(request, offset) :
	try :
		offset = int(offset)
	except ValueError:
		raise Http404()

	art = article.objects.get(id=offset, state="exist")
	canedit = False
	if "user_id" in request.session:
		user_id = request.session["user_id"]
		u = user.objects.get(id = user_id)
		if art.writer == u:
			print "writer is user"
			canedit = True
	return render_to_response("article.html",locals(),context_instance=RequestContext(request))

def article_del(request, offset):
	try :
		offset = int(offset)
	except ValueError:
		raise Http404()
	art = article.objects.get(id=offset)
	candel = False
	if "user_id" in request.session:
		user_id = request.session["user_id"]
		u = user.objects.get(id=user_id)
		if art.writer == u:
			print "writer is user"
			candel = True
			art.state = "del"
			art.save()
			return HttpResponseRedirect("/personal/articles/")

	return render_to_response("warning.html", {warnings:"You have no access to delete this article"},context_instance=RequestContext(request))

def article_add(request):
	if request.method == 'POST':
		if request.session.test_cookie_worked():
			request.session.delete_test_cookie()
			# add article here 
			# try:
			if "user_id" in request.session:
				user_id = request.session["user_id"]
				u = user.objects.get(id = user_id)
				if u.state == "manager":
					# has the access to add article
					ublog = blog.objects.get(useby=u)
					article_title = request.POST["article_title"]
					article_content = request.POST["article_content"]
					now = datetime.datetime.now()
					new_article = article.objects.create(writer=u, blogname=ublog, state="exist", createtime=now, modiftime=now, title=article_title, content=article_content)
					new_article.save()

					# return render_to_response("article.html")
					return HttpResponseRedirect('/'+str(new_article.id) + '/')
				else:
					return HttpResponse("You have no access to add article")
			return HttpResponse("Please login first")
			# except:
				# return HttpResponse("Getting user_id in session has some problem may be")
		else:
			return HttpResponse("Please enable cookies and try again")

	request.session.set_test_cookie()
	return render_to_response("article_add.html")

def personal(request):
	if "user_id" in request.session:
		user_id = request.session["user_id"]
		u = user.objects.get(id=user_id)

		if request.method == 'POST':

			# edit your profile
			new_mail = request.POST.get("mail", '')
			new_photo = request.FILES.get("photo", '')
			old_password = request.POST.get("old_password", '')
			new_password = request.POST.get("new_password", '')
			new_website = request.POST.get("website", '')
			new_birth = request.POST.get("birth", '')
			# new_birth = "2014-12-12" 
			
			birth_date_time = '' if new_birth == '' else datetime.datetime.strptime(new_birth,'%Y-%m-%d') 
			# to day string 
			# date_time.strftime('%Y-%m-%d')
			# datetime to time cut
			# time_time = time.mktime(date_time.timetuple())
			# time_time
			new_sex = request.POST.get("sex", '')
			new_phone = request.POST.get("phone", '')

			u.password = new_password if old_password == u.password and new_password != '' else u.password
			u.mail = u.mail if new_mail == '' else new_mail
			u.website = u.website if new_website == '' else new_website
			u.birth = u.birth if new_birth == '' else birth_date_time
			u.sex = u.sex if new_sex == '' else int(new_sex)
			u.photo = u.photo if new_photo == '' else new_photo
			
			u.save()
			
	return render_to_response("personal.html", locals(), context_instance = RequestContext(request))

def logout(request):
	del request.session["user_id"]
	return HttpResponseRedirect("/")

def login(request):
	if request.method == 'POST':
		if request.session.test_cookie_worked():	
			request.session.delete_test_cookie()
			#check username and password
			#...
			#...
			#set
			#request.session["username"] = "cjs"
			#get
			#password = request.session["password"]
			#clear
			#del request.session["username"]
			#check if exist
			#if "username" in request.session
			#
			try:
				u = user.objects.get(nickname=request.POST['username'])
				if u.password == request.POST['password']:
					request.session['user_id'] = u.id
					return HttpResponseRedirect("/personal/")
					# return render_to_response("personal.html", context_instance=RequestContext(request))
			except user.DoesNotExist:
				return HttpResponse("Your username and password didn't match!")
		else:
			return HttpResponse("Please enable cookies and try again")

	request.session.set_test_cookie()
	return render_to_response("login.html")

def index(request):
	_username = "陈坚生"
	_username = _username.decode("utf-8")

	cjs = user.objects.get(realname=_username)
	cjsblog = blog.objects.get(useby=cjs)
	cjsarticle = article.objects.filter(blogname=cjsblog, state="exist")
	print cjs.nickname
	return render_to_response("myblog.html",locals(),context_instance=RequestContext(request))

def hello(request):
    return HttpResponse("Hello world! my blog is test")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)