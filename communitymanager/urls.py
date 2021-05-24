from django.urls import path
from communitymanager import views


urlpatterns = [
    path('communautes', views.communautes, name='commus'),
    path('communaute/<int:id_commu>-<str:nom_commu>', views.communaute, name='commu'),
    path('post/<int:id_post>-<slug:slug_post>', views.post, name='post'),
    path('nouveau_post', views.nouveau_post, name='nouveau_post'),
    path('modif_post/<int:id_post>', views.modif_post, name='modif_post'),
    path('news_feed', views.news_feed, name='news_feed'),

    ]