from django.contrib.auth.context_processors import auth
from Usuarios.models import Avatar


def custom_user_avatar(request):
    
    context = auth(request)
    user = context['user']
    
    if user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user.id)
        if len(avatar) > 0:
            context['user_avatar'] = avatar[0]
        else:
            context['user_avatar'] = ""
    return context