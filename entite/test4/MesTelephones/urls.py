from django.urls import path
from . import views 

urlpatterns = [
    #path('', views.index, name='MesTelephones'),
    path('MesTelephones/' ,views.index, name='MesTelephones'),
    path('types/', views.list_typ, name='types'),
    path('del_typ/<int:id>', views.del_typ, name='del_typ'),
    path('MesTelephones/update_typ/<int:id>', views.update_typ,name='update_typ'),
    path('MesTelephones/update_typ/update_typ_action/<int:id>',views.update_typ_action, name='update_typ_action'),
    path('MesTelephones/addtele/', views.add, name='add'),
    path('MesTelephones/addtele/add_tele/', views.add_tele, name='add_tele'),
    path('users/', views.list_users, name='users'),
    path('users/createUser/', views.create_compte, name='create_compte'),
    path('users/createUser/add_user_action/', views.create_user_action,name='create_user_action'),
    path('users/del_user/<int:id>', views.del_user, name='del_user'),
    path('', views.connect, name='connect'),
    path('login/login/', views.signIn, name='signIn'),
    path('login/', views.signIn, name='signIn'),
    path('disconnect/', views.signOut, name='disconnect'),
    ]