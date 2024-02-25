from django.shortcuts import render

def home_view(request):
    # Logic for rendering the home page
    return render(request, 'pages/home.html')

def about_view(request):
    # Logic for rendering the about page
    return render(request, 'pages/about.html')
