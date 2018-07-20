from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path("userList/", views.userList, name='userlist'),
    path("get_userlist/", views.get_userlist),
    path("detailaccount/<int:accountId>", views.detailaccount, name='detailaccount'),
    path("specifyaccount/", views.specifyaccount),
    path("getAllTweets/<int:pageNumber>", views.getAllTweets, name='tweetslist'),
    path("error/", views.page_not_found)
]
# if not settings.DEBUG:
#     urlpatterns += [、
#         url(r'^static/(?P<path>.*)$', serve,
#             {'document_root': settings.STATIC_ROOT, 'show_indexes': settings.DEBUG})
#     ]

app_name = 'inforShow'
handler404 = "views.page_not_found"