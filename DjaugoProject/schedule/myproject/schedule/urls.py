from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_list, name='schedule_list'),  # スケジュール一覧ページ
    path('add/', views.add_schedule, name='add_schedule'),  # 行動登録ページ
]