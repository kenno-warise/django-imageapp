from django.shortcuts import render, redirect
from .models import Image
from .forms import ImageCreateForm


def top_page(request):
    images = Image.objects.all()
    context = {
            'images': images,
    }
    return render(request, 'images/top-page.html', context)

def form_page(request):
    if request.method == 'POST':
        form = ImageCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('images:top_page')
    else:
        form = ImageCreateForm()
    context = {
            'form': form
    }
    return render(request, 'images/form-page.html', context)
