from django.urls import path

from core_apps.users.views import UserRegistrationAPI, UserLoginAPI, UserTokenObtainPairView


urlpatterns = [
    path(
        "signup/",
        UserRegistrationAPI.as_view(),
        name="user_signup_api",
    ),
    path("login/", UserLoginAPI.as_view(), name="user_login_api"),
    path("get-token/", UserTokenObtainPairView.as_view(), name="get_token"),
]
