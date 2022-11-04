from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('panel/',views.panel,name='panel'),
    path('panel/about/', views.AboutModel.as_view(),name='about_form'),
    path('panel/update_logo/<int:pk>',views.UpdateLogo.as_view(),name='update_logo'),
    path('panel/update_phone/<int:pk>',views.UpdatePhone.as_view(),name='update_phone'),
    path('panel/update_about/<int:pk>/',views.UpdateAbout.as_view(),name='update_about'),
    path('panel/photo_add/', views.PhotoAdd.as_view(),name='photo_add'),
    path('panel/offer_add/', views.OfferAdd.as_view(),name='offer_add'),
    path('panel/list_offer/',views.ListOffersView.as_view(),name='list_offer'),
    path('panel/delete_offer/<int:pk>',views.DeleteOffer.as_view(),name='delete_offer'),
    path('panel/thank_you/',views.thank_you,name='thank_you'),
    path('panel/photo_list',views.ListPhotoes.as_view(),name='photo_list'),
    path('panel/delete_photo/<int:pk>/',views.DeletePhotoes.as_view(),name='delete_photo'),
    path('panel/update_photo/<int:pk>',views.UpdatePhoto.as_view(),name='update_photo')
]