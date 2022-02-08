"""NotesSharingProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',about,name='about'),
    path('',index,name='index'),
    path('contact', contact, name='contact'),
    path('login', userlogin, name='login'),
    path('login_admin', login_admin, name='login_admin'),
    path('signup', signup1, name='signup'),
    path('admin_home', admin_home, name='admin_home'),
    path('logout', Logout, name='logout'),
    path('profile', profile, name='profile'),
    path('changepassword', changepassword, name='changepassword'),
    path('edit_profile', edit_profile, name='edit_profile'),
    path('upload_notes', upload_notes, name='upload_notes'),
    path('view_mynotes', view_mynotes, name='view_mynotes'),
    path('delete_mynotes/<int:pid>', delete_mynotes, name='delete_mynotes'),
    path('view_allnotes', view_allnotes, name='view_allnotes'),
    path('view_users', view_users, name='view_users'),
    path('delete_users/<int:pid>', delete_users, name='delete_users'),
    path('pending_notes', pending_notes, name='pending_notes'),
    path('accepted_notes', accepted_notes, name='accepted_notes'),
    path('rejected_notes', rejected_notes, name='rejected_notes'),
    path('all_notes', all_notes, name='all_notes'),
    path('assign_status/<int:pid>', assign_status, name='assign_status'),
    path('delete_notes/<int:pid>', delete_notes, name='delete_notes'),
    path('viewallnotes', viewallnotes, name='viewallnotes'),
    path('change_passwordadmin', change_passwordadmin, name='change_passwordadmin'),
    path('unread_queries', unread_queries, name='unread_queries'),
    path('read_queries', read_queries, name='read_queries'),
    path('view_queries/<int:pid>', view_queries, name='view_queries'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
