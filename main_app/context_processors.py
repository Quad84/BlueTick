from .models import BlueTick_info
def info_func(request):

    info = BlueTick_info.objects.first()

    return {
        'info' : info
    }