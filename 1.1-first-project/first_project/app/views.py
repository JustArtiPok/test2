import os
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('current_time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    try:
        # Получаем список файлов в текущей директории
        files = os.listdir('.')
        # Формируем текст для вывода
        if files:
            # Объединяем файлы с переносом строки
            files_list = '\n'.join(files)
            msg = f'Содержимое рабочей директории:\n{files_list}'
        else:
            msg = 'Рабочая директория пуста'
    except Exception as e:
        msg = f'Ошибка при чтении директории: {e}'
    
    return HttpResponse(msg, content_type='text/plain; charset=utf-8')