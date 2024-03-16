from django.urls import path
from.import views

urlpatterns = [
    path('', views.home),
    path('connecthub/', views.loginfn),
    path('signup/', views.signuppagefn),
    path('signupfn/', views.signupfn),
    path('logouthub/', views.logoutfnhub),
    path('search1/', views.searchpagefn),
     path('search2/', views.searchfn),
    path('create1/', views.createpostfn),
    path('userview/', views.userviewfn),
    path('addprofile/', views.addprofilefn),
    path('editprofile/', views.editprofilefn),
    path('proview/<int:id>', views.proviewfn),
    path('editpost/', views.editpostpgfn),
    path('editc/<int:pr_id>', views.editpostfn),
    path('deletec/<int:pr_id>', views.dltpostfn),
    # path('feed/', views.feeffn),

]