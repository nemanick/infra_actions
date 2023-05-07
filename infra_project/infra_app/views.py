from django.http import HttpResponse


def index(request):
    return HttpResponse('Ну теперь 1000% получится деплой! ;-((')


def second_page(request):
    return HttpResponse('А это вторая страница!')
