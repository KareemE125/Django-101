from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name': 'John Doe',
        'age': 30,
        'hobbies': ['Football', 'Music', 'Programming'],
    }
    return render(request, 'pages/index.html', context)

def default(request):
    return render(request, 'pages/default.html')
