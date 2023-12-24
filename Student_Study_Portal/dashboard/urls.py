from django.urls import path
from .import views


urlpatterns = [

    #These URL is for Notes Module
    path('',views.home,name="home"),
    path('notes',views.notes,name="notes"),
    path('delete_note/<int:pk>',views.delete_note,name="delete-note"),
    path('notes_detail/<int:pk>',views.NotesDetailsView.as_view(),name="notes-detail"),
    

    #These URL is for Homework Module
    path('homework',views.homework,name="homework"),
    path('update_homework/<int:pk>',views.update_homework,name='update-homework'),
    path('delete_homework/<int:pk>',views.delete_homework,name="delete-homework"),

    #These URL is for YouTube Module
    path('youtube',views.youtube,name="youtube"),


    #These URL is for TO-DO TASK Module
    path('todo',views.todo,name="todo"),
    path('update_todo/<int:pk>',views.update_todo,name="update-todo"),
    path('delete_todo/<int:pk>',views.delete_todo,name="delete-todo"),


    #These URL is for Books Module
    path('books',views.books,name='books'),

    #These URL is for Books Module
    path('dictionary',views.dictionary,name="dictionary"),

    #These URL is for WiKiPedia Module
    path('wiki',views.wiki,name="wiki"),


    #These URL is for WiKiPedia Module
    path('conversion',views.conversion,name="conversion"),


    #This URL is for register Module
    path('register',views.register,name="register")




    

]
