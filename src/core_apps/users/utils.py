from rest_framework_simplejwt.tokens import RefreshToken


def get_jwt_token(user_obj):
    """A util funtion to generate JWT token for user"""
    
    refresh = RefreshToken.for_user(user=user_obj)
    return {"refresh": str(refresh), "access": str(refresh.access_token)}
