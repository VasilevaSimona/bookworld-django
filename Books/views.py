from django.shortcuts import render, redirect
from .models import Book
from datetime import datetime
from .forms import BookForm
def books(request):
    if request.method=="POST":
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            book=form.save(commit=False)
            book.user=request.user
            book.save()
            return redirect("books")
    #queryset=Book.objects.filter(author__first_name="John").all()
    queryset=Book.objects.filter(user=request.user).all()
    context={"books":queryset,"Date":datetime.now().date(),"form":BookForm}
    return render(request,"index.html", context=context)