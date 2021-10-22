from django.shortcuts import render, get_object_or_404
from .models import Link
from django.contrib import messages


# Create your views here.
def Home(request):
    if request.method == 'POST':
            new_link = Link.objects.create(url = request.POST['url'])
            print(f'hhttp://127.0.0.1:8000/link/{new_link.pk}')
            messages.success(request, f'Your link has been created and press the copy button to copy it to clipboard!')
            context = {
                'copy': f'http://127.0.0.1:8000/link/{new_link.pk}',
            }
            return render(request, 'home.html', context=context)
    else:
        return render(request, 'home.html')



def Redirect(request, pk):
    link = get_object_or_404(Link, pk=pk)
    context = {
        'link': link.url,
        'redirect': True,
        'title': 'Redirect'
    }
    return render(request, 'redirect.html', context=context)