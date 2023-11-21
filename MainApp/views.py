from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]


# Create your views here.

def home(request):
    # text = """<h1>"Изучаем django День первый"</h1>
    #         <strong>Автор</strong>: <i>Иванов И.П.</i>"""
    # return HttpResponse(text)

    context = {
        "name": "Петров Николай Иванович",
        "email": "my_mail@mail.ru"
    }

    return render(request,'index.html', context)

def about(request):

    anketa = {
        "Имя":"Иван",
        "Отчество":"Петрович",
        "Фамилия":"Иванов",
        "телефон":"8-923-600-01-02",
        "email":"vasya@mail.ru"
    }
    text = f"""Имя: <b>{anketa['Имя']}</b><br>
        Отчество: <b>{anketa['Отчество']}</b><br>
        Фамилия: <b>{anketa['Фамилия']}</b><br>
        телефон: <b>{anketa['телефон']}</b><br>
        email: <b>{anketa['email']}</b><br>
"""
    return HttpResponse(text)

def get_item(requset, id):

    for item in items:
        if item['id'] == id:
            text = f"""<h1>Название: {item['name']}</h1> 
            <p>Количество: {item['quantity']}<p>
            <a href='/items'>Назад </a>
            """
            return HttpResponse(text)
        
    return HttpResponseNotFound(f"""Товар с {id=} не найден""")

def get_items(requset):

    # text = "<h2>Список товаров</h2><ol>"
    # for item in items:
    #     text += f"<li><a href='/item/{item['id']}'>Название: {item['name']}</li>"
    # text += "</ol>" 
    # return HttpResponse(text)

    context = {
        "items" : items
    }
    return render(requset, "get_items.html", context)