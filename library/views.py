from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Sum
from datetime import date
from datetime import datetime
# Create your views here.
from library.models import Book, Category, Student, Borrow


def index(request):
    return render(request, "index.html", {})


def categories(request):
    if request.method == "POST":
        title = request.POST['title']

        Category(title=title).save()
        return redirect('/categories')
    categories = Category.objects.all()
    return render(request, "category.html", {"categories": categories})


def delete_category(request, id):
    category = Category.objects.filter(id=id)
    category.delete()
    return redirect('/categories')


def edit_category(request, id):
    category = Category.objects.filter(id=id).get()
    return JsonResponse({'title': category.title})


def books(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        cat = Category.objects.get(id=int(request.POST['category_id']))
        description = request.POST['description']
        available = int(request.POST['quantity'])

        book = Book(title=title, author=author, description=description, available=available)
        book.save()
        if book.categories.add(cat):
            return redirect('/books')
    books = Book.objects.all()
    categories = Category.objects.all()
    return render(request, "books.html", {"books": books, "categories": categories})


def edit_book(request, id):
    book = Book.objects.filter(id=id).get()
    return JsonResponse(
        {'title': book.title, 'author': book.author, 'description': book.description, 'available': book.available})


def delete_book(request, id):
    book = Book.objects.filter(id=id).get()
    book.delete()
    return redirect("/books")


def students(request):
    if request.method == "POST":
        sid = request.POST["sid"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        department = request.POST["department"]
        section = request.POST["section"]
        year = request.POST["year"]

        student = Student(student_id=sid, firstname=firstname, lastname=lastname, department=department,
                          section=section, year=year)
        student.save()
        return redirect("/students")
    students = Student.objects.all()
    return render(request, "students.html", {"students": students})


def borrow(request):
    if request.method == "POST":
        student_id = request.POST['student_id']
        student = Student.objects.get(id=student_id)
        status = "Borrowed"
        books_id = request.POST.getlist('selector')
        for book_id in books_id:
            book = Book.objects.get(id=book_id)
            b = Borrow(qty=1, status=status)
            b.save()
            b.student.add(student)
            b.book.add(book)
            return redirect("/borrow")
    students = Student.objects.all()
    books = Book.objects.all()
    datas = []
    for book in books:
        left = Borrow.objects.filter(status="Borrowed", book__title=book.title).aggregate(Sum('qty'))
        if left['qty__sum'] is None:
            l = 0
        else:
            l = int(left['qty__sum'])
        datas.append(book.available - l)
    return render(request, "borrow.html", {"datas": zip(books, datas), "students": students})


def returning(request):
    if request.method == "POST":
        b_id = int(request.POST["borrow_id"])
        borrow = Borrow.objects.get(id=b_id)
        borrow.date = datetime.now()
        borrow.status = "Returned"
        borrow.save()
        return redirect('/returning')
    borrows = Borrow.objects.all()
    return render(request, "return.html", {"borrows": borrows})
