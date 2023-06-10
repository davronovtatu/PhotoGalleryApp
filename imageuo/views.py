from django.shortcuts import render,redirect
from .models import Category,Photo
from .forms import PhotoForm,CategoryForm




# Bosh sahifa uchun view
def galleryphoto(request, category_id=None):  # category_id ni argument sifatida qo'shing
    if category_id is not None:
        photos = Photo.objects.filter(category_id=category_id)
    else:
        photos = Photo.objects.all()

    categories = Category.objects.all()
    context = {
        'photos': photos,
        'categories': categories,
    }
    return render(request, 'photo/gallery.html', context)


# rasimni ko'rish uchun view
def detailphoto(request,pk):
    photo=Photo.objects.get(id=pk)
    context={
        'photo':photo
    }
    return render(request,'photo/detail.html',context)

#  rasim qoshish uchun view
def addphoto(request):
    if request.method=='POST':
        form=PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form=PhotoForm()
    return render(request,'photo/add.html',{ 'form':form })

#  kategoriya qoshish uchun view

def addcategory(request):
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form=CategoryForm()
    return render(request,'photo/category.html',{ 'form':form })
