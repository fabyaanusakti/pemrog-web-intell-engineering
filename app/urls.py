from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('detail_projek/projek=<int:pk>/', detail_projek_view, name='detail_projek'),
    path('profile/', profile_view, name='profile'),
    # ---- Start of Homepage View Address ---- #
    path('', home, name='home'),
    # ---- End of Homepage View Address ---- #

    # ---- Start of Users Page Address---- # 
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # ---- End of Users  Page Address---- # 

    # ---- Start of Project Page Address ---- #
    path('projek/', projek_view, name='projek'),
    path('projek/projek=<int:pk>/edit/', edit_projek, name='edit_projek'),
    path('projek/projek=<int:pk>/delete/', delete_projek, name='projek_delete'),
    # ---- End of Project Page Address ---- #

    # ---- Start of Meaningfull Objectives Page Address ---- #
    path('meaningful_objectives/', objectives_view, name='objectives_view'),
    # ---- End of Meaningfull Objectives Page Address ---- #

    # ---- Start of Intelligence Experience Page Address ---- #
    path('intelligence_experince/', experience_view, name='experience_view'),
    # ---- End of Intelligence Experience Page Address ---- #

    # ---- Start of Intelligence Implementation Page Address ---- #
    path('intelligence_implementation/', implementation_view, name='implementation_view'),
    # ---- End of Intelligence Implementation Page Address ---- #

    # ---- Start of Limitation Page Address ---- #
    path('batasan_pengembangan/', limitation_view, name='limitation_view'),
    # ---- End of Limitation Page Address ---- #

    # ---- Start of Realization Page Address ---- #
    path('status_realisasi/', realization_view, name='realization_view'),
    # ---- End of Realization Page Address ---- #

    # ---- Start of Planning Page Address ---- #
    path('perencanaan/', planning_view, name='planning_view'),
    # ---- End of Planning Page Address ---- #
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

