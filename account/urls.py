from django.conf.urls import url
from django.urls import reverse_lazy

from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    # url(r'^login/$', views.user_login, name='user_login'),
    url(r"^login/$", auth_views.LoginView.as_view(template_name='account/login.html'), name='user_login'),
    url(r"^new-login/$", auth_views.auth_login, {"template_name": "account/login.html"}),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='user_logout'),
    url(r'^register/$', views.register, name="user_register"),
    url(r'^password-change/$', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change_form.html',



        success_url=reverse_lazy('account:password_change_done')), name='password_change'),
    url(r'^password-change-done/$', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'), name='password_change_done'),
    url(r'^password-reset/$', auth_views.PasswordResetView, {"template_name": "account/password_reset_form.html",
                                                             "email_template_name": "account/password_reset_email.html",
                                                             "post_reset_redirect": "/account/password-reset-done"}, name="password_reset"),
    url(r'^password-reset-done/$', auth_views.PasswordResetDoneView,
        {"template_name": "account/password_reset_done.html"}, name="password_reset_done"),
    url(r'^password-reset-confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.PasswordResetConfirmView,
        {"template_name": "account/password_reset_confirm.html",
         "post_reset_redirect": "/account/password-reset-complete"}, name="password_reset_confirm"),
    url(r'^password-reset-complete/$', auth_views.PasswordResetCompleteView,
        {"template_name": "account/password_reset_complete.html"}, name="password_reset_complete"),
    url(r'^my-information/$', views.myself, name="my_information"),
    url(r'^edit-my-information/$', views.myself_edit, name="edit_my_information"),
    url(r'^my-image/$', views.my_image, name="my_image"),
]