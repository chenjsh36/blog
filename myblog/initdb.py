from myblogapp.models import user, blog, article, comment, tag

import datetime
_birth = datetime.datetime(1994,02,14)
user1 = user(realname="陈坚生", password="123456", userid="1", nickname="chenjsh36", state="manager", birth=_birth,sex=0)
user1.save()

users = user.objects.all()
users

cjs = user.objects.get(realname="陈坚生")

current_time = datetime.datetime.now()
blog1 = blog(useby=cjs, name="chenjsh36's blog", birth=current_time, words="千里之行始于足下", state="exist")
blog1.save()

cjsblog = blog.objects.get(name="chenjsh36's blog")

create_time = datetime.datetime.now();

article1 = article(writer=cjs, blogname=cjsblog, state="exist", createtime=create_time, modiftime=create_time, title="文章", content="write something here")
article1.save()

tag1 = tag(name="web")
tag1.save()
tag1.articles.add(article1)

tag2 = tag(name="django")
tag2.save()
tag2.articles.add(article1)

birth3 = datetime.datetime.now()
user3 = user(realname="路人1",password="123456",userid="2",nickname="luren",state="tourist",birth=birth3,sex=0)
user3.save()

_comment1time = datetime.datetime.now()
comment1 = comment(byarticle=article1, byuser=user3, state="waitreply", time=_comment1time, content="好文章，need to save")
comment1.save()

comment2 = comment(byarticle=article1, byuser=cjs, state="waitreply", time=datetime.datetime.now(), content="谢谢！", supercomment=comment1)
comment2.save()
comment1.subcomment = comment2
comment1.state = "replied"