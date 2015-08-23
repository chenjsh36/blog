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

article1 = article(writer=cjs, blogname=cjsblog, state="exist", createtime=create_time, modiftime=create_time, title="第一篇文章", content="""
[b]参考资料：[/b][b]多对多关系建立和访问： [url=http://www.redicecn.com/html/Python/20120505/399.html]http://www.redicecn.com/html/Python/20120505/399.html[/url][/b]
[b]Django 字段类型清单： [url=http://www.cnblogs.com/lhj588/archive/2012/05/24/2516040.html]http://www.cnblogs.com/lhj588/archive/2012/05/24/2516040.html[/url]
[/b]Django Book 2.0: [url=http://docs.30c.org/djangobook2/]http://docs.30c.org/djangobook2/[/url]
Django,数据模型创建之数据库API参考:[url=http://www.cnblogs.com/micky-zhou/archive/2013/03/15/2961780.html]http://www.cnblogs.com/micky-zhou/archive/2013/03/15/2961780.html[/url]
在SAE上搭建django+mysql+python：[url=http://blog.csdn.net/luanjiyang/article/details/37879747]http://blog.csdn.net/luanjiyang/article/details/37879747[/url]
[b]遇到的问题：[/b]
*Python脚本运行出现语法错误：IndentationError: unindent does not match any outer indentation level：[url=http://www.crifan.com/python_syntax_error_indentationerror/comment-page-1/]http://www.crifan.com/python_syntax_error_indentationerror/comment-page-1/[/url]
*settings.DATABASES is improperly configured. Please supply the ENGINE value. Check settings documentation for more details.:[url=http://blog.csdn.net/wangziling100/article/details/7627718]http://blog.csdn.net/wangziling100/article/details/7627718[/url]
*OperationalError: (2013, "Lost connection to MySQL server at 'waiting for initial communication packet', system error: 0") :install mysql
* Error loading MySQLdb module: this is MySQLdb version (1, 2, 4, 'beta', 4), but _mysql is version (1, 2, 4, 'final' , 1):[url=http://www.cnblogs.com/zhxhdean/p/3173663.html]http://www.cnblogs.com/zhxhdean/p/3173663.html[/url]
*django: 开发服务器下admin界面没有css：[url=http://blog.csdn.net/fengyu09/article/details/17923737]http://blog.csdn.net/fengyu09/article/details/17923737[/url]
*SAE导入sql文件：去除所有lock和unlock和drop语句、导入时兼容格式设置为mysql40，由于window不区分大小写，但sae上区分，所以会导致进入admin后仍然不能访问的问题
[b]实验：SAE上搭建django+mysql+python[/b]
""")
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