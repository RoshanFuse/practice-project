from django.contrib import admin
from django.urls import path
from enroll import views

# for customise the admin panel
admin.site.site_header = 'developer roshan'
admin.site.site_title = 'my world'
admin.site.index_title = 'roshan'
###############################################

urlpatterns = [
    path('',views.add_show,name='addshow'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
]
