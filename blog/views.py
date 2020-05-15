from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse



@api_view(['GET'])
def api_root(request, format=None):
    response = Response({
        'sign-up': reverse('signup', request=request, format=format),
        'login': reverse('rest_login', request=request, format=format),
        'logout': reverse('rest_logout', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'posts': reverse('posts', request=request, format=format),
        'post-create': reverse('post-create', request=request, format=format),

    })

    return response